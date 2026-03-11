import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="VSME", layout="wide")

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

st.title('VSME (Voluntary Sustainability Reporting Standard for SMEs)')

st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en Regelgeving")

st.markdown("""
De VSME is een Europese rapportagestandaard voor kleine en middelgrote ondernemingen. Deze standaard is ontwikkeld voor bedrijven die niet onder de CSRD-verplichting vallen, maar wel steeds vaker gevraagd worden om informatie te leveren over hun duurzaamheidsprestaties.

De VSME helpt bedrijven om op een eenvoudige en gestructureerde manier inzicht te geven in hun impact op onderwerpen zoals CO₂-uitstoot, grondstoffengebruik en sociale omstandigheden in de keten.

Hoewel de VSME vrijwillig is, wordt deze standaard steeds belangrijker omdat grote bedrijven, banken en opdrachtgevers duurzaamheidsinformatie vragen van hun leveranciers.
   
            """)
st.subheader("Belangrijke details over de VSME:")
st.markdown("""
*	**Doel**: MKB-bedrijven ondersteunen bij het verzamelen en delen van duurzaamheidsinformatie, zodat zij beter kunnen aansluiten bij de informatiebehoefte van klanten, financiers en ketenpartners die wel CSRD -plichtig zijn.
*	**Verplichting**: De VSME is niet wettelijk verplicht. Bedrijven kunnen de standaard gebruiken om **vrijwillig een duurzaamheidsrapportage op te stellen** die aansluit bij Europese CSRD rapportage-eisen op: 
    -	Klimaatverandering en CO₂-uitstoot.
    -	Circulaire economie en gebruik van grondstoffen.
    -	Mensenrechten en arbeidsomstandigheden in de toeleveringsketen.
    -	Biodiversiteit en milieu-impact.
*	**Rapportagestandaarden**: De rapportage moet voldoen aan de Europese Sustainability Reporting Standards (ESRS).
*	**Ketenverantwoordelijkheid**: Steeds meer grote bedrijven vragen hun leveranciers om gegevens over bijvoorbeeld CO₂-uitstoot, materialen en circulariteit. De VSME helpt MKB-bedrijven om deze informatie gestructureerd en vergelijkbaar aan te leveren.
*	**Handhaving**: De VSME is een vrijwillige standaard en kent daarom geen directe handhaving door toezichthouders.

[Klik hier voor meer informatie](https://www.rvo.nl/onderwerpen/vsme)

            """)