# pages/02_Leveringszekerheid_Map.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

ss = st.session_state 

st.set_page_config(page_title="Leveringszekerheid • Wereldkaart", layout="wide")

hide_sidebar = """
    <style>
        /* Hide sidebar completely */
        [data-testid="stSidebar"] {
            display: none !important;
        }
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        [data-testid="collapsedControl"] {
            display: none !important;
        }

        /* Reduce top padding/margin of main container */
        .main > div {
            padding-top: 0rem !important;
        }

        /* Reduce top padding on container blocks */
        .block-container {
            padding-top: 1.0rem !important;
        }

        /* Optional: reduce title block spacing if used */
        h1, h2, h3 {
            margin-top: 0.2rem;
        }
    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.title("Leveringszekerheid — Wereldkaart")
st.page_link("Home.py", label="⬅ Terug naar Home")

# Read selected materiaal from query params (or fallback)

st.caption(f"Gefilterd op materiaal: **{ss.selected_material_geo}**")

# Demo data — replace with your real geo/materials feed
df = ss.geo_df.merge(ss.wgi_df, on = 'country').loc[lambda d: d.material == ss.selected_material_geo][['iso3','country','governance_score', 'market_share']]
hhi = ss.geo_df.groupby('material').apply(lambda g: (g['market_share']**2).sum()).rename('hhi')
hhi_kpi = hhi.reset_index().loc[lambda d: d.material == ss.selected_material_geo].iloc[0]['hhi']

with st.container(border = True, horizontal_alignment = 'center'):
    st.metric("Herfindahl–Hirschman index (mate van geconcentreerdheid - 0, is zeer verspreid, 1 is volledig monopolie)", f"{hhi_kpi:.2f}")


fig = px.choropleth(
    df, locations="iso3", color="governance_score",
    color_continuous_scale=["#d62728", "#ffbf00", "#2ca02c"],  # red→yellow→green
    range_color=(0, 1), projection="natural earth",
    hover_name="country", hover_data={'iso3':False, "market_share" : ':.2f', "governance_score" : ':.2f'}
)
fig.update_layout(
    height=600, margin=dict(l=10, r=10, t=30, b=10),
    coloraxis_colorbar=dict(title="Zekerheid")
)
st.plotly_chart(fig, use_container_width=True)
