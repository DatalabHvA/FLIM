# pages/03_Klantvraag_Bars.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import sys
sys.path.append("..")

from widgets import *

ss = st.session_state

st.set_page_config(page_title="Klantvraag Overheid • Analyse", layout="wide")
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

st.title("Klantvraag Overheid — Analyse")

st.markdown("""
### Intro

In 2021 spendeerde de Rijksoverheid ruim **85 miljard euro** aan ingekochte diensten, producten en werken.  
Het gestelde doel is dat hier per **2030** al voor **50% minder primaire grondstoffen** voor gebruikt worden, en om dit te laten toenemen tot **100% circulair in 2050**.

In 2023 was de inkoop van *Werkplekomgeving (Rijksoverheid)* jaarlijks goed voor zo'n **60 miljoen euro**.  
Toen is ook de ambitie uitgesproken om vanaf **2030 enkel nog gebruik te maken van circulair meubilair**.  

*(Bron: [Rijksoverheid](https://www.denkdoeduurzaam.nl/actueel/nieuws/2023/11/13/duurzame-revolutie-op-de-werkplek-focus-op-circulair-meubilair-en-consuminderen))*

---

### MVOI – Wat is het?

“Nederland staat voor belangrijke maatschappelijke uitdagingen, zoals het aanpakken van klimaatverandering en het overstappen naar een circulaire economie.  

Maatschappelijk verantwoord opdrachtgeven en inkopen (MVOI) is een manier waarop de overheid kan helpen bij het aanpakken van deze uitdagingen door zorgvuldig te kiezen wat ze koopt.
Centrale en decentrale overheden, inclusief overheidsinstellingen, kopen jaarlijks gezamenlijk voor circa **85 miljard euro (2021)** aan diensten, producten en werken in. Hiermee heeft de overheid een groot effect op de samenleving.
MVOI houdt in dat aanbestedende diensten niet alleen rekening houden met de prijs van hun inkopen, maar ook met de milieu- en sociale effecten. Deze effecten zijn ondergebracht in zes thema’s:

 - Milieu en Biodiversiteit  
 - Klimaat  
 - Circulair (inclusief biobased)  
 - Ketenverantwoordelijkheid (Internationale Sociale Voorwaarden)  
 - Diversiteit & Inclusie  
 - Social Return.”

*(Bron: [RIVM, 2025](https://www.rivm.nl/maatschappelijk-verantwoord-opdrachtgeven-en-inkopen/wat-is-mvoi))*

### Inzet per MVOI-thema (B/C)            
""")

df_mvoi = pd.DataFrame({'jaar' : ['2015-2016', '2017-2018', '2019-2020', '2021-2022'],
                        'Totaal MVOI' : [0.78, 0.87, 0.87, 0.79],
                        'Circulair' : [0.26, 0.35, 0.46, 0.39],
                        'Ketenverantwoordelijkheid' : [0.14, 0.23, 0.14, 0.09]})

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df_mvoi['jaar'],
        y=df_mvoi['Totaal MVOI'],
        mode='lines+markers',
        line=dict(color='#1f5f7a', width=3),
        marker=dict(size=8),
        name='Totaal MVOI'
    )
)

fig.update_layout(
    title="Aandeel inkoop/aanbesteding met MVOI-criteria",
    yaxis=dict(
        range=[0.70, 0.90],
        tickformat=".0%",
        showgrid=True,
        gridcolor='lightgrey'
    ),
    xaxis=dict(
        showgrid=False
    ),
    margin=dict(l=40, r=40, t=80, b=40)
)

fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=df_mvoi['jaar'],
        y=df_mvoi['Circulair'],
        mode='lines+markers',
        line=dict(color="#0d394c", width=3),
        marker=dict(size=8),
        name='Totaal MVOI'
    )
)
fig2.add_trace(
    go.Scatter(
        x=df_mvoi['jaar'],
        y=df_mvoi['Ketenverantwoordelijkheid'],
        mode='lines+markers',
        line=dict(color="#d2a905", width=3),
        marker=dict(size=8),
        name='Totaal MVOI'
    )
)
fig2.update_layout(
    title="Inzet per MVOI-thema",
    yaxis=dict(
        range=[0.0, 0.50],
        tickformat=".0%",
        showgrid=True,
        gridcolor='lightgrey'
    ),
    xaxis=dict(
        showgrid=False
    ),
    margin=dict(l=40, r=40, t=80, b=40),
    legend=dict(
        orientation="h",          # horizontaal
        yanchor="top",
        y=-0.25,                  # onder de plot
        xanchor="center",
        x=0.5
    )
)

