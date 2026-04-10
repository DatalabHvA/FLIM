# Home.py
import numpy as np
import json
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events
import plotly.io as pio
from datetime import datetime, timedelta
from PIL import Image
import base64
from pathlib import Path

import streamlit.components.v1 as components
from widgets import *

def _iframe(html, height):
    if hasattr(st, "iframe"):
        st.iframe(html, height=height)
    else:
        components.html(html, height=height)

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

# Navigation guard — must run before any component renders
if ss.get("_navigate_to"):
    target = ss["_navigate_to"]
    del ss["_navigate_to"]
    st.switch_page(target)

log_event("Home", "page_load")

init_session_state()

# ---- shared layout so axes are fully visible and consistent
COMMON_LAYOUT = dict(
    margin=dict(l=40, r=15, t=20, b=60),
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

# --- Figure builders (cached) ---

@st.cache_data(show_spinner=False)
def make_levzeker_bar_figure(x_labels: tuple, y: tuple, C_LAYOUT):
    colors = ["#bfbfbf" if pd.isna(v) else "#2ca02c" if v >= 0.6 else "#ffbf00" if v >= 0.45 else "#d62728" for v in y]
    y_plot = tuple(0.05 if pd.isna(v) else v for v in y)
    hover = ["Geen data beschikbaar" if pd.isna(v) else f"Zekerheid: {v:.2f}" for v in y]

    fig = go.Figure(
        data=[go.Bar(x=list(x_labels), y=list(y_plot), marker_color=colors,
                     customdata=hover,
                     hovertemplate="<b>%{x}</b><br>%{customdata}<extra></extra>")]
    )
    fig.update_layout(
        xaxis_title=None, yaxis_title="Index", showlegend=False,
        margin=dict(l=40, r=5, t=20, b=60),
        xaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10, categoryorder="category ascending"),
        yaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
        height = CHART_HEIGHT
    )

    fig.update_yaxes(
        tickvals=[0.2, 0.5, 0.8],                     
        ticktext=["Laag", "Midden", "Hoog"],
        range=[0, 1], tickangle=-90
    )
    return fig

@st.cache_data(show_spinner=False)
def make_klantvraag_scatter_b2b(sel_hist_df: pd.DataFrame):
    
    fig = go.Figure()

    # add each line
    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Traditionele meubels']],
        mode='lines+markers',
        name='Traditionele meubels (CAGR 4,95%)',
        line=dict(color='black', width=3),
        marker=dict(size=6)
    ))

    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Duurzame meubels']],
        mode='lines+markers',
        name='Duurzame meubels (CAGR 10,1%)',
        line=dict(color='green', width=3),
        marker=dict(size=6)
    ))

    # layout tweaks
    fig.update_layout(
        xaxis_title="Jaar",
        yaxis_title="Index (2023 = 100)",
        template="plotly_white",
        margin=dict(l=40, r=15, t=20, b=70),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    return fig

@st.cache_data(show_spinner=False)
def make_klantvraag_scatter_b2c(sel_hist_df: pd.DataFrame):
    
    fig = go.Figure()

    # add each line
    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Traditionele meubels']],
        mode='lines+markers',
        name='Traditionele meubels (CAGR 4,95%)',
        line=dict(color='black', width=3),
        marker=dict(size=6)
    ))

    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Duurzame meubels']],
        mode='lines+markers',
        name='Duurzame meubels (CAGR 10,3%)',
        line=dict(color='green', width=3),
        marker=dict(size=6)
    ))

    # layout tweaks
    fig.update_layout(
        xaxis_title="Jaar",
        yaxis_title="Index (2023 = 100)",
        template="plotly_white",
        margin=dict(l=40, r=15, t=20, b=70),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )
    return fig

