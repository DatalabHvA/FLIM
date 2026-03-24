# pages/03_Klantvraag_Bars.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import sys
sys.path.append("..")

from Home import make_klantvraag_scatter_b2b, make_klantvraag_scatter_b2c
from widgets import *

ss = st.session_state

st.set_page_config(page_title="Klantvraag B2B/B2C • Analyse", layout="wide")
st.markdown(
    """
    <style>
      /* pull content up */
      .block-container { padding-top: 0.9rem !important; }
      /* compact header */
      header[data-testid="stHeader"] { height: 1.2rem; }
      [data-testid="stSidebarNav"] {display: none;}
      [data-testid="stSidebar"] .block-container {
          padding-top: 0 !important;
      }

    section[data-testid="stSidebar"] .block-container > div:first-child,
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: -60px !important;   /* <- adjust this number */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.page_link("Home.py", label="⬅ Terug naar Home")

    st.header("Filters")
    widget_klantsegment()
    widget_klanttype()
    

if ss.klanttype_value == 'Overheid':
    st.title("Klantvraag — Overheid")

    st.markdown("""
  
    In 2021 spendeerde de Rijksoverheid ruim **85 miljard euro** aan ingekochte diensten, producten en werken.  
    In 2023 was de inkoop van *Werkplekomgeving (Rijksoverheid)* jaarlijks goed voor zo'n **60 miljoen euro**.  
    
    Het gestelde doel is dat per 2030 al voor **50% minder primaire grondstoffen** ingekocht worden, en om dit te laten toenemen tot **100% circulair in 2050**.
    Tevens is ook de ambitie uitgesproken om vanaf **2030 enkel nog gebruik te maken van circulair meubilair**.  

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

    ### Inzet per MVOI-thema            
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
            name='Circulair'
        )
    )
    fig2.add_trace(
        go.Scatter(
            x=df_mvoi['jaar'],
            y=df_mvoi['Ketenverantwoordelijkheid'],
            mode='lines+markers',
            line=dict(color="#d2a905", width=3),
            marker=dict(size=8),
            name='Ketenverantwoordelijkheid'
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
            ("Duurzaam hout",  "Hout voldoet aan Dutch Procurement Criteria", "Minimumeis"),
            ("Textiel",  "Eisen levensduur textiel", "Minimumeis"),
            ("Textiel",  "Geen gehalogeneerde blaasmiddelen", "Minimumeis"),
            ("Kunststof",  "Eisen kunststof onderdelen", "Minimumeis"),
            ("Coating", "Beperking coatingmengsels (H-zinnen)", "Minimumeis"),
            ("Samenstelling",  "Materialen eenvoudig te scheiden", "Minimumeis"),
            ("Samenstelling",  "Levering samenstellingsetiket", "Minimumeis"),
            ("Levensduur", "Nalevering onderdelen 10 jaar", "Minimumeis"),
            ("Levensduur",  "Garantie 10 jaar / 5 jaar refurbished", "Contractbepaling"),
            ("Vervoer",  "Emissieklasse 6 voertuigen", "Minimumeis"),
            ("Verpakkingen",  "Secundaire verpakking gerecycled", "Minimumeis"),
            ("Verpakkingen",  "Toelichting verpakkingskeuze", "Minimumeis"),
            ("ISV",  "Internationale Sociale Voorwaarden", "Minimumeis"),
            ("Social Return",  "Minimaal 5% social return", "Minimumeis"),
            ("Social Return",  "Rapportage social return", "Contractbepaling"),
        ],
        "🟡 Ambitieniveau 2 – Significant": [
            ("Textiel",  "Duurzame bekledingsmaterialen (OEKO-TEX)", "Minimumeis"),
            ("Textiel",  "OEKO-TEX ECO-paspoort toevoegingen", "Minimumeis"),
            ("Materiaalgebruik",  "Hoger % circulair textiel gewaardeerd", "Gunningscriterium"),
            ("Samenstelling", "Levering materialenpaspoort", "Minimumeis"),
            ("Vervoer", "Rapportage CO₂ transport", "Minimumeis"),
            ("Verpakkingen",  "Herbruikbare/recyclebare verpakking gewaardeerd", "Gunningscriterium"),
            ("Social Return",  "Hoger % social return gewaardeerd", "Gunningscriterium"),
        ],
        "🟢 Ambitieniveau 3 – Ambitieus": [
            ("Plaatmateriaal",  "Formaldehyde-emissies <30% E1", "Minimumeis"),
            ("Materiaalgebruik",  "<0,10% REACH stoffen gewaardeerd", "Gunningscriterium"),
            ("Circulaire economie",  "Plan van aanpak circulaire economie", "Gunningscriterium"),
            ("Levenscyclusanalyse",  "Levering LCA", "Minimumeis"),
            ("Verpakkingen", "Inzamelen/recyclen verpakking gewaardeerd", "Gunningscriterium"),
        ],
    }

    def df_for(level_label: str) -> pd.DataFrame:
        df = pd.DataFrame(
            data[level_label],
            columns=["Onderwerp", "Criterium", "Criteriumtype"],
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

else:
    st.title("Klantvraag — B2C & B2B")
    c1, c2 = st.columns(2)

    with c1:
        with st.container(border = True):
            st.subheader('1. Kansen (in de markt)')
            st.write('De groei van de duurzame meubelmarkt is meer dan dubbel zo groot als de traditionele productcategorieën. Dit biedt kansen om nieuw marktaandeel te claimen.')
            
            if ss.klanttype_value == 'B2C':
                fig = make_klantvraag_scatter_b2c(ss.klantvraag_df_b2c)
            elif ss.klanttype_value == 'B2B':
                fig = make_klantvraag_scatter_b2b(ss.klantvraag_df_b2b)        
            fig.update_layout(
                title='Verglijking marktgroei: normale vs duurzame markt',
                legend=dict(orientation="h", x=0.5, xanchor="center", y=-0.35),
                margin=dict(t=40, b=60, l=40, r=40),
            )
            st.plotly_chart(fig)    
    
    with c2: 
        with st.container(border = True):
            st.subheader("2. Risico's (in de markt)")
            st.write('Een groeiend deel van de markt verwacht duurzame alternatieven. Gebrek aan actie op dit gebied vormt een risico tot verlies van marktaandeel en afname van klanttevredenheid.')

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

    with st.container(border = True):

        with st.expander('**3.1 Klantkeuze voor duurzaam**'):
            # Data
            if ss.klanttype_value == 'B2B':
                st.write('Op de vraag naar relevantie van duurzame inkoop en verantwoorde ketens antwoordt 64% van de gevraagde afnemers dat dit belangrijk gevonden wordt. Daarbij vindt slechts 8% dit onbelangrijk')
                categories = ['Erg relevant','Enigzins relevant','Niet erg relevant','Geenzins relevant']
                values = [65, 27, 6, 2]
                colors = ["#05853A", "#2BC417", '#F1C40F', '#E74C3C']  # red, orange, yellow, green
                title_text = "Relevantie van duurzame inkoop en verantwoorde ketens"
            else:
                st.write('Op de vraag “Hoe belangrijk is duurzaamheid voor jou bij het kiezen van meubels?” antwoordt 50% van de gevraagde consumenten dat dit belangrijk gevonden wordt. Daarbij vindt slechts 16% van de consumenten duurzaamheid onbelangrijk')
                categories = ['Heel erg belangrijk', 'Belangrijk', 'Neutraal', 'Niet belangrijk']
                values = [8, 42, 34, 16]
                colors = ["#05853A", "#2BC417", '#F1C40F', '#E74C3C']  # red, orange, yellow, green
                title_text = 'Belang van duurzaamheid bij het kiezen van meubels'
            # Cumulative values for text positioning
            cumulative = [sum(values[:i+1]) for i in range(len(values))]

            # Build the figure
            fig = go.Figure()

            for i, (category, value, color) in enumerate(zip(categories, values, colors)):
                fig.add_trace(go.Bar(
                    y=["Respondenten"],
                    x=[value],
                    name=category,
                    orientation='h',
                    marker=dict(color=color),
                    text=f"{value}%",
                    textposition='inside',
                    insidetextanchor='middle',
                    textfont=dict(color="black", size=14),
                    hovertemplate=f"{category}<br>{value}% van respondenten<extra></extra>",
                    legendrank=len(categories) - i
                ))

            # Layout
            fig.update_layout(
                barmode='stack',
                title=title_text,
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
            if ss.klanttype_value == 'B2C':
                st.markdown('*(Bron: [CBM en Q&A Retail, 2025](https://cbm.nl/publicatie/129-level-playingfield-nodig-voor-toekomst-meubelindustrie))*')
            else:
                st.markdown("""
Op de vraag aan bedrijven binnen een grootschalig Duits onderzoek naar hoe relevant duurzame inkoop en verantwoorde toeleveringsketens voor hen zijn, gaf het overgrote deel aan dat dit (zeer) belangrijk is.

[Bron](https://unite.eu/nl-nl/media/pers/studie-duurzame-b2b-inkoop)                            
                            """)
                            
        if ss.klanttype_value == 'B2C':
            with st.expander('**3.2 Klantwens vs afzet**'):
                st.write('Deze vergelijking tussen wat klanten willen (hoge voorkeur voor duurzame producten) en wat daadwerkelijk wordt verkocht toont een mismatch. Klanten willen duurzamer, maar het vertaalt zich niet in verkoopcijfers. Komt dit omdat het huidige aanbod hier nog niet voldoende aansluit of gemakkelijk genoeg beschikbaar is? Wat met zekerheid gezegd kan worden: Tussen de 40-50% van de duurzame vraag naar meubels blijft momenteel onvervuld.')
                
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

                st.markdown('*(Bron: [Milieu Centraal, D&B (iov Rijkswaterstaat), 2023](https://www.milieucentraal.nl/media/b01enjyy/factsheet-consumenteninzichten-zitmeubilair.pdf))*')
        else:
            with st.expander('**3.2 Klantwens vs afzet**'):
                p1, p2 = st.columns(2)
                                
                p1.write("Een grote Duitse studie onder inkopers en bestuurders heeft aangetoond dat duurzaamheid tegenwoordig steeds meer wordt geïntegreerd in inkoopbeleid (51%) en inkoopstrategieën (40%). Beiden tonen een 9% en 7% stijging ten opzichte van 2020. (Jaro, 2023)")
                p1.write("Of beleid en strategieën daadwerkelijk worden toegepast in de dagelijkse activiteiten van het bedrijf, hangt echter af van inkoopbeslissingen. In dit opzicht blijven de daadwerkelijke effecten van beleid en strategieën nog achter, aangezien zaken als levenscycluskostenanalyse, risicobeoordeling en de duurzaamheidsprestaties van leveranciers nog niet bovenaan de lijst staan als het gaat om besluitvormingscriteria (zie visual).")
                
                p2.image('assets/B2B_3_2.png')
                p1.markdown('[bron](https://unite.eu/assets/2023_jaro_whitepaperstudie2023_en.pdf)')
        if ss.klanttype_value == 'B2C':
            with st.expander('**3.3 Voorkeur voor lokale productie**'):

                st.write('1 op de 3 Nederlandse consumenten vindt het (heel erg) belangrijk dat meubels geproduceerd worden in het land waar zij zelf wonen. Hierin lopen de hoge inkomens voorop.')

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
                st.markdown('*(Bron: [CBM en Q&A Retail, 2025](https://cbm.nl/publicatie/129-level-playingfield-nodig-voor-toekomst-meubelindustrie))*')
                
    with st.container(border = True):
        with st.expander('**4. Prijsperceptie en -acceptatie**'):
            st.write('Toont bereidheid van klanten om een meerprijs te betalen voor duurzaamheid. Meer dan de helft is bereid 10-20% extra te betalen. Dit opent mogelijkheden voor premium positionering.(uit enquête Duitse markt)')

            # Data
            if ss.klanttype_value == 'B2B':
                categories = ["Niet bereid", "5% toeslag", "10% toeslag", ">10% toeslag"]
                values = [19.0, 25.0, 24.0, 32.0]
                colors = ["#E38178", "#FBBC05", "#0FAD4E", "#2E7D3E"]
                title_text = "Bereidheid consument om meer te betalen<br>voor duurzaamheid"
            elif ss.klanttype_value == 'B2C':
                categories = ['Bereid om veel meer te betalen','Bereid om enigszins meer te betalen','Bereid om een klein beetje meer te betalen','Weet het niet','Niet bereid om meer te betalen']
                values = [5.50, 38.80, 12.70, 35.40, 7.60]
                colors = ["#E38178", "#FBBC05", "#9EB8A9",  "#0FAD4E", "#2E7D3E"]
                title_text = "Bereidheid bedrijven om meer te betalen voor duurzaamheid"

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
                    text=title_text,
                    x=0.5,
                    xanchor="center",
                    font=dict(size=22)
                ),
                height=420,
                margin=dict(l=60, r=40, t=100, b=60),
                showlegend=False,
                yaxis=dict(
                    range=[0, max(values)],
                    showgrid=False,
                    ticks=""
                ),
                xaxis=dict(
                    ticks="",
                ),
            )

            st.plotly_chart(fig)

            st.markdown('*(Bron: [PwC, 2024](https://www.pwc.com/gx/en/issues/c-suite-insights/voice-of-the-consumer-survey/2024.html))*')
            
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