cols = st.columns(2)
with cols[0]:
    st.plotly_chart(fig)
with cols[1]: 
    st.plotly_chart(fig2)

st.write("De tweejaarlijkse onderzoeken van het RIVM op gebied van toepassing van MVOI-criteria binnen inkoop- en aanbestedingstrajecten toont dat meer dan een >75% aandeel van alle trajecten hier actief op selecteert. Hiervan bevat meer dan de helft eisen op gebied van toekomstbestendige keuzes op gebied van grondstoffen, ontwerp en ketenverantwoordelijkheid.")

st.markdown("### Ambitieniveau bij uitvraag MVOI")

df_mvi_ambitie = pd.DataFrame({
    "Jaar": ["2015-2016", "2017-2018", "2019-2020", "2021-2022"],
    "Geen MVI toegepast": [0.22, 0.13, 0.13, 0.22],
    "MVI toegepast": [0.78, 0.00, 0.00, 0.00],
    "Basis": [0.00, 0.35, 0.19, 0.19],
    "Significant/ambitieus": [0.00, 0.52, 0.68, 0.59]
})

fig3 = go.Figure()

colors = {
    "Geen MVI toegepast": "#4EA72E",     # lichtgroen
    "MVI toegepast": "#9C2E97",          # paars
    "Basis": "#2E6B1F",                  # donkergroen
    "Significant/ambitieus": "#2492B8"   # blauw
}

for col in ["Geen MVI toegepast", "MVI toegepast", "Basis", "Significant/ambitieus"]:
    fig3.add_trace(
        go.Bar(
            x=df_mvi_ambitie["Jaar"],
            y=df_mvi_ambitie[col],
            name=col,
            marker_color=colors[col]
        )
    )

fig3.update_layout(
    barmode="stack",
    yaxis=dict(
        range=[0, 1],
        tickformat=".0%",
        showgrid=True,
        gridcolor="lightgrey"
    ),
    legend=dict(
        orientation="h",
        yanchor="top",
        y=-0.2,
        xanchor="center",
        x=0.5
    ),
    margin=dict(l=40, r=40, t=80, b=100)
)

cols2 = st.columns(2)
with cols2[0]:
    st.plotly_chart(fig3)

st.markdown("""
In 2021-2022 besteedde 79% van de aanbestedingen aandacht aan MVOI (Maatschappelijk Verantwoord Opdrachtgeven en Inkopen). Bijvoorbeeld door bij de aanbestedingen geschiktheidseisen, selectiecriteria, minimumeisen en contractbepalingen te gebruiken op het gebied van duurzaamheid. [RIVM, 2024](https://www.rivm.nl/maatschappelijk-verantwoord-opdrachtgeven-en-inkopen/trends-in-mvoi)

*Het ambitieniveau "basis" is bedoeld om niet-duurzame producten, diensten en werken uit te sluiten. De criteria voor "significant" en "ambitieus" gaan een stap verder. Die hebben als doel het aanmoedigen van duurzame producten en het stimuleren van innovatieve oplossingen. De criteria voor elk ambitieniveau staan op [mvicriteriatool](https://www.mvicriteria.nl/nl) per productgroep aangegeven. Deze inkoopcriteria worden regelmatig aangescherpt. Voor de periode 2015-2016 is enkel onderscheid gemaakt tussen wel of geen gebruik van MVOI (Maatschappelijk Verantwoord Opdrachtgeven en Inkopen). Onderscheid in ambitieniveaus bestond toen nog niet.*            

""")

st.markdown("""
### MVOI-criteria kantoormeubilair per ambitieniveau
""")

import streamlit as st
import pandas as pd

