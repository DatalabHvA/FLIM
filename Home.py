# Home.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events
from datetime import datetime, timedelta
from PIL import Image
import base64
from pathlib import Path

# --- Layout ---
st.set_page_config(page_title="Dashboard • Home", layout="wide")
st.markdown(
    """
    <style>
      /* pull content up */
      .block-container { padding-top: 0.9rem !important; }
      /* compact header */
      header[data-testid="stHeader"] { height: 1.2rem; }
      [data-testid="stSidebarNav"] {display: none;}
      [data-testid="stSidebar"] .block-container {
          padding-top: 0 !important;
      }

    section[data-testid="stSidebar"] .block-container > div:first-child,
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: -60px !important;   /* <- adjust this number */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Overzicht")
st.caption("Klik op de tegels/visualisaties om verder te navigeren of details te openen.")

# ---------- Session state ----------
ss = st.session_state
ss.setdefault("events_epoch", 0)       # to invalidate plotly_events widget state
ss.setdefault("dialog_open", False)
ss.setdefault("prijs_dialog_payload", None)  # (material)
ss.setdefault("events_epoch", 0)
ss.selected_material = None
ss.clicks = None

# ---- shared layout so axes are fully visible and consistent
COMMON_LAYOUT = dict(
    margin=dict(l=40, r=5, t=20, b=60),
    xaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
    yaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
)
CHART_HEIGHT = 320

# ---------- Caching helpers ----------

@st.cache_data(show_spinner=False)
def bar_colors(values):
    # low<=33 green, 33–66 yellow, >66 red
    cols = []
    for v in values:
        if v <= 33:
            cols.append("#2ca02c")   # green
        elif v <= 66:
            cols.append("#ffbf00")   # yellow
        else:
            cols.append("#d62728")   # red
    return cols

# --- Demo data builders (cacheable; swap with your real loaders) ---
@st.cache_data(show_spinner=False)
def get_prijs_snapshot(materials_list, seed=1):
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "materiaal": materials_list,
        "prijsstijging_pct": rng.uniform(5, 90, size=len(materials_list)).round(1),
    })

@st.cache_data(show_spinner=False)
def get_prijs_history(materials_list, seed=1):
    rng = np.random.default_rng(seed)
    hist = []
    base_date = datetime.today() - timedelta(days=365)
    for m in materials_list:
        level = rng.uniform(20, 80)
        series = np.clip(level + np.cumsum(rng.normal(0, 1.8, 52)), 0, 120)
        hist.append(pd.DataFrame({
            "datum": [base_date + timedelta(days=7*i) for i in range(52)],
            "materiaal": m,
            "prijsstijging_pct": series.round(1),
        }))
    return pd.concat(hist, ignore_index=True)

@st.cache_data(show_spinner=False)
def get_levzeker(materials_list, seed=2):
    rng = np.random.default_rng(seed)
    return pd.DataFrame({
        "materiaal": materials_list,
        "zekerheid_index": rng.uniform(10, 95, size=len(materials_list)).round(1),
    })

# --- Figure builders (cached) ---

@st.cache_data(show_spinner=False)
def make_levzeker_bar_figure(x_labels: tuple, y_vals: tuple, C_LAYOUT):
    colors = bar_colors(y_vals)
    fig = go.Figure(
        data=[go.Bar(x=list(x_labels), y=list(y_vals), marker_color=colors,
                     hovertemplate="<b>%{x}</b><br>Zekerheid: %{y:.1f}<extra></extra>")]
    )
    fig.update_layout(
        height=CHART_HEIGHT, xaxis_title=None, yaxis_title="Index", showlegend=False,
        **C_LAYOUT
    )
    return fig

@st.cache_data(show_spinner=False)
def make_prijs_line_dialog_figure(sel_hist_df: pd.DataFrame):
    line = go.Figure()
    line.add_trace(go.Scatter(x=sel_hist_df["datum"], y=sel_hist_df["prijsstijging_pct"], mode="lines+markers",
                              hovertemplate="%{x|%d-%m-%Y}: %{y:.1f}%<extra></extra>"))
    line.update_layout(height=360, margin=dict(l=10, r=10, t=10, b=10),
                       xaxis_title=None, yaxis_title="%", showlegend=False)
    return line

# --- Heatmap data (labels + values). Replace with your real source.
@st.cache_data(show_spinner=False)
def get_heatmap_series(seed: int = 7):
    wetgeving = pd.DataFrame({'label' : ['EUDR [2025]','ESPR [2026]', 'Right to repair directive [2026]', 'Plastics Norm [2026]', 'REACH [2007]', '(indrect via keten)'],
                             'value' : [1,2,3,4,5,6]})
    return wetgeving

# --- Heatmap figure (single column, many rows)
@st.cache_data(show_spinner=False)
def make_single_col_heatmap(labels: tuple, values: tuple, height: int = CHART_HEIGHT):
    import plotly.graph_objects as go

    # Reshape z and y
    z = [[value] for value in values]
    text = [[label] for label in labels]

    # Base heatmap (no text)
    heatmap = go.Heatmap(
        z=z,
        x=[""],
        y=labels,
        colorscale="reds",
        reversescale=True,
        showscale=False,
        hoverinfo = 'none'
    )

    # Overlay text as scatter
    scatter = go.Scatter(
        x=[""]*len(labels),     # position text in center of each cell
        y=labels,
        mode="text",
        text=labels,
        textfont=dict(size=12, color="black"),
        hoverinfo="none",
        showlegend=False,
    )

    fig = go.Figure(data=[heatmap, scatter])

    fig.update_yaxes(
        autorange="reversed", showticklabels=False, showgrid=False, zeroline=False
    )
    fig.update_xaxes(
        showticklabels=False, showgrid=False, zeroline=False
    )
    fig.update_layout(
        template="plotly_white",
        height=height,
        xaxis_title=None,
        yaxis_title=None,
        margin=dict(t=40, b=30, l=30, r=0),
    )

    return fig
# ---------- Sidebar Filters ----------
with st.sidebar:
    st.header("Filters")
    branche = st.selectbox("Branche", ["Meubelmakers", "Interieurbouw"], index=0)
    medewerkers = st.selectbox("Aantal medewerkers", ["0–50 fte", "51–250 fte", "250+ fte"], index=0)
    omzet = st.selectbox("Omzet", ["<€10M", "<€50M", ">€50M"], index=1)
    klantsegment = st.selectbox("Klantsegment", ["Laag", "Midden", "Hoog"], index=1)
    klanttype = st.selectbox("Klanttype", ["B2C", "B2B", "Overheid"], index=1)

    materials = st.multiselect(
        "Materialen",
        [
            "spaanplaat",
            "Multiplex",
            "MDF plaatmateriaal",
            "Aluminium",
            "RVS 305",
            "Polytherureen Schuim",
            "Katoen",
            "Leer",
            "Plastic",
        ],
        default=["spaanplaat", "Multiplex", "MDF plaatmateriaal"],
    )

# ---------- Data (apply filters where appropriate) ----------
# NOTE: Hook your real filters into these calls (branche/fte/omzet/etc.).
prijs_now_df   = get_prijs_snapshot(tuple(materials))      # cache key: selected materials
prijs_hist_df  = get_prijs_history(tuple(materials))
levzeker_df    = get_levzeker(tuple(materials))

# ---------- Tiles ----------

def tile_prijsstijgingen(df_now: pd.DataFrame, df_hist: pd.DataFrame):
    st.subheader("Prijsstijgingen")
    st.caption("Klik op een balk voor trenddetails.")

    # --- build the bar chart (any way you like) ---
    x = df_now["materiaal"].tolist()
    y = df_now["prijsstijging_pct"].tolist()
    colors = ["#2ca02c" if v <= 33 else "#ffbf00" if v <= 66 else "#d62728" for v in y]

    fig = go.Figure(
        go.Bar(
            x=x, y=y, marker_color=colors,
            hovertemplate="<b>%{x}</b><br>Stijging: %{y:.1f}%<extra></extra>"
        )
    )
    fig.update_layout(height=CHART_HEIGHT, xaxis_title=None, yaxis_title="%", showlegend=False,
                      **COMMON_LAYOUT)

    # IMPORTANT: key includes epoch so old clicks are never replayed
    clicks = plotly_events(
        fig,
        click_event=True, hover_event=False, select_event=False,
        override_height=320, override_width="100%",
        key=f"evt_prijs_{ss.events_epoch}",
    )

    # If a click happened, open the dialog ONCE (this run), then "arm" the next run
    if clicks:
        materiaal = clicks[0].get("x")
        if materiaal:
            @st.dialog(f"Trend • {materiaal}", on_dismiss = 'rerun')
            def _show_dialog():
                # filter line data
                d = df_hist[df_hist["materiaal"] == materiaal].sort_values("datum")
                line = go.Figure(
                    go.Scatter(x=d["datum"], y=d["prijsstijging_pct"], mode="lines+markers",
                            hovertemplate="%{x|%d-%m-%Y}: %{y:.1f}%<extra></extra>")
                )
                line.update_layout(height=CHART_HEIGHT, xaxis_title=None, yaxis_title="%", showlegend=False, 
                                   **COMMON_LAYOUT)
                st.plotly_chart(line, use_container_width=True)

            _show_dialog()

            # --- after printing the dialog, bump epoch so the next rerun sees a fresh widget ---
            ss.events_epoch += 1
            # NOTE: no dialog flags, no payload stored — nothing to clean up on close

def tile_leveringszekerheid(df_now: pd.DataFrame):
    st.subheader("Leveringszekerheid")
    st.caption("Klik op een balk om de wereldkaart te openen.")

    x = tuple(df_now["materiaal"].tolist())
    y = tuple(df_now["zekerheid_index"].tolist())
    fig = make_levzeker_bar_figure(x, y, COMMON_LAYOUT)  # cached

    ss.clicks2 = plotly_events(
        fig,
        click_event=True, hover_event=False, select_event=False,
        override_height=320, override_width="100%",
        key=f"evt_zeker_{ss.events_epoch}",
    )

    if ss.clicks2:
        mat = ss.clicks2[0].get("x")
        if mat:
            ss.selected_material = mat
            st.switch_page("pages/02_Leveringszekerheid.py")

def tile_klantvraag_image(image_path: str, target_page: str):
    st.subheader("Klantvraag")
    st.caption("Klik op de figuur voor de klantvraag detailpagina.")

    def img_to_base64(path):
        return base64.b64encode(Path(path).read_bytes()).decode()

    img_b64 = img_to_base64("assets/klantvraag.png")
    st.markdown(
        f"""
        <a href="{target_page}" target="_self">
            <img id="centerimage" src="data:image/png;base64,{img_b64}" style="width:110%; height:{CHART_HEIGHT*0.8}px;
                          margin-top:40px;">
        </a>
        """,
        unsafe_allow_html=True
    )

def tile_heatmap_to_page(df, target_page: str):
    with st.container(border=False):
        st.subheader("Wet- en regelgeving")
        st.caption("Klik op een item om details te openen.")
        labels = tuple(df["label"].tolist())
        values = tuple(df["value"].tolist())
        fig = make_single_col_heatmap(labels, values, height=CHART_HEIGHT)

        clicks = plotly_events(
            fig,
            click_event=True, hover_event=False, select_event=False,
            override_height=CHART_HEIGHT+40, override_width="100%",
            key=f"evt_heatmap_{st.session_state.events_epoch}",
        )
        if clicks:
            # For Heatmap, Plotly returns y = row label (our 'label')
            sel_label = clicks[0].get("y")
            if sel_label:
                # Robust: set session state and (best-effort) URL param
                st.session_state["heatmap_label"] = sel_label
                st.write(sel_label)
                st.switch_page(target_page)


# ---------- Layout: 3 tiles in one row ----------
col1, col2, col3 = st.columns(3, gap="small", border = True)

with col1: tile_prijsstijgingen(prijs_now_df, prijs_hist_df)
with col2: tile_leveringszekerheid(levzeker_df)
with col3:tile_klantvraag_image(
            image_path="assets/klantvraag.png",
            target_page="/Klantvraag"
        )
    
# Second row: put the heatmap in the FIRST column
h1, h2, h3 = st.columns(3, gap="small", border = True)
with h1:
    heat_df = get_heatmap_series()
    tile_heatmap_to_page(heat_df, "pages/04_wet_regelgeving.py")
