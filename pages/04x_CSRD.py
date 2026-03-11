import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="CSRD", layout="wide")

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

st.title('CSRD (Corporate Sustainability Reporting Directive)')

st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en Regelgeving")

st.markdown("""
De CSRD is een Europese richtlijn die bedrijven verplicht om uitgebreid te rapporteren over hun duurzaamheidsprestaties en de impact van hun activiteiten op mens en milieu. Deze richtlijn vervangt en versterkt de bestaande Non-Financial Reporting Directive (NFRD).
Vanaf **2025** moeten grote ondernemingen en beursgenoteerde bedrijven voldoen aan de nieuwe rapportage-eisen. Vanaf **2026** geldt dit ook voor middelgrote ondernemingen.            
            """)

st.subheader("Belangrijke details over de CSRD:")
st.markdown("""
*	**Doel**: Transparantie vergroten over de duurzaamheidsprestaties van bedrijven en investeerders, consumenten, en andere stakeholders beter informeren.
*	**Verplichting**: Bedrijven moeten rapporteren over een breed scala aan duurzaamheidsthema’s, waaronder: 
    -	Klimaatverandering en CO₂-uitstoot.
    -	Circulaire economie en gebruik van grondstoffen.
    -	Mensenrechten en arbeidsomstandigheden in de toeleveringsketen.
    -	Biodiversiteit en milieu-impact.
*	**Rapportagestandaarden**: De rapportage moet voldoen aan de Europese Sustainability Reporting Standards (ESRS).
*	**Ketenverantwoordelijkheid**: Bedrijven moeten niet alleen hun eigen activiteiten rapporteren, maar ook die van hun toeleveranciers en zakelijke partners.
*	**Handhaving**: De Autoriteit Financiële Markten (AFM) zal toezicht houden op naleving.

[Klik hier voor meer informatie](https://www.rvo.nl/onderwerpen/csrd)

           """)