# --- Data -------------------------------------------------
data = {
    "🔴 Ambitieniveau 1 – Basis": [
        ("Duurzaam hout", "18,010", "Hout voldoet aan Dutch Procurement Criteria", "Minimumeis"),
        ("Textiel", "18,031", "Eisen levensduur textiel", "Minimumeis"),
        ("Textiel", "18,036", "Geen gehalogeneerde blaasmiddelen", "Minimumeis"),
        ("Kunststof", "18,011", "Eisen kunststof onderdelen", "Minimumeis"),
        ("Coating", "18,039", "Beperking coatingmengsels (H-zinnen)", "Minimumeis"),
        ("Samenstelling", "18,012", "Materialen eenvoudig te scheiden", "Minimumeis"),
        ("Samenstelling", "18,046", "Levering samenstellingsetiket", "Minimumeis"),
        ("Levensduur", "18,002", "Nalevering onderdelen 10 jaar", "Minimumeis"),
        ("Levensduur", "18,001", "Garantie 10 jaar / 5 jaar refurbished", "Contractbepaling"),
        ("Vervoer", "18,014", "Emissieklasse 6 voertuigen", "Minimumeis"),
        ("Verpakkingen", "18,018", "Secundaire verpakking gerecycled", "Minimumeis"),
        ("Verpakkingen", "18,022", "Toelichting verpakkingskeuze", "Minimumeis"),
        ("ISV", "18,021", "Internationale Sociale Voorwaarden", "Minimumeis"),
        ("Social Return", "18,040", "Minimaal 5% social return", "Minimumeis"),
        ("Social Return", "18,043", "Rapportage social return", "Contractbepaling"),
    ],
    "🟡 Ambitieniveau 2 – Significant": [
        ("Textiel", "18,033", "Duurzame bekledingsmaterialen (OEKO-TEX)", "Minimumeis"),
        ("Textiel", "18,035", "OEKO-TEX ECO-paspoort toevoegingen", "Minimumeis"),
        ("Materiaalgebruik", "18,007", "Hoger % circulair textiel gewaardeerd", "Gunningscriterium"),
        ("Samenstelling", "18,024", "Levering materialenpaspoort", "Minimumeis"),
        ("Vervoer", "18,048", "Rapportage CO₂ transport", "Minimumeis"),
        ("Verpakkingen", "18,020", "Herbruikbare/recyclebare verpakking gewaardeerd", "Gunningscriterium"),
        ("Social Return", "18,041", "Hoger % social return gewaardeerd", "Gunningscriterium"),
    ],
    "🟢 Ambitieniveau 3 – Ambitieus": [
        ("Plaatmateriaal", "18,030", "Formaldehyde-emissies <30% E1", "Minimumeis"),
        ("Materiaalgebruik", "18,028", "<0,10% REACH stoffen gewaardeerd", "Gunningscriterium"),
        ("Circulaire economie", "18,016", "Plan van aanpak circulaire economie", "Gunningscriterium"),
        ("Levenscyclusanalyse", "18,047", "Levering LCA", "Minimumeis"),
        ("Verpakkingen", "18,023", "Inzamelen/recyclen verpakking gewaardeerd", "Gunningscriterium"),
    ],
}

def df_for(level_label: str) -> pd.DataFrame:
    df = pd.DataFrame(
        data[level_label],
        columns=["Onderwerp", "Code", "Criterium", "Criteriumtype"],
    )
    return df

# --- UI ---------------------------------------------------
st.header("Ambitieniveau MVOI")

levels = list(data.keys())
selected_level = st.selectbox("Selecteer een ambitieniveau", levels, key="ambitieniveau")

df_show = df_for(selected_level)

# optioneel: iets netter tonen
st.caption(f"Huidige MVOI eisen meubilair: {len(df_show)} criteria")
st.dataframe(df_show, use_container_width=True, hide_index=True)

st.markdown("""
Bezoek voor verdere details de [MVI-criteriatool website](https://www.mvicriteria.nl/nl/webtool#//23/2//nl)
            
*(Bron: [Kantoormeubels](https://www.mvicriteria.nl/nl/webtool#//23/2//nl))*
""")

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