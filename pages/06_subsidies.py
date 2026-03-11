import streamlit as st
import pandas as pd
import numpy as np
import sys
import plotly.graph_objects as go
from plotly.subplots import make_subplots
sys.path.append("..")

from widgets import *

ss = st.session_state

st.set_page_config(page_title="Subsidies", layout="wide")

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
    widget_omzet()
    widget_klantsegment()

# -----------------------------
# Layout / Navigation
# -----------------------------
st.title("Subsidies")
st.caption("Versnel je circulaire plannen met publieke financiering")

st.markdown("""
Subsidies kunnen je helpen om eerder over te gaan op het verkennen, ontwikkelen, testen of opschalen van een idee nog voordat het direct (voldoende) financieel rendement oplevert. Ze zijn daarmee geen vervanging voor een gezond businessmodel, maar een instrument van de overheid om richting en versnelling te geven aan gewenste innovatie in Nederlands en Europees verband.
Subsidies zijn bedoeld om ondernemers te helpen risico’s te verkleinen bij innovaties, in dit geval op gebied van grondstoffen, ontwerp, processen en productketens. Denk hierbij aan: processn voor herstel, opknappen en hergebruik maar ook efficiëntere productie, toepassen van biobased alternatieven en andere vormen van toekomstbestendig ondernemen.


*Let op: het subsidielandschap verandert continu. De voorbeelden binnen deze factor zijn illustratief. Check altijd actuele voorwaarden bij je branchevereniging, een subsidieadviseur of een actuele subsidie-tool.*      
""")

c1, c2 = st.columns([6,2])
with c1: 
    st.subheader("Hoe zit de subsidiestructuur in elkaar?")
    st.write("Subsidies sluiten vaak aan op een specifieke fase van jouw project. Onderstaand overzicht helpt je bepalen waar jij zit en waar je moet zoeken.")

    st.image('assets/subsidies1.png')
with c2: st.write("")

with st.expander("Fase 1: Verkenning – “Is mijn idee technisch en economisch haalbaar?”"):
    st.markdown("""
Je onderzoekt:
-	Technische haalbaarheid
-	Beschikbaarheid van materialen
-	Marktpotentie
-	Kosten-batenanalyse
                
**Subsidievoorbeelden**:
                """)
    st.page_link("pages/06a_MIT_haalbaarheid.py", label = "MIT Haalbaarheidsstudie – RVO [13.2]", icon="➡")
    st.page_link("pages/06x_TSE.py", label = "TSE Industrie - Studies – RVO [13.3]", icon="➡")
    st.markdown("""                
**Voorbeeldproject**:
Een producent onderzoekt verduurzaming van zijn industriële productieprocessen. 
    """)

with st.expander("Fase 2: Ontwikkeling – “We gaan bouwen en testen.”"):
    st.markdown("""
Je werkt aan:
-	Prototype of pilot
-	Proof-of-concept
-	Samenwerking met ketenpartners
-	Testen van materiaalprestaties
                
**Subsidievoorbeelden**:
                """)
    st.page_link("pages/06a_MIT_haalbaarheid.py", label = "MIT: R&D-Samenwerkingsprojecten – RVO [13.4]", icon="➡")
    st.page_link("pages/06x_CKP.py", label = "CKP – Circulaire ketenprojecten – RVO [13.6]", icon="➡")
    st.markdown("""               
    **Voorbeeldproject**:
    Uit een Rijkswaterstaat evaluatie is gebleken dat 8 meubelpartijen al gebruik hebben gemaakt van de Circulaire Ketenprojecten-subsidie om samen met hun keten te werken naar een meer circulair proces. Verdere details zijn niet bekend. [Rijksoverheid, 2025](https://www.rijksoverheid.nl/documenten/regelingen/2025/09/03/bijlage-4-subsidieregeling-circulaire-ketenprojecten-kwink-groep)
        """)

with st.expander("Fase 3: Implementatie – “We gaan het echt doen.”"):
    st.markdown("""
Je gaat:
-	Innovatie toepassen in productie
-	Processen anders inrichten
-	Producten naar markt brengen
-	Een eerste commerciële uitrol doen
                
**Subsidievoorbeelden**:
            """)
            
    st.page_link("pages/06x_DEIplus.py", label = "DEI+ Circulaire Economie – RVO [13.5]", icon="➡")
    st.page_link("pages/06b_ERDF.py", label = "ERDF: Circular Economy – Europees [13.1]", icon="➡")

    st.markdown("""         
**Voorbeeldproject**:
Ontwikkeling van een pilot-lijn voor het recyclen van biopolyester meubelschuim tot nieuwe grondstof voor matrassen, waarmee een gesloten materiaalcyclus in de matrasketen mogelijk wordt. [Auping & Foamplant, Nederland](https://www.agro-chemie.nl/artikelen/het-circulaire-matras-is-geen-droom-meer-de-circulaire-polyestertextielketen-wordt-werkelijkheid) (DEI+ subsidie)

    """)

with st.expander("Fase 4: Opschaling – “Het werkt, nu gaan we vergroten.”"):
    st.markdown("""
Je focust op:
•	Productiecapaciteit vergroten
•	Nieuwe markten betreden
•	Internationale samenwerking
•	Verdere professionalisering
                
**Typische subsidievoorbeelden**:
                """)
    st.page_link("pages/06x_EFRO.py", label = "EFRO", icon="➡")
    st.page_link("pages/06x_EIC.py", label = "EIC Accelerator program", icon="➡")
    st.markdown("""                
**Voorbeeldproject**:
Opschaling van een circulaire productlijn naar industrieel formaat om hout-composiet producten voor badkamers internationaal aan te kunnen bieden. [Woodio, Finland](https://eic.ec.europa.eu/success-stories/eic-supported-woodio-build-full-scale-manufacturing-plant-lahti_en) (EIC subsidie)

    """)


st.subheader("Hulp nodig?")
st.write("""Het subsidielandschap kan complex aanvoelen en verandert regelmatig, dus kun je wel hulp gebruiken bij het vinden van passende regeling of bij het opstellen van de aanvraag? 

Neem dan contact op met jouw branchevereniging. Zij kunnen vaak meedenken over jouw projectidee, relevante subsidies signaleren en indien nodig doorverwijzen naar een subsidieadviseur. 

""")
