# pages/02_Leveringszekerheid_Map.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import sys
sys.path.append("..")

from Home import get_levzeker
from widgets import *

ss = st.session_state 

st.markdown("""
    <style>
        /* Hide all sidebar navigation links */
        section[data-testid="stSidebar"] li {
            display: none !important;
        }
        
        /* Verminder padding bovenaan hoofdpagina */
        div.block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Leveringszekerheid • Wereldkaart", layout="wide")

st.title("Leveringszekerheid — Wereldkaart")

with st.sidebar:
    st.page_link("Home.py", label="⬅ Terug naar Home")

    st.header("Filters")
    widget_materiaal()

# Read selected materiaal from query params (or fallback)

st.caption(f"Gefilterd op materiaal: **{ss.selected_materiaal_value}**")

st.markdown("""
    Leveringszekerheid laat de betrouwbaarheid van beschikbaarheid van de geselecteerde materialen zien. Dit wordt getoond aan de hand van de volgende twee indicatoren:
                """)


# Demo data — replace with your real geo/materials feed
df = ss.geo_df.merge(ss.wgi_df, on = 'ISO').loc[lambda d: d.material == ss.selected_materiaal_value][['ISO','country','governance_score', 'market_share']]
hhi = ss.geo_df.groupby('material').apply(lambda g: (g['market_share']**2).sum()).rename('hhi')
hhi_kpi = hhi.reset_index().loc[lambda d: d.material == ss.selected_materiaal_value].iloc[0]['hhi']

df_now = get_levzeker(tuple([ss.selected_materiaal_value]))
wgi_kpi = df_now.iloc[0]['supply_risk']

c1, c2 = st.columns(2)

with c1:
    with st.container(border = True, horizontal_alignment = 'center'):
        st.metric("Herfindahl–Hirschman index (HHI)", f"{hhi_kpi:.2f}")
        st.write('De HHI geeft de mate van geconcentreerdheid aan van de oorsprong van een grondstof (0 is zeer verspreid, 1 is volledig monopolie). Als deze indicator hoog is betekent het dat een enkele verstoring grote gevolgen kan hebben voor de leveringszekerheid.')
with c2:
    with st.container(border = True, horizontal_alignment = 'center'):
        st.metric("Gemiddelde World Governance Indicactor (WGI) voor productielanden van deze grondstof", f"{wgi_kpi:.2f}")
        st.write('De WGI geeft aan hoe stabiel het bestuur en de instituties van een land zijn. Deze maat wordt door de Europese Unie gebruikt om het risico op problemen bij de productie en levering van grondstoffen te meten.')

st.markdown("""
    Onderstaande kaart toont de herkomst en leveringszekerheid van het geselecteerde materiaal wereldwijd.
    De kleuren geven aan hoe stabiel en betrouwbaar de productie per land is: 
    groen = hoge zekerheid, rood = lage zekerheid).
            """)


fig = px.choropleth(
    df, locations="ISO", color="governance_score",
    color_continuous_scale=["#d62728", "#ffbf00", "#2ca02c"],  # red→yellow→green
    range_color=(0, 1), projection="natural earth",
    hover_name="country", hover_data={'ISO':False, "market_share" : ':.2f', "governance_score" : ':.2f'}
)
fig.update_layout(
    height=600, margin=dict(l=10, r=10, t=30, b=10),
    coloraxis_colorbar=dict(title="Zekerheid")
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
    **Herfindahl–Hirschman Index (HHI)**
            
    De HHI is een maatstaf voor marktconcentratie en heeft daarmee indirecte gevolgen voor leveringszekerheid. 
    - Bij een lage HHI  is de markt competitief met veel aanbieders van het geselecteerde materiaal.  Een lage HHI wijst op meer concurrentie en spreiding, wat doorgaans gunstig is voor leveringszekerheid.
    - Bij een hoge HHI is er sprake van een sterk geconcentreerde markt met weinig aanbieders. De markt is in dat geval kwetsbaar voor storingen of geopolitieke risico’s; één speler kan de markt domineren. (bron: investopedia.com)

    **Worldwide Governance Indicators (WGI)**
            
    Leveringszekerheid van grondstoffen hangt sterk af van governance van een land waar materialen vandaan komen. De WGI wordt door de Europese Unie gebruikt om het risico op problemen bij de productie en levering van grondstoffen te meten (bron: worldbank.org). 
    In de WGI zijn onder andere de volgende dimensies meegenomen die invloed hebben op leveringszekerheid van de geselecteerde materialen:
    - **Betrouwbaarheid** van **overheidsdiensten** en **consistente beleidsuitvoering**: deze  verminderen risico’s op verstoringen in levering. 
    - Een **sterke rechtsstaat** zorgt voor contracthandhaving en eigendomsrechten: dit is cruciaal voor stabiele toeleveringsketens. 
    - **Politieke stabiliteit**: minder kans op conflicten of politieke crises die leveringen kunnen onderbreken.
            """)
