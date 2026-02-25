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

from widgets import *

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
    df1 = pd.read_excel('data/Analyse factoren.xlsx', sheet_name='Data per factor (incl kwal)')
    df1['Factor'] = df1['Factor'].ffill()
    df1 = df1.loc[lambda d: d.Factor == 'Prijsstijgingen']
    targets = set(df1.loc[df1['Data gebruikt'] == 'Ja']['ID'].dropna().unique().astype(int).astype(str))
    targets.add('ID')
    prijzen_indices = pd.read_excel('data/prijzen.xlsx').columns
    prijzen_indices = pd.Series(prijzen_indices).apply(lambda x: str(x).split('.')[0])
    indices = [i for i, x in enumerate(prijzen_indices) if str(x) in targets]
    ss.prijzen_df = pd.read_excel('data/prijzen.xlsx', skiprows = 1).iloc[:,indices]
    ss.prijzen_df.columns = pd.Series(ss.prijzen_df.columns).apply(lambda x: x.split('.')[0])
if 'geo_df' not in ss:
    #df1 = pd.read_excel('data/Analyse factoren.xlsx', sheet_name='factor_productielanden')
    #targets = set(df1.loc[df1['Opgenomen in Webapp'] == 'Ja']['id'].dropna().unique())
    #ss.geo_df = pd.read_excel('data/material_market_share.xlsx').loc[lambda d: d['id'].isin(targets)].drop('id', axis = 1)
    ss.geo_df = pd.read_excel('data/material_market_share.xlsx').loc[lambda d: d.market_share > 0.03]
if 'wgi_df' not in ss:
    ss.wgi_df = pd.read_excel('data/wgi_governance_scores_2023_with_iso3.xlsx')
