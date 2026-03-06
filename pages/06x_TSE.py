import streamlit as st
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="TSE", layout="wide")
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

st.title('TSE Industrie - Studies')
st.subheader('*Topsector Energie Industrie - Studies*')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")

rows = [["Verkenning", "€25K-€4M",  "Individueel óf<br>samenwerking" ]]

html = generate_table(rows)
st.markdown(html, unsafe_allow_html=True)

