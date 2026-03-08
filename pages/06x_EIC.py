import streamlit as st
import sys
sys.path.append("..")

from widgets import *


st.set_page_config(page_title="ECI", layout="wide")
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

st.title('EIC Acceletator-subsidie')
st.subheader('*European Innovation Council Accelerator*')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")


html = generate_table("Opschaling", "`tot €10M",  "Individueel ")
st.markdown(html, unsafe_allow_html=True)

st.markdown('''
****1. Beschrijving subsidie****
Het EIC Accelerator programma ondersteunt innovatieve bedrijven met baanbrekende technologieën die een grote impact kunnen hebben op de Europese economie en samenleving. Het programma richt zich op scale-ups en innovatieve mkb-bedrijven die hun technologie of product willen opschalen richting marktintroductie.

De subsidie is onderdeel van het European Innovation Council (EIC) binnen het Horizon Europe programma en ondersteunt bedrijven bij:
-	het demonstreren van technologie in een operationele omgeving
-	het opschalen van productie en bedrijfsmodellen
-	het versnellen van marktintroductie van disruptieve innovaties

Naast subsidie biedt het programma ook vermogensfinanciering via het EIC Fonds, waardoor bedrijven extra investeringskapitaal kunnen aantrekken voor snelle groei.

****2. Relevantie meubelbranche**** 
Voor de meubelindustrie is het EIC Accelerator programma relevant voor bedrijven die radicaal nieuwe technologieën of circulaire innovaties ontwikkelen die de sector structureel kunnen veranderen. Zoals bijvoorbeeld het ontwikkelen van mieuwe materialen of technologieën die het gebruik van primaire grondstoffen verminderen, zoals biobased materialen of circulaire composieten. Het programma richt zich vooral op innovaties met grote impact en opschalingspotentieel in Europa.       

****3. Samenwerkingsprojecten****
In tegenstelling tot veel andere Europese subsidies kan het EIC Accelerator programma door één bedrijf worden aangevraagd.        

****4. Externe links****
[EIC Accelerator – Europese Unie](https://eic.ec.europa.eu/eic-funding-opportunities/eic-accelerator_en)            
''')