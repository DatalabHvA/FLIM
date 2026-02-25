# pages/03_Klantvraag_Bars.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import sys
sys.path.append("..")

from Home import make_klantvraag_scatter

ss = st.session_state

st.set_page_config(page_title="Klantvraag B2B/B2C • Analyse", layout="wide")
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

with st.sidebar:
    st.page_link("Home.py", label="⬅ Terug naar Home")

    st.header("Filters")
    
    options_klantsegment =  ["Laag", "Midden", "Hoog"]
    st.selectbox("Klantsegment", options_klantsegment, key = 'klantsegment')
    options_klanttype = ["B2C", "B2B", "Overheid"]
    st.selectbox("Klanttype", options_klanttype, key = 'klanttype')
    
st.title("Klantvraag — Analyse")

klantvraag_df = pd.DataFrame({'Jaar' : [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
                              'Duurzame meubels (CAGR 2,8%)' : [100.0,102.8,105.7,108.6,111.7,114.8,118.0,121.3],
                              'Traditionele meubels (CAGR 7,3%)' : [100.0,107.3,115.1,123.5,132.6,142.2,152.6,163.8]})

c1, c2 = st.columns(2)
with c1: 
    with st.container(border = True):
        st.subheader("1. Risico's (in de markt)")

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
    with st.container(border = True):
        st.subheader('2. Kansen (in de markt)')
        fig = make_klantvraag_scatter(klantvraag_df)
        fig.update_layout(
            title='Verglijking marktgroei: normale vs duurzame markt',
            legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.2),
            margin=dict(t=40, b=40, l=40, r=40),
        )
        st.plotly_chart(fig)
        st.write('Laat de sterke stijging zien van de vraag naar duurzame producten. Groeitempo is meer dan 2x sneller dan traditionele productcategorieën. Duidelijke marktkans om te benutten/nu in te stappen.')

with st.container(border = True):
    st.subheader('3. Klantwens vs afzet')
    # Gegevens
    # Data
    categorieën = [
        "Staat open voor gerecycled",
        "Koopt gerecycled",
        "Staat open voor refurbished",
        "Koopt refurbished",
        "Staat open voor tweedehands",
        "Koopt tweedehands"
    ]
    waarden = [77, 16, 68, 5, 53, 13]
    types = ["Intentie", "Actie"] * 3

    # DataFrame met naam data3
    data3 = pd.DataFrame({
        "Categorie": categorieën,
        "Waarde": waarden,
        "Type": types
    })

    # Kleurinstellingen
    kleuren = {"Intentie": "steelblue", "Actie": "sandybrown"}

    # Figuur maken
    fig = go.Figure()

    fig.add_trace(go.Bar(
        y=data3["Categorie"],
        x=data3["Waarde"],
        orientation='h',
        marker_color=[kleuren[t] for t in data3["Type"]],
        text=[f"{v}%" for v in data3["Waarde"]],
        textposition="outside",
        hovertext=data3["Type"],
        showlegend=False
    ))

    # Layout
    fig.update_layout(
        title="Trechter: van intentie naar realiteit bij duurzame meubelaankopen",
        xaxis_title="Percentage (%)",
        yaxis_title="",
        barmode="overlay",
        template="plotly_white",
        height=500,
        margin=dict(l=220, r=40, t=80, b=40),
    )

    fig.update_yaxes(
        autorange="reversed",
        categoryorder="array",
        categoryarray=categorieën
    )
    st.plotly_chart(fig)

    st.write('Deze vergelijking tussen wat klanten willen (hoge voorkeur voor duurzame producten) en wat daadwerkelijk wordt verkocht toont een mismatch. Klanten willen duurzamer, maar het vertaalt zich niet in verkoopcijfers. Komt dit omdat het huidige aanbod hier nog niet voldoende aansluit of gemakkelijk genoeg beschikbaar is? Conclusie: ruim 40-50% van de duurzame vraag naar meubels blijft onvervuld.')

with st.container(border = True):
    st.subheader('4. Prijsperceptie en -acceptatie')

    # Data
    categories = ['Niet bereid', '5% premium', '10% premium', '>10% premium']
    values = [31, 25, 30, 14]
    colors = ['#E74C3C', '#E67E22', '#F1C40F', '#27AE60']  # red, orange, yellow, green

    # Cumulative values for text positioning
    cumulative = [sum(values[:i+1]) for i in range(len(values))]

    # Build the figure
    fig = go.Figure()

    for i, (category, value, color) in enumerate(zip(categories, values, colors)):
        fig.add_trace(go.Bar(
            y=["Consumenten"],
            x=[value],
            name=f"{value}% van respondenten",
            orientation='h',
            marker=dict(color=color),
            text=category,
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(color="black", size=14),
            hovertemplate=f"{category}<br>{value}% van respondenten<extra></extra>"
        ))

    # Layout
    fig.update_layout(
        barmode='stack',
        title='Bereidheid Duitse consumenten om meer te betalen voor duurzame producten',
        xaxis_title='Percentage respondenten',
        yaxis_title='',
        xaxis=dict(range=[0, 100]),
        template='plotly_white',
        height=400,
        legend_title="Verdeling",
    )

    # Optional: to center label text better
    fig.update_traces(textfont_size=14, cliponaxis=False)

    st.plotly_chart(fig)

    st.write('Toont bereidheid van klanten (in dit geval Duitse consumenten) om een meerprijs te betalen voor duurzaamheid. Meer dan de helft is bereid 10-20% extra te betalen. Dit opent mogelijkheden voor premium positionering.')

with st.container(border = True):
    st.subheader('5. Voorbeelden uit de praktijk')
    st.markdown('''
    | Bedrijfsnaam| Korte beschrijving | 
    | ----------- | ------------| 
    | [Gispen](https://www.gispen.com/nl/circulair-inrichten/nieuw-circulair-meubilair/) | Ontwikkelt circulair meubilair volgens strenge duurzame ontwerpcriteria, met hergebruikte en recyclebare materialen en een focus op maximale levensduur en reparatie. | 
    | [OPNIEUW!](https://www.opnieuw.nl/) | Biedt volledig circulaire inrichting met een focus op hergebruik en refurbishing van bestaand meubilair, met meetbare circulaire impact |
    | [Ahrend](https://www.ahrend.com/nl/diensten/furniture-as-a-service/) | Furniture-as-a-service |
    | [Lande Family](https://www.landefamily.nl/duurzaamheid) | Circulair design, nemen producten terug om ze te repareren, opnieuw te stofferen of in onderdelen te hergebruiken en hebben de ambitie om afvalvrij te produceren | 
    | [Label vandenBerg](https://label.nl/wp-content/uploads/2022/07/LABEL-Vandenberg_NL_Onderhoudsboekje_Online.pdf) | Focust op het (opnieuw) bekleden, repareren en hergebruiken van meubels. Gebruik van lokale materialen en minimaliseren van transport. |
                
    ''')