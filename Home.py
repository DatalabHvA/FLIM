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

# ---------- Session state ----------
ss = st.session_state
ss.setdefault("events_epoch", 0)       # to invalidate plotly_events widget state
if 'prijzen_df' not in ss:
    ss.prijzen_df = pd.read_excel('data/prijzen.xlsx')
if 'geo_df' not in ss:
    ss.geo_df = pd.read_excel('data/material_market_share.xlsx')
if 'wgi_df' not in ss:
    ss.wgi_df = pd.read_excel('data/wgi_governance_scores_2023_with_iso3.xlsx')

if 'selected_materials' not in ss:
    ss.selected_materials = ['Hout','Aluminium','Textiel', 'Katoen']
if 'selected_material_prijs' not in ss:
    ss.selected_material_prijs = 'Hout'
if 'selected_material_geo' not in ss:
    ss.selected_material_geo = 'Hout'
if 'heatmap_label' not in ss:
    ss.heatmap_label = 'ESPR [2026]'
if 'bubble_label' not in ss:
    ss.bubble_label = 'Rvo.nl nationale subsidies'
    
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
def get_prijs_kpi(materials_list):
    variance = ss.prijzen_df.drop('Jaar', axis = 1).std().rename('risk2').reset_index().rename(columns = {'index' : 'materiaal'})
    return variance.loc[lambda d: d['materiaal'].isin(materials_list)]

@st.cache_data(show_spinner=False)
def get_levzeker(materials_list):
        wgi = ss.geo_df.merge(ss.wgi_df, on = 'country').groupby('material').apply(lambda g: (g['market_share'] * g['governance_score']).sum()).rename('wgi_score')
        return wgi.reset_index().loc[lambda d: d['material'].isin(materials_list)][['material','wgi_score']].rename(columns = {'wgi_score' : 'supply_risk'})

# --- Figure builders (cached) ---

@st.cache_data(show_spinner=False)
def make_levzeker_bar_figure(x_labels: tuple, y: tuple, C_LAYOUT):
    colors = colors = ["#2ca02c" if v >= 0.75 else "#ffbf00" if v >= 0.4 else "#d62728" for v in y]

    fig = go.Figure(
        data=[go.Bar(x=list(x_labels), y=list(y), marker_color=colors,
                     hovertemplate="<b>%{x}</b><br>Zekerheid: %{y:.1f}<extra></extra>")]
    )
    fig.update_layout(
        height=CHART_HEIGHT, xaxis_title=None, yaxis_title="Index", showlegend=False,
        **C_LAYOUT
    )
    return fig

