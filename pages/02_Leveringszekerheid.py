# pages/02_Leveringszekerheid_Map.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

ss = st.session_state 

st.set_page_config(page_title="Leveringszekerheid • Wereldkaart", layout="wide")

hide_sidebar = """
    <style>
        [data-testid="stSidebar"] {
            display: none !important;
        }
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        [data-testid="collapsedControl"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.title("Leveringszekerheid — Wereldkaart")
st.page_link("Home.py", label="⬅ Terug naar Home")

# Read selected materiaal from query params (or fallback)

st.caption(f"Gefilterd op materiaal: **{ss.selected_material_geo}**")

# Demo data — replace with your real geo/materials feed
rng = np.random.default_rng(2)
countries = ["NLD", "BEL", "DEU", "FRA", "ESP", "ITA", "SWE", "POL", "USA", "CHN", "IND", "BRA", "ZAF"]
df = pd.DataFrame({
    "iso3": countries,
    "zekerheid": rng.uniform(10, 95, size=len(countries)).round(1),
})

fig = px.choropleth(
    df, locations="iso3", color="zekerheid",
    color_continuous_scale=["#d62728", "#ffbf00", "#2ca02c"],  # red→yellow→green
    range_color=(0, 100), projection="natural earth",
)
fig.update_layout(
    height=600, margin=dict(l=10, r=10, t=30, b=10),
    coloraxis_colorbar=dict(title="Zekerheid")
)
st.plotly_chart(fig, use_container_width=True)
