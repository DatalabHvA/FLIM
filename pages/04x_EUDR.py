import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="EUDR", layout="wide")

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

st.title('EUDR (European Union Deforestation Regulation)')

st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en Regelgeving")

st.markdown("""
De EUDR (European Union Deforestation Regulation) is een nieuwe Europese wet die ontbossing door consumptie in de EU tegengaat. 
Vanaf 30 december 2026 moet u kunnen aantonen dat uw product geen schade heeft aangebracht aan het bos. Komt uw product uit een gebied dat na 30 december 2020 ontbost is? Dan mag u het niet op de Europese markt brengen, importeren en exporteren.

Producten zijn verboden als ze van grond komen die na 30 december 2020 is ontbost. De EU-regels gelden voor onder andere:
-	Hout
-	Leer
-	Papier en karton
En alle producten die van deze grondstoffen zijn gemaakt.

**Belangrijke details over de EUDR**
*	**Doel**: Ontbossing en bosdegradatie wereldwijd verminderen.
*	**Verplichting**: Alle bedrijven, ongeacht hun omvang, moeten relevante documentatie bewaren en op verzoek van de overheid reageren op vragen.
    -	<u>Grote bedrijven</u> moeten een due diligence-verklaring (DDS) indienen, waarin ze aantonen dat het product niet bijdraagt aan ontbossing na 31 december 2020.
    -	<u>MKB-bedrijven</u> zijn niet verplicht om een volledige due diligence uit te voeren, zij moeten wel controleren of hun leveranciers (meestal grotere exploitanten) dit hebben gedaan.
*	**Traceerbaarheid**: De locatie van productie (geolocatie/coördinaten) moet worden vastgelegd
*	**Handhaving**: In Nederland controleert de NVWA.


[Klik hier voor meer informatie](https://www.nvwa.nl/onderwerpen/plant/eudr-ontbossingsverordening)

<u>**Achtergrondinformatie**</u>

**De drie kernvoorwaarden**\n
Voordat bedrijven de EU-markt betreden, moeten ze aantonen dat hun producten aan de volgende drie voorwaarden voldoen:
1.	**Ontbossingsvrij** : Producten mogen niet afkomstig zijn van land dat na 31-12-2020 ontbost is of onderhevig is geweest aan bosdegradatie. Dit geldt zowel voor directe inkoop als voor upstream-activiteiten. 
2.	**Legaal geproduceerd** : Het product moet voldoen aan alle toepasselijke wetten in het land van herkomst. Deze omvatten milieuregels, arbeidsrechten, landbezit en bescherming voor inheemse en lokale gemeenschappen. 
3.	**Due diligence-verklaring** : Er moet een formele verklaring worden ingediend via het gecentraliseerde informatiesysteem van de EU voordat het product op de EU-markt kan worden gebracht of daaruit kan worden geëxporteerd. 
Indien aan een van deze voorwaarden niet wordt voldaan, is het product niet geschikt voor handel binnen de EU. Naleving is niet vrijblijvend en moet worden aangetoond door middel van verifieerbare gegevens, correcte documentatie en tijdige indiening van de vereiste verklaring.

**Belangrijkste doelstellingen van de EUDR**
De EUDR is in het leven geroepen om de gevolgen van door ontbossing veroorzaakte handel voor het milieu en de mensenrechten aan te pakken. De belangrijkste doelstellingen weerspiegelen de inzet van de EU voor verantwoorde inkoop, klimaatactie en duurzame toeleveringsketens. De verordening omvat vier kerndoelstellingen: 
-	Voorkom dat aan ontbossing gerelateerde goederen de EU-markt betreden of verlaten. 
-	Promoot ontbossingsvrije en legaal geproduceerde producten. 
-	Steun de toezeggingen van de EU op het gebied van klimaat, biodiversiteit en mensenrechten. 
-	Zorg voor transparantie, traceerbaarheid en verantwoording in wereldwijde toeleveringsketens. 
De verordening maakt deel uit van de **Green Deal van de EU** en is een aanvulling op andere ESG-beleidsmaatregelen, zoals de Corporate Sustainability Due Diligence Directive (CSDDD) en de Corporate Sustainability Reporting Directive (CSRD). 

**Wie moet voldoen aan de EUDR-verordening?**
De EUDR definieert duidelijk de rollen en verantwoordelijkheden van bedrijven die betrokken zijn bij het op de EU-markt brengen, importeren, exporteren of verhandelen van relevante producten. 

**Operatoren en handelaren**
Exploitanten zijn entiteiten die producten voor het eerst op de EU-markt brengen of vanuit de EU exporteren. Handelaren zijn degenen die deze producten binnen de EU verder distribueren zonder de oorspronkelijke importeurs of exporteurs te zijn. Beide categorieën zijn wettelijk verantwoordelijk om ervoor te zorgen dat alle relevante producten voldoen aan de EUDR voordat ze op de markt worden gebracht of worden geëxporteerd. 
Voor grote bedrijven is de deadline voor naleving 30-12-2025. Vanaf die datum moeten zij kunnen aantonen dat de producten die onder de richtlijn vallen ontbossingsvrij zijn, legaal geproduceerd zijn en ondersteund worden door een volledige due diligence-verklaring, ingediend via het centrale informatiesysteem van de EU. Marktdeelnemers en handelaren moeten ook gegevens over de herkomst en traceerbaarheid verzamelen en bewaren voor inspecties of audits. 

**MKB-vrijstellingen en overgangsperiode**
Kleine en micro-ondernemingen profiteren van een uitgestelde nalevingsdeadline van 30 juni 2026. Hoewel MKB-ondernemers niet verplicht zijn om een volledige due diligence uit te voeren, moeten zij wel controleren of hun leveranciers (meestal grotere exploitanten) dit hebben gedaan. Alle bedrijven, ongeacht hun omvang, moeten relevante documentatie bewaren en op verzoek van de overheid reageren op vragen. 

**Meer weten?**
-	[Ondernemersplein](https://ondernemersplein.overheid.nl/duurzaam-ondernemen/milieu/verordening-ontbossingsvrije-producten-eudr-wat-betekent-dit-voor-u/#art:welke-producten-en-goederen-vallen-onder-de-eudr)

Externe links:\n
[https://benelux.bureauveritas.com/duurzaamheid/esg-ketenmanagement-verantwoord-inkopen/regelgeving-voor-ontbossingsvrije-producten](https://benelux.bureauveritas.com/duurzaamheid/esg-ketenmanagement-verantwoord-inkopen/regelgeving-voor-ontbossingsvrije-producten) \n
[https://eudr.co/eudr-regulation/](https://eudr.co/eudr-regulation/)


            """, unsafe_allow_html = True)