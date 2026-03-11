import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="CBAM", layout="wide")

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

st.title('CBAM (Carbon Border Adjustment Mechanism)')

st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en Regelgeving")
st.markdown("""
Het **CBAM** is een nieuwe Europese regelgeving die vanaf **1 oktober 2023** gefaseerd wordt ingevoerd. Het mechanisme heft een prijs op de CO₂-uitstoot van geïmporteerde goederen, om zo te voorkomen dat Europese bedrijven die betalen voor hun CO₂-uitstoot oneerlijk worden beconcureerd door buitenlandse producenten met lagere milieueisen. CBAM is bedoeld om "carbon leakage" (het verplaatsen van productie naar landen met lagere milieustandaarden) tegen te gaan en de wereldwijde CO₂-uitstoot te verminderen.

CBAM geldt voor CO2-intensieve productcategorieën als ijzer, staal en aluminium. 

**Wanneer verplicht?**\n
CBAM trad in werking op 1 oktober 2023 met een overgangsperiode tot 31 december 2025. Wie vanaf 2026 CBAM-goederen invoert in de EU moet vooraf een toelating aanvragen en een prijs betalen voor de CO2-uitstoot.
            """)
st.subheader("Belangrijke details over CBAM:")

st.markdown("""            
*	**Doel**: Een gelijk speelveld creëren voor Europese en buitenlandse producenten, en de wereldwijde CO₂-uitstoot verminderen door importeurs te stimuleren om duurzamere producten te kiezen.
*	**Verplichting**: Importeurs moeten: 
    -	**Rapportage**: Jaarlijks rapporteren over de directe en indirecte CO₂-uitstoot van geïmporteerde goederen.
    -	**Betaling**: Het verschil in CO₂-prijs tussen het land van herkomst en de EU betalen, als de CO₂-kosten in het land van herkomst lager zijn.
    -	**Certificaten kopen**: CBAM-certificaten kopen om de CO₂-uitstoot van hun import te compenseren.

*	**Handhaving**: In Nederland is de **Douane** verantwoordelijk voor de handhaving van CBAM. Importeurs die niet voldoen, riskeren boetes of importverboden.

[Klik hier voor meer informatie](https://www.douane.nl/onderwerpen/vgem/milieu/cbam/)
            """)