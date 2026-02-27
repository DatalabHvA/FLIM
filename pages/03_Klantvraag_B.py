# pages/03_Klantvraag_Bars.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import sys
sys.path.append("..")

from Home import make_klantvraag_scatter
from widgets import *

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
    widget_klantsegment()
    widget_klanttype()
    

st.title("Klantvraag — Analyse")

c1, c2 = st.columns(2)
with c1: 
    with st.container(border = True):
        st.subheader("1. Risico's (in de markt)")

        if ss.klanttype_value == 'B2C':
            pie = go.Pie(labels=['Duurzame meubels', 'Traditionele meubels'], 
                    values=[0.07, 0.93], name='Meubelmarkt in 2030')
        elif ss.klanttype_value == 'B2B':
            pie = go.Pie(labels=['Duurzame meubels', 'Traditionele meubels'], 
                    values=[0.19, 0.81], name='Meubelmarkt in 2030')
        else:
            pie = go.Pie(labels=['Duurzame meubels', 'Traditionele meubels'], 
                    values=[0.16, 0.84], name='Meubelmarkt in 2030')
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
        if ss.klanttype_value == 'B2C':
            fig = make_klantvraag_scatter(ss.klantvraag_df_b2c)
        elif ss.klanttype_value == 'B2B':
            fig = make_klantvraag_scatter(ss.klantvraag_df_b2b)        
        fig.update_layout(
            title='Verglijking marktgroei: normale vs duurzame markt',
            legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.35),
            margin=dict(t=40, b=60, l=40, r=40),
        )
        st.plotly_chart(fig)
        st.write('Laat de sterke stijging zien van de vraag naar duurzame producten. Groeitempo is meer dan 2x sneller dan traditionele productcategorieën. Duidelijke marktkans om te benutten/nu in te stappen.')

with st.container(border = True):

    st.subheader('3.1 Klantkeuze voor duurzaam')

    st.write('Op de vraag “Hoe belangrijk is duurzaamheid voor jou bij het kiezen van meubels?” antwoordt 50% van de gevraagde consumenten dat dit belangrijk dan wel heel erg belangrijk gevonden wordt. Daarbij komt ook dat slechts 15% van de consumenten dit als ‘ (helemaal) niet belangrijk’ ervaart.')
    # Data
    categories = ['Heel erg belangrijk', 'Belangrijk', 'Neutraal', 'Niet belangrijk']
    values = [8, 42, 34, 16]
    colors = ["#005B26", '#27AE60', '#F1C40F', '#E74C3C']  # red, orange, yellow, green

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
        legend=dict(traceorder="reversed")
    )

    # Optional: to center label text better
    fig.update_traces(textfont_size=14, cliponaxis=False)

    st.plotly_chart(fig)

    st.subheader('3.2 Klantwens vs afzet')
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
    st.markdown('bron: [Milieu Centraal, D&B (iov Rijkswaterstaat)](https://www.milieucentraal.nl/media/b01enjyy/factsheet-consumenteninzichten-zitmeubilair.pdf)')

    st.subheader('3.3 Voorkeur voor lokale productie')

    st.write('1 op de 3 Nederlandse consumenten vindt het (heel erg) belangrijk dat meubels geproduceerd worden in het land waar zij zelf wonen. Hierin lopen de hoge inkomens voorop.')
    st.markdown('bron: [CBM en Q&A Retail, 2025](https://cbm.nl/publicatie/129-level-playingfield-nodig-voor-toekomst-meubelindustrie)')

    data = [
        ("Tot 80.000 euro", 25, "#4285F4"),        # blauw
        ("80.000 tot 120.000 euro", 27, "#EA4335"),# rood
        ("Meer dan 120.000 euro", 46, "#FBBC05"),  # geel
        ("Nederland totaal", 31, "#34A853"),       # groen
    ]

    # Plotly toont horizontale bar-categorieën standaard van onder naar boven.
    # Daarom draaien we de lijst om zodat "Nederland totaal" bovenaan komt.
    labels = [d[0] for d in data]
    values = [d[1] for d in data]
    colors = [d[2] for d in data]

    fig = go.Figure(
        go.Bar(
            x=values,
            y=labels,
            orientation="h",
            marker=dict(color=colors),
            text=[f"{v}%" for v in values],
            textposition="outside",
            cliponaxis=False,  # laat tekst buiten de as zien
            hovertemplate="%{y}: %{x}%<extra></extra>",
        )
    )

    fig.update_layout(
        title=dict(
            text="Het is van groot belang dat mijn meubels in<br>eigen land geproduceerd zijn",
            x=0.5,
            xanchor="center",
        ),
        height=360,
        margin=dict(l=170, r=60, t=80, b=30),
        plot_bgcolor="white",
        xaxis=dict(
            range=[0, 50],          # zodat 46% nog net past + ruimte voor label
            showgrid=False,
            ticks="",
            title=None,
        ),
        yaxis=dict(
            title=None,
            ticks="",
        ),
        showlegend=False,
    )

    st.plotly_chart(fig)