def make_klantvraag_overheid_plot():
    years = ss.klantvraag_overheid_df.years
    normale = ss.klantvraag_overheid_df.normale
    circulair = ss.klantvraag_overheid_df.circulair
    arrow_year = 2026
    # linear interpolation between 2020 (90) and 2030 (50)
    arrow_y = 90 + (50 - 90) * ((arrow_year - 2020) / 10)

    # Dense line for dashed boundary (piecewise linear)
    x_dense = list(range(2020, 2051))
    def normale_interp(x):
        if x <= 2030:
            return 90 + (50 - 90) * ((x - 2020) / 10)
        return 50 + (0 - 50) * ((x - 2030) / 20)
    normale_dense = [normale_interp(x) for x in x_dense]

    fig = go.Figure()

    # Stacked area: Normale + Circulaire
    fig.add_trace(go.Scatter(
        x=years,
        y=normale,
        stackgroup="one",
        name="Normale inkoop",
        mode="lines",
        line=dict(width=0.5),   # keep >0 for maximum compatibility
        fillcolor="#5A5A5A",
        hovertemplate="Jaar: %{x}<br>Normale inkoop: %{y:.0f}%<extra></extra>",
    ))

    fig.add_trace(go.Scatter(
        x=years,
        y=circulair,
        stackgroup="one",
        name="Circulaire inkoop",
        mode="lines",
        line=dict(width=0.5),
        fillcolor="#00B050",
        hovertemplate="Jaar: %{x}<br>Circulaire inkoop: %{y:.0f}%<extra></extra>",
    ))

    # Dashed boundary = top of 'normale'
    fig.add_trace(go.Scatter(
        x=x_dense,
        y=normale_dense,
        mode="lines",
        showlegend=False,
        line=dict(color="white", width=5, dash="dash"),
        hoverinfo="skip",
    ))

    # Arrow + label
    fig.add_annotation(
        x=arrow_year, y=arrow_y,
        ax=arrow_year, ay=0,
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.2,
        arrowwidth=3,
        arrowcolor="red",
        text="",
    )
    fig.add_annotation(
        x=arrow_year, y=0,
        xref="x", yref="y",
        showarrow=False,
        text="<b>2026</b>",
        font=dict(color="red"),
        yshift=-22
    )

    fig.update_layout(
        #title=dict(text="Publieke markt verschuift:<br>van lineair naar circulair", x=0.5),
        xaxis=dict(range=[2020, 2050], tickmode="array", tickvals=[2020, 2030, 2050], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, 100], ticksuffix="%", tick0=0, dtick=20, showgrid=False, zeroline=False),
        legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.18, yanchor="top"),
        margin=dict(l=40, r=15, t=5, b=60),
        plot_bgcolor="white",
        paper_bgcolor="white",
    )

    return fig

# ---------- Sidebar Filters ----------
with st.sidebar:
    st.header("Bedrijfsprofiel")
    widget_branche()
    widget_medewerkers()
    widget_omzet()
    widget_klantsegment()
    widget_klanttype()
    widget_materialen()

# ---------- Data (apply filters where appropriate) ----------
# NOTE: Hook your real filters into these calls (branche/fte/omzet/etc.).

# ---------- Tiles ----------

def tile_prijsstijgingen(target_page):
    st.subheader("Prijsontwikkelingen")
    st.write("De prijzen en prijsschommelingen van grondstoffen en materialen zijn de afgelopen 10 jaar toegenomen.")
    st.caption("Klik op een balk voor de achterliggende informatie en toelichting.")
    st.caption(" ")
    # --- build the bar chart (any way you like) ---
    x = tuple(ss.df_now_prijs["materiaal"].tolist())
    y_raw = (ss.df_now_prijs["risk2"] * 100).tolist()
    colors = ["#bfbfbf" if pd.isna(v) else "#2ca02c" if v <= 10 else "#ffbf00" if v <= 20 else "#d62728" for v in y_raw]
    y = tuple(5 if pd.isna(v) else v for v in y_raw)
    hover = ["Geen data beschikbaar" if pd.isna(v) else f"Stijging: {v:.1f}%" for v in y_raw]

    fig = go.Figure(
        go.Bar(
            x=x, y=y, marker_color=colors,
            customdata=hover,
            hovertemplate="<b>%{x}</b><br>%{customdata}<extra></extra>"
        )
    )
    fig.update_layout(height=CHART_HEIGHT, 
                      xaxis_title=None, 
                      yaxis_title="Prijsvariatie t.o.v. 2015 (%)", 
                      showlegend=False,
                      margin=dict(l=40, r=5, t=20, b=60),
                      xaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10, categoryorder="category ascending"),
                      yaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
)

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
            row = ss.df_now_prijs[ss.df_now_prijs['materiaal'] == mat]
            if not row.empty and not pd.isna(row.iloc[0]['risk2']):
                ss.selected_materiaal_value = mat
                log_event("Home", "bar_click_prijsstijgingen", mat)
                ss["_navigate_to"] = target_page
                st.rerun()
    st.caption('De balken tonen de veranderingen in de prijzen van de door u gekozen materialen. Dit kan een langdurige of kortstondige veranderingen zijn.')

