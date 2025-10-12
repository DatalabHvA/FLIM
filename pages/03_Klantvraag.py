# pages/03_Klantvraag_Bars.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import sys
sys.path.append("..")

from Home import make_klantvraag_scatter

st.set_page_config(page_title="Klantvraag • Analyse", layout="wide")

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

st.title("Klantvraag — Analyse")
st.page_link("Home.py", label="⬅ Terug naar Home")

st.write("Belangrijke risico's en kansen in de markt")

klantvraag_df = pd.DataFrame({'Jaar' : [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
                              'Duurzame meubels (CAGR 2,8%)' : [100.0,102.8,105.7,108.6,111.7,114.8,118.0,121.3],
                              'Traditionele meubels (CAGR 7,3%)' : [100.0,107.3,115.1,123.5,132.6,142.2,152.6,163.8]})

c1, c2 = st.columns(2)
with c1: 
    pie = go.Pie(labels=['Duurzame meubels', 'Traditionele meubels'], 
                 values=[0.13, 0.87], name='Meubelmarkt in 2030')
    fig = go.Figure(data=[pie])
    fig.update_layout(
        title='Meubelmarkt in 2030',
        legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.1),
        margin=dict(t=40, b=40, l=40, r=40),
    )
    st.plotly_chart(fig)
    st.write('Toont risico’s van het niet inspelen op duurzaamheid. Een significant deel van de markt verwacht duurzame alternatieven. Gebrek aan actie leidt tot afname van klanttevredenheid en marktaandeel.')

with c2:
    fig = make_klantvraag_scatter(klantvraag_df)
    fig.update_layout(
        title='Verglijking marktgroei: normale vs duurzame markt',
        legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.2),
        margin=dict(t=40, b=40, l=40, r=40),
    )
    st.plotly_chart(fig)
    st.write('Laat de sterke stijging zien van de vraag naar duurzame producten. Groeitempo is meer dan 2x sneller dan traditionele productcategorieën. Duidelijke marktkans om te benutten/nu in te stappen.')

