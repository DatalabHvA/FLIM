import streamlit as st

st.set_page_config(page_title="Financierseisen", layout="wide", initial_sidebar_state='collapsed')

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


st.title('Financierseisen')
st.page_link("Home.py", label="⬅ Terug naar Home")
st.write(st.session_state["bubble_label"])