def tile_leveringszekerheid(target_page):
    st.subheader("Leveringszekerheid")
    
    st.write("De leveringszekerheid van grondstoffen in de meubelindustrie afgenomen door geopolitieke spanningen en schaarste in aanbod op de markt.")
    st.caption("Klik op een balk om de wereldwijde grondstofspreiding en de onderbouwing van de risicoscore te zien volgens de World Governance Indicatoren.")
    st.caption(" ")

    x = tuple(ss.df_now_lev["material"].tolist())
    y = tuple(ss.df_now_lev["supply_risk"].tolist())
    fig = make_levzeker_bar_figure(x, y, COMMON_LAYOUT)  # cached

    fig.update_layout(yaxis_title="Stabiliteit van productielanden (WGI)")

    clicks = plotly_events(
        fig,
        click_event=True, hover_event=False, select_event=False,override_height=CHART_HEIGHT,
        key=f"evt_zeker_{ss.events_epoch}",
    )

    if clicks:
        mat = clicks[0].get("x")
        if mat:
            row = ss.df_now_lev[ss.df_now_lev['material'] == mat]
            if not row.empty and not pd.isna(row.iloc[0]['supply_risk']):
                ss.selected_materiaal_value = mat
                log_event("Home", "bar_click_leveringszekerheid", mat)
                ss["_navigate_to"] = target_page
                st.rerun()
    st.caption('De balken laten de stabiliteit van de belangrijkste productielanden zien.')

def tile_klantvraag_overheid(target_page: str):
    with st.container(border=False):
        st.subheader("Klantvraag")
        st.write("Publieke markt verschuift: van lineair naar circulair")
        #st.caption("Klik op een punt in de grafiek om meer te weten te komen over de ontwikkelingen in de klantvraag en andere marktontwikkelingen.")
        fig = make_klantvraag_overheid_plot()

        clicks = plotly_events(
            fig,
            click_event=True, hover_event=False, select_event=False,
            override_height=CHART_HEIGHT, override_width="100%",
            key=f"evt_klantvraag_onderwijs_{ss.events_epoch}"
        )
        if clicks:
            st.switch_page(target_page)
        if st.button("Bekijk informatie over klantvraag", width = 'stretch'):
            st.switch_page(target_page)
        #st.caption('De grafiek vergelijkt de verwachte groei van het meubelsegment gericht op kwaliteit, duurzaamheid en repareerbaarheid (groene lijn) met die van de totale markt (zwarte lijn).')

def tile_klantvraag_B(target_page: str):
    with st.container(border=False):
        st.subheader("Klantvraag")
        st.write("De vraag naar meubels met focus op kwaliteit, levensduur en repareerbaarheid groeit dubbel zo hard als de normale meubelmarkt.")
        #st.caption("Klik op een punt in de grafiek om meer te weten te komen over de ontwikkelingen in de klantvraag en andere marktontwikkelingen.")
        if ss.klanttype_value == 'B2C':
            fig = make_klantvraag_scatter_b2c(ss.klantvraag_df_b2c)
        elif ss.klanttype_value == 'B2B':
            fig = make_klantvraag_scatter_b2b(ss.klantvraag_df_b2b)
        fig.update_layout(**COMMON_LAYOUT,
            legend=dict(orientation="h", yanchor="bottom", y=-0.5, xanchor="center", x=0.5),
            )

        clicks = plotly_events(
            fig,
            click_event=True, hover_event=False, select_event=False,
            override_height=CHART_HEIGHT, override_width="110%",
            key=f"evt_klantvraag_{ss.events_epoch}"
        )
        if clicks:
            st.switch_page(target_page)
        if st.button("Bekijk informatie over klantvraag", width = 'stretch'):
            st.switch_page(target_page)
        #st.caption('De grafiek vergelijkt de verwachte groei van het meubelsegment gericht op kwaliteit, duurzaamheid en repareerbaarheid (groene lijn) met die van de totale markt (zwarte lijn).')

