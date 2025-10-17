import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Personeel", layout="wide")

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
            padding-top: 2.0rem !important;
        }

    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.subheader('1. Ontwikkelingen rond personeel in de meubelbranche')
st.page_link("Home.py", label="⬅ Terug naar Home")

st.markdown('''
**Tekort aan arbeidskrachten vormt een grote productiebelemmering**

Uit de Conjunctuurmonitor 2024 van CBM blijkt dat de meubelbranche continu nieuw personeel moet aannemen. 87% van de ondervraagde WMB-bedrijven zagen hun personeelsbestand groeien, en 22% van hen ervoer een toename in de wervingsinspanningen ten opzichte van voorgaande jaren.
''')

with st.container(border = True):
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("2. Risico's")
        st.markdown('''
        **Mislopen en verliezen van jong talent door gebrek een duurzaamheid**
        
        Jonge generaties, met name Gen Z en Millennials, hechten steeds meer waarde aan ethische overwegingen bij hun keuze voor werk en werkgevers. Uit onderzoek blijkt dat ongeveer de helft van de Gen Z'ers wereldwijd en 40% van de Millennials bereid zijn een opdracht of potentiële werkgever af te wijzen als deze niet aansluiten bij hun persoonlijke overtuigingen, waaronder duurzaamheid. Werkgevers die duurzaamheid en maatschappelijke verantwoordelijkheid niet integreren, riskeren waardevolle medewerkers te verliezen. Het is daarom essentieel om duurzaamheid niet alleen als een milieukwestie te zien, maar als een strategisch voordeel voor het aantrekken en behouden van talent.
        
        [Download het rapport: Deloitte - 2024 Gen Z en Millennial Survey](https://www.deloitte.com/content/dam/assets-zone2/nl/nl/docs/about/2024/deloitte-nl-con-genz-millennial-survey-2024-country-report-netherlands.pdf)
        ''')
    with c2: 
        # Define categories and values
        topics = ['Opdracht', 'Werkgever']

        # Values per group per topic
        values = {
            "Global Gen Z": [50, 44],
            "Global millennials": [43, 40],
            "Nederlandse Gen Z": [41, 36],
            "Nederlandse millennials": [31, 29]
        }

        # Define consistent colors
        colors = {
            "Global Gen Z": "#009CA6",         # Teal
            "Global millennials": "#5B5B5B",   # Dark grey
            "Nederlandse Gen Z": "#00726B",    # Dark teal
            "Nederlandse millennials": "#BFBFBF"  # Light grey
        }

        # Build figure
        fig = go.Figure()

        for label, vals in values.items():
            fig.add_trace(go.Bar(
                x=topics,
                y=vals,
                name=label,
                text=[f"{v}%" for v in vals],
                textposition="outside",
                marker_color=colors[label]
            ))

        # Layout settings
        fig.update_layout(
            barmode="group",
            xaxis_title="",
            yaxis_title="Percentage",
            template="plotly_white",
            margin=dict(l=00, r=00, t=00, b=40),  # left, right, top, bottom
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig)
        st.caption('Percentage resprondenten die opdrachten of potentiële werkgevers afgewezen hebben op basis van persoonlijke ethiek/overtuigingen.')

with st.container(border = True):
    st.subheader('3. Kansen')
    st.markdown('''

    Wist je dat **69%** van de branche aangeeft dat wervingsproblemen samenhangen met concurrentie binnen de bedrijfssector?

    - **Duurzaamheid en maatschappelijke betrokkenheid worden steeds meer een harde eis bij werkzoekenden**     
    Millennials en Generatie Z hervormen de arbeidsmarkt door duurzaamheid en maatschappelijke verantwoordelijkheid te eisen als ononderhandelbare onderdelen van hun werk. Bedrijven die zich niet aanpassen aan deze verwachtingen riskeren waardevolle talenten te verliezen. [Deloitte Global Millennial Survey 2024](https://www.deloitte.com/nl/nl/services/consulting/research/2024-gen-z-and-millennial-survey.html)

    - **Jongere generaties hebben steeds meer voorkeur van zingeving boven salaris**
    Generatie Z en millennials willen werken voor bedrijven die aansluiten bij hun waarden en een positieve impact hebben op de maatschappij en het milieu. Dit gaat vaak boven salaris of functietitel. [Deloitte Global Millennial Survey 2024, Forbes, The Rise of Purpose-Driven Careers, 2023](https://www.deloitte.com/nl/nl/services/consulting/research/2024-gen-z-and-millennial-survey.html)

    - **Betekenisvol werk is de sleutel tot werknemersbetrokkenheid**
    Betekenisvol werk is de belangrijkste drijfveer voor betrokkenheid bij jongere werknemers. 77% van Generatie Z geeft aan dat ze willen dat hun baan een positieve sociale of ecologische impact heeft. [Gallup State of the Global Workplace Report 2023](https://advisor.visualcapitalist.com/wp-content/uploads/2023/06/state-of-the-global-workplace-2023-download.pdf)

    - **Duurzaamheids verbintenis versterkt behoud van jonge generatie werknemers**
    Jongere generaties blijven vaker bij organisaties die een authentieke betrokkenheid bij  maatschappelijke verantwoordelijkheid tonen. Organisaties die deze thema’s integreren in hun cultuur, zullen in staat zijn om jong talent langer aan zich te binden. [PwC Workforce of the Future Report 2024](https://www.pwc.com.tr/global-workforce-sustainability-study-2024)

    - **Duurzaamheid verhoogt de aantrekkelijkheid van techniek**
    Uit onderzoek voor de Tech Barometer 2024 blijkt dat 55% van de zij-instromers in technische beroepen het groeiend belang van duurzaamheid als een belangrijke factor ziet die de technieksector aantrekkelijker maakt.. - [Tech Barometer 2024](https://www.rovc.nl/over-rovc/meer-over-rovc/documenten-en-downloads/algemene-brochures-en-publicaties/techbarometer-2024)
         
                
                
                
                
    ''')