if 'klantvraag_df' not in ss:
    ss.klantvraag_df = pd.DataFrame({'Jaar' : [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
                              'Traditionele meubels (CAGR 2,8%)' : [100.0,102.8,105.7,108.6,111.7,114.8,118.0,121.3],
                              'Duurzame meubels (CAGR 7,3%)' : [100.0,107.3,115.1,123.5,132.6,142.2,152.6,163.8]})
if 'klantvraag_overheid_df' not in ss:
    ss.klantvraag_overheid_df = pd.DataFrame({'years' : [2020, 2030, 2050],
                              'normale' : [90, 50, 0],
                              'circulair' : [10, 50, 100]})
if 'personeel_df' not in ss:
    ss.personeel_df = pd.DataFrame({'Categorie' : ['Global Gen Z', 'Global millennials', 'Nederlandse Gen Z', 'Nederlands millennials'],
                                    'Opdracht_project' : [0.5, 0.43, 0.41, 0.31],
                                    'Werkgever' : [0.44, 0.4, 0.36, 0.29]})

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

# --- Figure builders (cached) ---

@st.cache_data(show_spinner=False)
def make_levzeker_bar_figure(x_labels: tuple, y: tuple, C_LAYOUT):
    colors = colors = ["#2ca02c" if v >= 0.6 else "#ffbf00" if v >= 0.45 else "#d62728" for v in y]

    fig = go.Figure(
        data=[go.Bar(x=list(x_labels), y=list(y), marker_color=colors,
                     hovertemplate="<b>%{x}</b><br>Zekerheid: %{y:.1f}<extra></extra>")]
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
def make_klantvraag_scatter(sel_hist_df: pd.DataFrame):
    
    fig = go.Figure()

    # add each line
    fig.add_trace(go.Scatter(
        x=[str(x) for x in ss.klantvraag_df['Jaar']],
        y=[float(x) for x in ss.klantvraag_df['Traditionele meubels (CAGR 2,8%)']],
        mode='lines+markers',
        name='Traditionele meubels (CAGR 2,8%)',
        line=dict(color='black', width=3),
        marker=dict(size=6)
    ))

    fig.add_trace(go.Scatter(
        x=[str(x) for x in ss.klantvraag_df['Jaar']],
        y=[float(x) for x in ss.klantvraag_df['Duurzame meubels (CAGR 7,3%)']],
        mode='lines+markers',
        name='Duurzame meubels (CAGR 7,3%)',
        line=dict(color='green', width=3),
        marker=dict(size=6)
    ))

    # layout tweaks
    fig.update_layout(
        xaxis_title="Jaar",
        yaxis_title="Index (2023 = 100)",
        template="plotly_white",
        margin=dict(l=40, r=5, t=20, b=70),
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
    st.header("Filters")
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
    st.write("De prijsvariatie van deze belangrijke grondstoffen is de afgelopen 10 jaar het meest toegenomen.")
    st.caption("Klik op een balk voor de achterliggende grafiek en toelichting.")
    st.caption(" ")
    # --- build the bar chart (any way you like) ---
    x = tuple(ss.df_now_prijs["materiaal"].tolist())
    y = tuple((ss.df_now_prijs["risk2"]*100).tolist())
    
    colors = ["#2ca02c" if v <= 10 else "#ffbf00" if v <= 20 else "#d62728" for v in y]

    fig = go.Figure(
        go.Bar(
            x=x, y=y, marker_color=colors,
            hovertemplate="<b>%{x}</b><br>Stijging: %{y:.1f}%<extra></extra>"
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
            ss.selected_materiaal_value = mat
            st.switch_page(target_page)
    st.caption('De balken tonen de variatie in de prijs. Dit kan een stijging of een fluctuatie zijn.')

def tile_leveringszekerheid(target_page):
    st.subheader("Leveringszekerheid")
    
    st.write("De leveringszekerheid van belangrijkste grondstoffen in de meubelindustrie afgenomen door geopolitieke spanningen.")
    st.caption("Klik op een balk om de globale grondstofspreiding en de onderbouwing van de risicoscore te zien.")
    st.caption(" ")

    x = tuple(ss.df_now_lev["material"].tolist())
    y = tuple(ss.df_now_lev["supply_risk"].tolist())
    fig = make_levzeker_bar_figure(x, y, COMMON_LAYOUT)  # cached

    fig.update_layout(yaxis_title="Stabiliteit van productielanden")

    clicks = plotly_events(
        fig,
        click_event=True, hover_event=False, select_event=False,override_height=CHART_HEIGHT,
        key=f"evt_zeker_{ss.events_epoch}",
    )

    if clicks:
        mat = clicks[0].get("x")
        if mat:
            ss.selected_materiaal_value = mat
            st.switch_page(target_page)
    st.caption('De balken laten de stabiliteit van de belangrijkste productielanden zien volgens de World Governance Indicatoren.')

def tile_klantvraag_overheid(df, target_page: str):
    with st.container(border=False):
        st.subheader("Klantvraag")
        st.write("Publieke markt verschuift: van lineair naar circulair")
        st.caption("Klik op een punt in de grafiek om meer te weten te komen over de ontwikkelingen in de klantvraag en andere marktontwikkelingen.")
        fig = make_klantvraag_overheid_plot()

        clicks = plotly_events(
            fig,
            click_event=True, hover_event=False, select_event=False,
            override_height=CHART_HEIGHT, override_width="100%",
            key=f"evt_klantvraag_onderwijs_{ss.events_epoch}"
        )
        if clicks:
            st.switch_page(target_page)
        #st.caption('De grafiek vergelijkt de verwachte groei van het meubelsegment gericht op kwaliteit, duurzaamheid en repareerbaarheid (groene lijn) met die van de totale markt (zwarte lijn).')

def tile_klantvraag_B(df, target_page: str):
    with st.container(border=False):
        st.subheader("Klantvraag")
        st.write("De vraag naar meubels met focus op kwaliteit, levensduur en repareerbaarheid groeit dubbel zo hard als de normale meubelmarkt.")
        st.caption("Klik op een punt in de grafiek om meer te weten te komen over de ontwikkelingen in de klantvraag en andere marktontwikkelingen.")
        fig = make_klantvraag_scatter(df)
        fig.update_layout(**COMMON_LAYOUT,
            legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5),
            )

        clicks = plotly_events(
            fig,
            click_event=True, hover_event=False, select_event=False,
            override_height=CHART_HEIGHT, override_width="110%",
            key=f"evt_klantvraag_{ss.events_epoch}"
        )
        if clicks:
            st.page_link(target_page)
        st.caption('De grafiek vergelijkt de verwachte groei van het meubelsegment gericht op kwaliteit, duurzaamheid en repareerbaarheid (groene lijn) met die van de totale markt (zwarte lijn).')

def tile_wetgeving(target_page: str):
    with st.container(border=False):
        st.subheader("Wet- en regelgeving")
        st.write("Binnen 5 jaar gelden strengere normen op materiaalkeuze en ontwerp binnen de meubelbranche.")
        
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
    st.markdown("""
    <div class="custom-tile">
        Er zijn:<br><b>        <span style="font-size: 48px; font-weight: bold;">5</span></b><br>wet- en regelgevingen<br>die voor jouw bedrijf<br>van toepassing zijn
    </div>
    """, unsafe_allow_html=True)

    if st.button("Bekijk relevante wet- en regelgeving", width = 'stretch'):
        st.switch_page(target_page)

def tile_profilering(target_page):
    with st.container(border=False):
        st.subheader("Bedrijfsprofilering")
        st.write('Duurzame ambities zonder duidelijke positionering blijven onzichtbaar voor klanten, opdrachtgevers en medewerkers.')
        st.caption('Klik op onderstaand blok om te leren wat jij kunt doen.')

        with st.container():
            # Define categories and values
            #topics = ['Opdracht', 'Werkgever']
            topics = ['Werkgever']

            # Values per group per topic
            # values = {
            #     "Global Gen Z": [50, 44],
            #     "Global millennials": [43, 40],
            #     "Nederlandse Gen Z": [41, 36],
            #     "Nederlandse millennials": [31, 29]
            # }
            values = {
                #"Global Gen Z": [44],
                #"Global millennials": [40],
                "Nederlandse Gen Z": [36],
                "Nederlandse millennials": [29]
            }

            # Define consistent colors
            colors = {
                #"Global Gen Z": "#009CA6",         # Teal
                #"Global millennials": "#5B5B5B",   # Dark grey
                "Nederlandse Gen Z": "#00726B",    # Dark teal
                "Nederlandse millennials": "#BFBFBF"  # Light grey
            }

            # Build figure
            fig = go.Figure()

            for label, vals in values.items():
                fig.add_trace(go.Bar(
                    x=topics,
                    y=vals,
                    name=label,
                    text=[f"{v}%" for v in vals],
                    textposition="outside",
                    marker_color=colors[label]
                ))
            fig.update_yaxes(range=[0, 36 * 1.2])  # 20% extra headroom
            # Layout settings
            fig.update_layout(
                barmode="group",
                xaxis_title="",
                yaxis_title="Percentage",
                template="plotly_white",
                height=CHART_HEIGHT,
                legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
                **COMMON_LAYOUT
            )

            clicks = plotly_events(
                fig,
                click_event=True, hover_event=False, select_event=False,
                override_height = CHART_HEIGHT,
                key=f"evt_personeel_{ss.events_epoch}",
            )
            if clicks:
                # For Heatmap, Plotly returns y = row label (our 'label')
                st.switch_page(target_page)

        st.caption("Percentage van respondenten die een opdracht of een potentiele werkgever hebben afgewezen op basis van hun persoonlijk ethiek/overtuigingen.")

def tile_subsidies():
    st.subheader("Financiers")
    st.write('De overheid biedt financiële ondersteuning voor innovaties in materiaal, ontwerp en proces.')
    st.caption("Klik op de (ondersteepte) subsidies om meer te weten te komen.")
    cols = st.columns([1, 2, 1, 1, 2, 1])
    with cols[1]:
        st.image("https://upload.wikimedia.org/wikipedia/commons/2/20/Flag_of_the_Netherlands.svg", width = 'stretch')
    with cols[4]: 
        st.image("https://upload.wikimedia.org/wikipedia/commons/b/b7/Flag_of_Europe.svg", width = 'stretch')

    # Sample content and row colors
    labels = ['<b> Verkenning</b>', 'TSE Industrie - studies', '<a href="/a_MIT_haalbaarheid", target = "_self"<u>MIT - Haalbaarheid</u></a>', '','<b>Ontwikkeling</b>', 'MIT - R&D samenwerking', 'DEI+ - Circulaire Economie', 'VEKI - Versnelde Klimaatinvesteringen', '<b>Implementatie</b>', 'MIA\Vamil', 'CKP - Circulaire Ketenprojecten', '', '<b>Opschaling</b>', 'EFRO (Regionaal)', ' ', '']
    values = ['', 'Horizon Europe - Cluster 4', 'EIR RawMaterials - Innovation Program', 'Life Programme - Circulair Economy', '', 'Horizon Europe - Cluster 5', 'Interreg - Circular Economy & Green Growth', 'COST Action - Circular Economy Innovation', '', 'Horizon Europe - EIC Accelerator', '<a href="/b_EDFR", target = "_self"<u>ERDF - Circular Economy</u></a>', 'Life Programme',' ','Horizon Europe - Cluster 6', 'EIC Fund', 'Horizon Europe - European Green Deal']
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
st.title("FLIM-tool")
st.caption("Klik op de grafieken/visualisaties om verder te navigeren of details te openen.")

col1, col2, col3 = st.columns(3, gap="small", border = True)
with col1: tile_prijsstijgingen(target_page = "pages/01_Prijsstijgingen.py")
with col2: tile_leveringszekerheid(target_page = "pages/02_Leveringszekerheid.py")
with col3: 
    if ss.klanttype_value == 'Overheid':
        tile_klantvraag_overheid(ss.klantvraag_overheid_df, target_page="pages/03_Klantvraag_overheid.py")
    else: 
        tile_klantvraag_B(ss.klantvraag_df, target_page = "pages/03_Klantvraag_B.py")

    
h1, h2, h3 = st.columns(3, gap="small", border = True)
with h1:
    tile_wetgeving(target_page = "pages/04_wet_regelgeving.py")
with h2:
    tile_profilering(target_page = "pages/05_profilering.py") 
with h3:
    tile_subsidies()
