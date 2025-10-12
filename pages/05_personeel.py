import streamlit as st

st.set_page_config(page_title="Personeel", layout="wide")

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

st.title('Personeel')
st.page_link("Home.py", label="⬅ Terug naar Home")