@st.cache_data(show_spinner=False)
def make_klantvraag_scatter(sel_hist_df: pd.DataFrame):
    
    fig = go.Figure()

    # add each line
    fig.add_trace(go.Scatter(
        x=[str(x) for x in klantvraag_df['Jaar']],
        y=[float(x) for x in klantvraag_df['Duurzame meubels (CAGR 2,8%)']],
        mode='lines+markers',
        name='Duurzame meubels (CAGR 2,8%)',
        line=dict(color='red', width=3),
        marker=dict(size=6)
    ))

    fig.add_trace(go.Scatter(
        x=[str(x) for x in klantvraag_df['Jaar']],
        y=[float(x) for x in klantvraag_df['Traditionele meubels (CAGR 7,3%)']],
        mode='lines+markers',
        name='Traditionele meubels (CAGR 7,3%)',
        line=dict(color='green', width=3),
        marker=dict(size=6)
    ))

    # layout tweaks
    fig.update_layout(
        xaxis_title="Jaar",
        yaxis_title="Index (2023 = 100)",
        template="plotly_white",
        **COMMON_LAYOUT,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    return fig

# --- Heatmap data (labels + values). Replace with your real source.
@st.cache_data(show_spinner=False)
def get_heatmap_series(seed: int = 7):
    wetgeving = pd.DataFrame({'label' : ['EUDR [2025]','ESPR [2026]', 'Right to repair directive [2026]', 'Plastics Norm [2026]', 'REACH [2007]', '(indrect via keten)'],
                             'value' : [1,2,3,4,5,6]})
    return wetgeving

# --- Heatmap figure (single column, many rows)
@st.cache_data(show_spinner=False)
def make_single_col_heatmap(labels: tuple, values: tuple, cmap: list, height: int = CHART_HEIGHT):
    import plotly.graph_objects as go

    # Reshape z and y
    z = [[value] for value in values]
    text = [[label] for label in labels]

    # Base heatmap (no text)
    heatmap = go.Heatmap(
        z=z,
        x=[""],
        y=labels,
        colorscale=cmap,
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

    st.session_state.selected_materials = st.multiselect(
        "Materialen",
        ss.prijzen_df.drop('Jaar', axis = 1).columns,
        default=st.session_state.selected_materials,
    )

# ---------- Data (apply filters where appropriate) ----------
# NOTE: Hook your real filters into these calls (branche/fte/omzet/etc.).
klantvraag_df = pd.DataFrame({'Jaar' : [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
                              'Duurzame meubels (CAGR 2,8%)' : [100.0,102.8,105.7,108.6,111.7,114.8,118.0,121.3],
                              'Traditionele meubels (CAGR 7,3%)' : [100.0,107.3,115.1,123.5,132.6,142.2,152.6,163.8]})



# ---------- Tiles ----------

def tile_prijsstijgingen(target_page):
    df_now   = get_prijs_kpi(tuple(st.session_state.selected_materials))      # cache key: selected materials

    st.subheader("Prijsstijgingen")
    st.write("Conclusie van deze factor.")
    st.caption("Klik op een balk voor trenddetails.")

    # --- build the bar chart (any way you like) ---
    x = tuple(df_now["materiaal"].tolist())
    y = tuple((df_now["risk2"]*100).tolist())
    
    colors = ["#2ca02c" if v <= 10 else "#ffbf00" if v <= 20 else "#d62728" for v in y]

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
    if clicks:
        mat = clicks[0].get("x")
        if mat:
            ss.selected_material_prijs = mat
            st.switch_page(target_page)

def tile_leveringszekerheid(target_page):
    df_now = get_levzeker(tuple(st.session_state.selected_materials))
    st.subheader("Leveringszekerheid")
    st.caption("Klik op een balk om de wereldkaart te openen.")

    x = tuple(df_now["material"].tolist())
    y = tuple(df_now["supply_risk"].tolist())
    fig = make_levzeker_bar_figure(x, y, COMMON_LAYOUT)  # cached

    clicks = plotly_events(
        fig,
        click_event=True, hover_event=False, select_event=False,
        override_height=320, override_width="100%",
        key=f"evt_zeker_{ss.events_epoch}",
    )

    if clicks:
        mat = clicks[0].get("x")
        if mat:
            ss.selected_material_geo = mat
            st.switch_page(target_page)

def tile_klantvraag(df, target_page: str):
    with st.container(border=False):
        st.subheader("Klantvraag")
        st.caption("Klik op de grafiek om details te openen.")
        fig = make_klantvraag_scatter(df)
        clicks = plotly_events(
            fig,
            click_event=True, hover_event=False, select_event=False,
            override_height=CHART_HEIGHT, override_width="100%",
            key=f"evt_klantvraag_{st.session_state.events_epoch}",
        )
        if clicks:
            # For Heatmap, Plotly returns y = row label (our 'label')
            st.switch_page(target_page)

def tile_heatmap_to_page(df, target_page: str):
    with st.container(border=False):
        st.subheader("Wet- en regelgeving")
        st.caption("Klik op een item om details te openen.")
        colorscale = [
            [0.0, '#ff0000'],  # strong red
            [1.0, '#ffe5e5']   # very light red
        ]
        labels = tuple(df["label"].tolist())
        values = tuple(df["value"].tolist())
        fig = make_single_col_heatmap(labels, values, cmap = colorscale, height=CHART_HEIGHT)

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

def tile_personeel(target_page):
    with st.container(border=False):
        st.subheader("Personeel")

def tile_financierseisen(target_page):
    with st.container(border=False):
        st.subheader("Subsidies en financierseisen")
        # Example DataFrame
        df = pd.DataFrame({
            'label': [
                'BMKB-Groen', 'ISDE', 'MT / MOOI subsidies', 'Klimaatfonds', 
                'EIC Accelerator / EIT Raw Materials', 'Wur Europe / Cluster 6', 
                'Circular Future Funding (norm.)', 'LIFE programma', 
                'ESPR / Ecodesign & Product passport', 'Rvo.nl nationale subsidies'
            ],
            'x': [0.9, 1.6, 0.55, 0.6, 3.0, 3.4, 2.4, 3.45, 3.1, 1.7],
            'y': [2.4, 1.5, 1.85, 1.3, 2.4, 1.9, 1.0, 0.9, 1.45, 2.0],
            'color': ['green', 'orange', 'green', 'red', 
                    'green', 'green', 'orange', 'red', 'orange', 'yellow']
        })
        df["wrapped"] = df["label"].apply(lambda s: "<br>".join([s[i:i+20] for i in range(0, len(s), 20)]))
        # Create the figure
        fig = go.Figure()

        # Add bubbles
        fig.add_trace(go.Scatter(
            x=[float(x) for x in df['x']],
            y=[float(y) for y in df['y']],
            mode='markers+text',
            text=[str(label) for label in df['wrapped']],
            textposition='middle center',
            textfont=dict(color="black", size=8),
            marker=dict(
                size=70,
                color=df['color'],
                line=dict(color='black', width=1)
            ),
            customdata=df['label'],
            hoverinfo='text'
        ))

        # Add flag images
        fig.add_layout_image(
            dict(
                source="https://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg",
                x=0.9,
                y=2.7,
                sizex=0.5,
                sizey=0.25,
                xref="x",
                yref="y",
                xanchor="center",
                yanchor="bottom",
                layer="above"
            )
        )

        fig.add_layout_image(
            dict(
                source="https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg",
                x=3.0,
                y=2.7,
                sizex=0.5,
                sizey=0.25,
                xref="x",
                yref="y",
                xanchor="center",
                yanchor="bottom",
                layer="above"
            )
        )

        # Layout styling
        fig.update_layout(
            template="plotly_white",
            xaxis=dict(visible=False, range=[0, 4]),
            yaxis=dict(visible=False, range=[0, 3]),
            margin=dict(t=0, b=0, l=0, r=00),
            height=500
        )

        # Handle clicks
        click = plotly_events(
            fig,
            click_event=True, select_event=False, hover_event=False,
            override_height=500, override_width="100%", key="bubble_chart"
        )

        if click:
            selected = click[0]["pointIndex"]
            bubble_click = df.iloc[selected]['label']
            st.session_state["bubble_label"] = bubble_click
            st.switch_page(target_page)

def tile_subsidies():
    st.subheader("Subsidies")
    st.caption("Klik op een ondersteept item om details te openen.")
    c1, c2 = st.columns(2)
    with c1: 
        st.image("https://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg")
    with c2: 
        st.image("https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg")


    # Sample content and row colors
    labels = ['<b> Verkenning</b>', 'TSE Industrie - studies', '<a href="/a_MIT_haalbaarheid", target = "_self"<u>MIT - Haalbaarheid</u></a>', '','<b>Ontwikkeling</b>', 'MIT - R&D samenwerking', 'DEI+ - Circulaire Economie', 'VEKI - Versnelde Klimaatinvesteringen', '<b>Implementatie</b>', 'MIA\Vamil', 'CKP - Circulaire Ketenprojecten', '', '<b>Opschaling</b>', 'EFRO (Regionaal)', ' ', '']
    values = ['', 'Horizon Europe - Cluster 4', 'EIR RawMaterials - Innovation Program', 'Life Programme - Circulair Economy', '', 'Horizon Europe - Cluster 5', 'Interreg - Circular Economy & Green Growth', 'COST Action - Circular Economy Innovation', '', 'Horizon Europe - EIC Accelerator', '<a href="/b_EDFR", target = "_self"<u>EDRF - Circular Economy</u></a>', 'Life Programme',' ','Horizon Europe - Cluster 6', 'EIC Fund', 'Horizon Europe - European Green Deal']
    row_colors = [
        "#8BC4F9", "#BADEF9", "#BADEF9","#BADEF9", "#FFC277",
        "#FAE3C6", "#FAE3C6", "#FAE3C6", "#6BFF70", "#CCFFCE",
        "#CCFFCE", "#CCFFCE", "#FF94E2", "#FFDFF7","#FFDFF7", "#FFDFF7"
    ]

    # Build HTML table
    html = '<table style="width:100%;">'
    for i in range(16):
        bg = row_colors[i]
        label = labels[i]
        value = values[i]
        html += f'<tr style="background-color:{bg};"> <td style="font-size: 12px; padding: 2px; text-align: center;">{label}</td> <td style="font-size: 12px; padding: 2px; text-align: center">{value}</td> </tr>'
    html += '</table>'

    # Render table in Streamlit
    st.markdown(html, unsafe_allow_html=True)

# ---------- Layout: 3 tiles in one row ----------
st.title("FLIM risico tool")
st.caption("Klik op de tegels/visualisaties om verder te navigeren of details te openen.")

col1, col2, col3 = st.columns(3, gap="small", border = True)
with col1: tile_prijsstijgingen(target_page = "pages/01_Prijsstijgingen.py")
with col2: tile_leveringszekerheid(target_page = "pages/02_Leveringszekerheid.py")
with col3: tile_klantvraag(klantvraag_df, target_page="pages/03_Klantvraag.py")
    
h1, h2, h3 = st.columns(3, gap="small", border = True)
with h1:
    heat_df = get_heatmap_series()
    tile_heatmap_to_page(heat_df, target_page = "pages/04_wet_regelgeving.py")
with h2:
    tile_personeel(target_page = "pages/05_personeel.py")
with h3:
    tile_subsidies()