with st.container(border = True):
    st.subheader('4. Prijsperceptie en -acceptatie')

    # Data
    categories = ["Niet bereid", "5% toeslag", "10% toeslag", ">10% toeslag"]
    values = [19.0, 25.0, 24.0, 32.0]
    colors = ["#E38178", "#FBBC05", "#0FAD4E", "#2E7D3E"]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=categories,
            y=values,
            marker=dict(color=colors),
            text=[f"{v:.1f}%" for v in values],
            textposition="inside",
            textfont=dict(color="black", size=14),
            hovertemplate="%{x}: %{y:.1f}%<extra></extra>",
        )
    )

    fig.update_layout(
        title=dict(
            text="Bereidheid consument om meer te betalen<br>voor duurzaamheid",
            x=0.5,
            xanchor="center",
            font=dict(size=22)
        ),
        height=420,
        margin=dict(l=60, r=40, t=100, b=60),
        showlegend=False,
        yaxis=dict(
            range=[0, 35],
            showgrid=False,
            ticks=""
        ),
        xaxis=dict(
            ticks="",
        ),
    )

    st.plotly_chart(fig)

    st.write('Toont bereidheid van klanten (in dit geval Duitse consumenten) om een meerprijs te betalen voor duurzaamheid. Meer dan de helft is bereid 10-20% extra te betalen. Dit opent mogelijkheden voor premium positionering.')

with st.container(border = True):
    st.subheader('5. Voorbeelden uit de praktijk')

    data = [
        ["Gispen",
        "Gispen Circulair (diverse meubellijnen)",
        "Ontwikkelt circulair meubilair volgens strenge duurzame ontwerpcriteria, met hergebruikte en recyclebare materialen en een focus op maximale levensduur, reparatie en herstoffering.",
        "Kantoren, overheid, zorg, onderwijs",
        "Meubel",
        "https://www.gispen.com/nl/circulair-inrichten/nieuw-circulair-meubilair/"],

        ["OPNIEUW!",
        "Refurbished & hergebruikte meubelinrichtingen",
        "Biedt volledig circulaire inrichting met een sterke focus op hergebruik, refurbishing en reconfiguratie van bestaand meubilair, met meetbare circulaire impact (CO₂- en grondstoffenbesparing).",
        "Kantoren, overheid, onderwijs, corporate",
        "Meubel",
        "https://www.opnieuw.nl/"],

        ["Ahrend",
        "Furniture-as-a-Service (o.a. Ahrend Revived, 2020, Balance)",
        "Levert circulair kantoormeubilair via een dienstmodel, waarbij producten eigendom blijven van de producent en ontworpen zijn voor hergebruik, refurbishment en recycling.",
        "Kantoren, overheid, maatschappelijke organisaties",
        "Meubel",
        "https://www.ahrend.com/nl/diensten/furniture-as-a-service/"],

        ["Lande Family",
        "Circulaire collecties (o.a. Lande, De Vorm, Functionals)",
        "Ontwerpt circulair meubilair en neemt producten terug om te repareren, opnieuw te stofferen of in onderdelen te hergebruiken, met de ambitie om afvalvrij te produceren.",
        "Kantoren, hospitality, publieke ruimtes",
        "Meubel",
        "https://www.landefamily.nl/duurzaamheid"],

        ["Label Vandenberg",
        "Herstoffering & refurbishment services",
        "Richt zich op het (opnieuw) bekleden, repareren en hergebruiken van meubels, met gebruik van lokale materialen en minimalisering van transport en afval.",
        "Hospitality, culturele sector, high-end interieur",
        "Meubel",
        "https://label.nl/wp-content/uploads/2022/07/LABEL-Vandenberg_NL_Onderhoudsboekje_Online.pdf"],

        ["Triboo",
        "Greengridz – tafels",
        "Circulaire (werk)tafels opgebouwd uit modulaire componenten, ontworpen voor hergebruik, herconfiguratie en eenvoudige demontage, met een lage milieu-impact.",
        "Kantoren, projectinrichting, overheid",
        "Meubel",
        "https://www.triboo.eu"],

        ["Triboo",
        "Greengridz – bezels",
        "Circulaire tafelbezels die los vervangbaar zijn, ontworpen om esthetische en functionele aanpassingen mogelijk te maken zonder het volledige product te vervangen.",
        "Kantoren, projectinrichting, overheid",
        "Meubel",
        "https://www.triboo.eu"]
    ]

    columns = [
        "Bedrijfsnaam",
        "Circulaire producten/diensten",
        "Korte beschrijving",
        "Primaire filters (marktsegment)",
        "Branche",
        "Link"
    ]

    df = pd.DataFrame(data, columns=columns)

    st.table(df)