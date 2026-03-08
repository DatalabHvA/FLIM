import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="MIT - Samenwerking", layout="wide")

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

st.title('MIT: R&D-Samenwerkingsprojecten')
st.subheader('*MKB Innovatiestimulering Topsectoren – Research & Development Samenwerkingsprojecten *')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")

html = generate_table("Ontwikkeling", "€50K-€350k ",  "Samenwerking")
st.markdown(html, unsafe_allow_html=True)

st.markdown('''
****1. Beschrijving subsidie****
           
Een R&D-Samenwerkingsproject is gericht op de ontwikkeling of vernieuwing van producten, productieprocessen of diensten. Het moet een project zijn waarbij minstens twee Nederlandse mkb-bedrijven samenwerken aan nieuwe of verbeterde producten of technieken. Het project moet gedefinieerd kunnen worden als *industrieel onderzoek* en/of *experimentele ontwikkeling*.
            
*Industrieel onderzoek* is het uitzoeken en ontdekken hoe zou iets kunnen werken, voordat je het echt gaat bouwen. In de praktijk kan dit zijn:
-	Uitzoeken welke nieuwe materialen of houtsoorten geschikt zijn.
-	Onderzoeken hoe je een nieuw scharnier- of verbindingssysteem zou kunnen ontwerpen.
-	Het maken van eerste testonderdelen of proefopstellingen in een gecontroleerde omgeving (bijv. werkplaats/lab).

*Experimentele ontwikkeling* is het bouwen en testen: je gebruikt bestaande kennis om een nieuw of verbeterd product fysiek te gaan maken, testen en verfijnen. Bijvoorbeeld: 
-	Het maken van een prototype van een nieuw slim meubel.
-	Het testen van een nieuwe productiemethode (bijv. CNC-techniek, circulaire materialen).
-	Een pilotproductielijn opzetten om te kijken of het ontwerp werkt in de praktijk.
-	Verbeteringen aanbrengen na testen in “echte” omstandigheden.
            
****2. Relevantie meubelbranche**** 
Bedrijven in de meubel- en interieursector kunnen gebruikmaken van de MIT R&D Samenwerkingsprojecten wanneer zij samen met andere bedrijven of kennispartners werken aan nieuwe innovaties. De regeling is bedoeld voor mkb’s die gezamenlijk een vernieuwend product, proces of dienst ontwikkelen dat nog niet op de markt bestaat.

Daarbij is de regeling relevant voor meubelbedrijven wanneer het project:
-	**Nieuwe producten ontwikkelt die technisch vernieuwend zijn**, bijvoorbeeld circulaire of modulaire meubels, nieuwe stoffeertechnieken of slimme productoplossingen;
-	**Nieuwe productie- of bewerkingstechnieken ontwikkelt**, zoals robotisering, automatisering, digital manufacturing of geavanceerde CNC-technieken;
-   **Nieuwe duurzame materialen of componenten onderzoekt**, zoals biobased plaatmateriaal, circulaire schuimen, nieuwe verbindingssystemen of herbruikbare stofferingen;
-   **Samenwerking versterkt tussen ketenpartners**, zoals producenten, materiaalontwikkelaars, ontwerpers, leveranciers en kennisinstellingen.

Voorbeelden die passen bij de meubelindustrie zijn:
-	**Circulaire en biobased materialen**: samenwerking om nieuwe biobased plaatmaterialen, circulaire schuimen of vervangbare stofferingen te ontwikkelen;
-	**Innovatieve productietechnieken**: R&D naar robotisering, automatisering of geavanceerde machines voor schoner en efficiënter produceren;
-	**Modulaire en repareerbare meubels**: onderzoek naar nieuwe verbindingstechnieken en ontwerpprincipes om meubels makkelijker te repareren of te upgraden;
-	**Digitale innovaties**: samenwerking rond sensortechnologie, digital twins of datagedreven onderhoud om productgebruik en levensduur te verbeteren;
-	**Hogere inzet van reststromen**: R&D naar technieken om houtreststromen, textielsnijafval of retourmaterialen hoogwaardig te verwerken.

****3. Samenwerkingsprojecten****
            
Het project moet worden uitgevoerd door minimaal twee onafhankelijke mkb-ondernemingen die gezamenlijk een innovatie ontwikkelen. In het samenwerkingsverband brengt iedere partij eigen, aanvullende kennis of technologie in, waardoor het project alleen tot stand kan komen door samenwerking. Andere organisaties, zoals kennisinstellingen of grotere bedrijven, mogen aansluiten als partner, maar de kern van het project ligt altijd bij de samenwerkende mkb-bedrijven.

****4. Externe links****
            
[MIT R&D – Samenwerkingsprojecten – RVO.nl](https://www.rvo.nl/subsidies-financiering/mit-rd-samenwerkingsprojecten)
''')
