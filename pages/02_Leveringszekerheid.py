import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import sys
sys.path.append("..")

from widgets import *

st.set_page_config(page_title="Leveringszekerheid • Wereldkaart", layout="wide")

ss = st.session_state
init_session_state()
log_event("Leveringszekerheid", "page_load")

st.markdown(
    """
    <style>
      .block-container { padding-top: 0.9rem !important; }
      header[data-testid="stHeader"] { height: 1.2rem; }
      [data-testid="stSidebarNav"] {display: none;}
      [data-testid="stSidebar"] .block-container { padding-top: 0 !important; }
      section[data-testid="stSidebar"] .block-container > div:first-child,
      section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child {
          margin-top: -60px !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Leveringszekerheid")

with st.sidebar:
    st.page_link("Home.py", label="⬅ Terug naar Home")
    st.header("Filters")
    widget_materiaal_lev()

st.caption(f"Gefilterd op materiaal: **{ss.selected_materiaal_value}**")

st.markdown(
    "Leveringszekerheid geeft aan hoe **betrouwbaar** en **stabiel** de aanvoer van een materiaal is. "
    "De kaart en indicatoren zijn gebaseerd op de landen die dit materiaal naar **Nederland exporteren** (op basis van UN Comtrade-data). "
    "Twee indicatoren bepalen samen het risico: de **concentratie van exportlanden (HHI)** en de **bestuurlijke stabiliteit van die landen (WGI)**."
)

# --- Data ---
df = (
    ss.geo_df
    .merge(ss.wgi_df, on="ISO")
    .loc[lambda d: d.material == ss.selected_materiaal_value][["ISO", "country", "governance_score", "market_share"]]
)
hhi = ss.geo_df.groupby("material").apply(lambda g: (g["market_share"] ** 2).sum()).rename("hhi")
hhi_kpi = hhi.reset_index().loc[lambda d: d.material == ss.selected_materiaal_value].iloc[0]["hhi"]

df_now = get_levzeker(tuple([ss.selected_materiaal_value]))
wgi_kpi = df_now.iloc[0]["supply_risk"]

# --- KPI tiles ---
CARD_STYLE = "flex:1; border:1px solid rgba(49,51,63,0.2); border-radius:0.5rem; padding:1.2rem 1.4rem;"
LABEL_STYLE = "font-size:0.85rem; color:#666; margin-bottom:0.2rem;"
VALUE_STYLE = "font-size:2rem; font-weight:700; margin-bottom:0.8rem;"

st.markdown(f"""
<div style="display:flex; gap:1rem; align-items:stretch; margin-bottom:1rem;">
  <div style="{CARD_STYLE}">
    <div style="{LABEL_STYLE}">Herfindahl–Hirschman Index (HHI)</div>
    <div style="{VALUE_STYLE}">{hhi_kpi:.2f}</div>
    <p style="margin:0 0 0.5rem 0;">Meet de <strong>concentratie van exportlanden naar Nederland</strong> (schaal 0–1).</p>
    <ul style="margin:0; padding-left:1.2rem;">
      <li><strong>Laag (→ 0):</strong> veel landen exporteren dit materiaal naar Nederland — de aanvoer is gespreid en minder kwetsbaar.</li>
      <li><strong>Hoog (→ 1):</strong> één of enkele landen domineren de export — een storing of geopolitiek conflict bij dat land heeft direct grote gevolgen.</li>
    </ul>
  </div>
  <div style="{CARD_STYLE}">
    <div style="{LABEL_STYLE}">Gemiddelde World Governance Indicator (WGI)</div>
    <div style="{VALUE_STYLE}">{wgi_kpi:.2f}</div>
    <p style="margin:0 0 0.5rem 0;">Meet de <strong>bestuurlijke stabiliteit</strong> van de exportlanden naar Nederland (schaal 0–1).</p>
    <ul style="margin:0; padding-left:1.2rem;">
      <li><strong>Hoog (→ 1):</strong> exportlanden hebben betrouwbare overheden, sterke rechtsstaat en politieke stabiliteit — levering is goed gewaarborgd.</li>
      <li><strong>Laag (→ 0):</strong> exportlanden zijn politiek instabiel of hebben zwakke instituties — hogere kans op verstoringen in de toeleveringsketen.</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

# --- Background info ---
with st.expander("Meer uitleg over HHI en WGI"):
    st.markdown(
        """
        **Herfindahl–Hirschman Index (HHI)**

        De HHI berekent de som van de gekwadrateerde exportaandelen van alle landen die dit materiaal naar Nederland leveren.
        Een waarde dichtbij **0** betekent een gespreide aanvoer met veel exportlanden; een waarde dichtbij **1** wijst op een (bijna-)monopolie.
        Een hoge HHI maakt de toeleveringsketen kwetsbaar voor geopolitieke risico's of verstoringen bij één speler. *(bron: investopedia.com)*

        **Worldwide Governance Indicators (WGI)**

        De WGI van de Wereldbank meet zes dimensies van bestuurskwaliteit: betrouwbaarheid van overheidsdiensten,
        consistente beleidsuitvoering, rechtsstaat, eigendomsrechten, politieke stabiliteit en corruptiebeheersing.
        De Europese Unie gebruikt de WGI om leveringsrisico's van kritieke grondstoffen te beoordelen. *(bron: worldbank.org)*
        """
    )

# --- Map ---
st.markdown(
    "De kaart toont de landen die dit materiaal naar **Nederland exporteren**, ingekleurd op **bestuurlijke stabiliteit** (WGI-score): "
    "**groen** = hoge zekerheid, **rood** = lage zekerheid."
)

fig = px.choropleth(
    df, locations="ISO", color="governance_score",
    color_continuous_scale=["#d62728", "#ffbf00", "#2ca02c"],
    range_color=(0, 1), projection="natural earth",
    hover_name="country",
    hover_data={"ISO": False, "market_share": ":.2f", "governance_score": ":.2f"},
    labels={"market_share": "Aandeel export naar NL", "governance_score": "WGI-score"},
)
fig.update_layout(
    height=600, margin=dict(l=10, r=10, t=30, b=10),
    coloraxis_colorbar=dict(title="Zekerheid"),
)
st.plotly_chart(fig, width='stretch')

st.caption("Bron exportdata: UN Comtrade. Marktaandelen zijn berekend op basis van exportwaarde naar Nederland.")
