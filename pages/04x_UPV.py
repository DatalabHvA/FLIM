import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="UPV", layout="wide")

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

st.title('Uitgebreide Producentenverantwoordelijkheid (UPV)')
st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en regelgeving")

st.markdown("""
De UPV is een Europese regelgeving die producenten en importeurs verantwoordelijk stelt voor de gehele levenscyclus van hun producten, met name voor de inzameling, hergebruik en recycling aan het einde van de levensduur. Deze wet is bedoeld om afval te verminderen en de circulaire economie te stimuleren.
    """)
st.subheader("Wanneer verplicht?")
st.markdown("""
De rijksoverheid stelt als doel om in 2030 een UPV voor meubels in te stellen. Deze moet eraan bijdragen dat meubels beter ingezameld, hergebruikt, opgeknapt, gerepareerd en gerecycled worden. Producten die niet voldoen aan de UPV-eisen, mogen niet op de Europese markt worden verkocht.

**Belangrijke details over de UPV:**
*	**Doel**: Afval voorkomen, hergebruik stimuleren en de milieu-impact van producten verminderen door producenten verantwoordelijk te maken voor de afvalfase.
*	**Verplichting**: Producenten en importeurs moeten: 
    -	Zich registreren bij een erkende producentenorganisatie.
    -	Financieel bijdragen aan de inzameling, sortering en recycling van hun producten.
    -	Informatie verstrekken over hoe producten op een milieuvriendelijke manier kunnen worden weggegooid of gerecycled.
    -	Voldoen aan specifieke recyclingdoelstellingen per productcategorie.
*	**Traceerbaarheid**: Producenten moeten kunnen aantonen dat hun producten op de juiste manier worden ingezameld en verwerkt.
*	**Handhaving**: In Nederland is de Rijksdienst voor Ondernemend Nederland (RVO) verantwoordelijk voor de handhaving van de UPV-regelgeving. Bedrijven die zich niet houden aan de regels, riskeren boetes of marktverboden.

[Klik hier voor meer informatie](https://www.afvalcirculair.nl/uitgebreide-producentenverantwoordelijkheid-upv/)
    """)

st.subheader("Achtergrondinformatie")
st.markdown("""
<u>Relevantie voor jouw branche</u>\n
De Uitgebreide Producentenverantwoordelijkheid (UPV) Meubels zal grote impact hebben op de meubelbranche. Producenten en importeurs worden namelijk direct verantwoordelijk voor de inzameling en verwerking van hun producten aan het einde van de levensduur. Dat betekent dat consumenten en bedrijven hun oude meubels kosteloos moeten kunnen inleveren, inclusief logistiek en verwerking. Deze verantwoordelijkheid ligt volledig bij de producent of importeur. Voor een [groot aantal productgroepen](https://www.afvalcirculair.nl/uitgebreide-producentenverantwoordelijkheid-upv/) is er al een UPV.

            """, unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1: 
    st.subheader("Risico's")
    st.markdown("""
        - **Hogere kosten**: Het opzetten van systemen om de eindverwerking en recycling van producten te organiseren kunnen in het begin leiden tot hogere operationele kosten.
        - **Verlies afzetmarkten**: Fabrikanten die niet in staat zijn om te voldoen aan de UPV-verplichtingen, kunnen het risico lopen hun producten uit bepaalde markten te verliezen, vooral in landen met strikte handhaving.
        - **Noodzaak voor vereniging**: De initiële verantwoordelijkheid voor de wettelijke regeling ligt bij individuele producenten, wat het organiseren en financieren van de eindverwerking van producten complex maakt, waardoor fabrikanten genoodzaakt zijn zich te verenigen om de verplichtingen gezamenlijk uit te voeren.
        """)
with c2: 
    st.subheader("Kansen")
    st.markdown("""
        - **Tariefdifferentiatie** biedt een financiële prikkel voor duurzaam of circulair ontwerpen. Bijvoorbeeld: korting bij toepassing van een percentage recycled content
        - Om te komen tot een goed werkend systeem wordt **samenwerking met ketenpartners** (producenten, retailers, inzamelaars, recyclers) belangrijk, dit biedt kansen voor nieuwe businessmodellen.
        -De UPV zal bijdragen aan betere inzameling van meubels en biedt kansen voor **hergebruik** en restauratie.

                
                """)

st.markdown("""
<u>Externe links</u>

[Meer informatie over Uitgebreide Producentenverantwoordelijkheid (UPV)](https://www.afvalcirculair.nl/uitgebreide-producentenverantwoordelijkheid-upv/) 
            """, unsafe_allow_html=True)