def tile_wetgeving(target_page: str):
    with st.container(border=False):
        st.subheader("Wet- en regelgeving")
        st.write("De wet- en regelgeving verandert voor de meubelbranche. De komende jaren gaan er strengere normen en eisen gesteld worden aan materiaal- en ontwerpkeuzes.")
        st.caption("Klik op de button onder de visual om meer te weten te komen over de ontwikkelingen in de Nederlandse en Europese wet- en regelgeving.")
        
    # --- Stijl voor de niet-klikbare knop ---
    st.markdown("""
    <style>
    .custom-tile {
        background-color: #f4f1e6;
        border: 2px solid #333;
        border-radius: 12px;
        padding: 30px;
        font-size: 20px;
        font-family: sans-serif;
        text-align: center;
        line-height: 1.6;
        width: 100%;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Niet-klikbare "knop" (eigenlijk gewoon een <div>) ---
    if (ss.omzet_value == ">€50M") | (ss.medewerkers_value == "250+ fte"):
        _iframe(generate_badge(9), height=170)
        _iframe(generate_badge2(12), height=160)
    else:
        _iframe(generate_badge(8), height=170)
        _iframe(generate_badge2(11), height=160)
    if st.button("Bekijk relevante wet- en regelgeving", width = 'stretch'):
        st.switch_page(target_page)

def tile_profilering(target_page):
    with st.container(border=False):
        st.subheader("Bedrijfsprofilering")
        st.write('Duurzame ambities zonder duidelijke positionering blijven onzichtbaar voor klanten, opdrachtgevers en medewerkers.')
        with st.container(border = True):
            st.image('assets/Tegel - profilering.png')
        if st.button("Bekijk informatie over bedrijfsprofilering", width = 'stretch'):
            st.switch_page(target_page)

def tile_subsidies(target_page):
    with st.container(border=False):
        st.subheader("Subsidies")
        st.write('Er wordt financiële ondersteuning geboden vanuit de Nederlandse overheid en de Europese Unie voor innovaties op gebied van materialen, ontwerp en processen.')
        with st.container(border = True):
            st.image('assets/Tegel - subsidies.png')
        if st.button("Bekijk informatie over subsidies", width = 'stretch'):
                st.switch_page(target_page)

# ---------- Layout: 3 tiles in one row ----------
st.title("FLIM-tool")
st.write("**''Wat betekenen jouw materiaalkeuzes van vandaag voor de kosten, risico’s en regelgeving van morgen?''**")
st.write("De Financial Linear Impact Tool (FLIM) maakt zichtbaar welke financiële risico’s én kansen samenhangen met het gebruik van grondstoffen en materialen in je bedrijf. Op basis van zes factoren laat de tool zien waar risico’s ontstaan én waar kansen liggen om slimmer met grondstoffen om te gaan. Stem met de filters links de analyse af op jouw bedrijf en belangrijkste materialen, en ontdek waar andere keuzes financieel voordeel kunnen opleveren.")
st.caption("Klik op de grafieken/visualisaties om verder te navigeren of details te openen.")

col1, col2, col3 = st.columns(3, gap="small", border = True)
with col1: tile_prijsstijgingen(target_page = "pages/01_Prijsstijgingen.py")
with col2: tile_leveringszekerheid(target_page = "pages/02_Leveringszekerheid.py")
with col3: tile_wetgeving(target_page = "pages/04_wet_regelgeving.py")
    
h1, h2, h3 = st.columns(3, gap="small", border = True)
with h1:
    if ss.klanttype_value == 'Overheid':
        tile_klantvraag_overheid(target_page="pages/03_Klantvraag_B.py")
    else: 
        tile_klantvraag_B(target_page = "pages/03_Klantvraag_B.py")
with h2:
    tile_profilering(target_page = "pages/05_profilering.py") 
with h3:
    tile_subsidies(target_page = "pages/06_subsidies.py")
