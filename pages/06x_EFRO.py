import streamlit as st

st.set_page_config(page_title="EFRO", layout="wide")
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

st.title('EFRO-subsidie')
st.subheader('*Europees Fonds voor Regionale Ontwikkeling*')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")


html = generate_table("Opschaling", "vanaf €50K",  "Individueel of samenwerking")
st.markdown(html, unsafe_allow_html=True)

st.markdown('''
****1. Beschrijving subsidie****
Het Europees Fonds voor Regionale Ontwikkeling (EFRO) ondersteunt projecten die bijdragen aan economische ontwikkeling, innovatie en verduurzaming van regionale economieën in Europa. In Nederland wordt EFRO uitgevoerd via regionale programma’s zoals Kansen voor West, waarbij bedrijven, kennisinstellingen en overheden samenwerken aan innovatieve oplossingen.

Binnen deze programma’s is een belangrijk doel het versnellen van de transitie naar een circulaire economie, onder andere door:
-	het ontwikkelen en opschalen van circulaire toepassingen in productieketens
-	het aanpassen van materialen en productieprocessen
-	het terugwinnen van waardevolle grondstoffen uit afvalstromen
-	het stimuleren van innovatieve technologie en nieuwe businessmodellen

Projecten richten zich vaak op het demonstreren en opschalen van innovaties die al in pilots zijn getest en klaar zijn voor verdere toepassing in de markt.

****2. Relevantie meubelbranche**** 
Voor de meubelbranche biedt EFRO kansen om circulaire innovaties te realiseren, zoals:
-	**Circulaire product- en procesontwikkeling**: Ontwerpen van meubels en bijbehorende processen die tot eenvoudig hergebruik, reparatie of recyclen leiden.
-	**Duurzame materialen**: Vervanging van fossiele materialen door duurzame alternatieven, zoals bamboecomposiet of gerecycled textiel.
-	**Hergebruik van reststromen**: Ontwikkeling van processen om grondstoffen uit afval- en reststromen te winnen, zoals houtresten of textielafval.
-	**Fieldlabs en demonstratieprojecten**: Ondersteuning bij het opzetten van pilotprojecten voor circulaire meubelproductie.
            
****3. Samenwerkingsprojecten****
Het EFRO moedigt samenwerking aan, maar individuele bedrijven kunnen ook subsidie aanvragen. Voor grotere projecten is een samenwerkingsverband met andere bedrijven, kennisinstellingen of overheden vaak vereist. Dit verhoogt de kans op toekenning en vergroot de impact van het project.     

****4. Externe links****
[Europees Fonds voor Regionale Ontwikkeling (EFRO) - Rijksoverheid](https://www.rijksoverheid.nl/onderwerpen/europese-subsidies/europese-structuur--en-investeringsfondsen/europees-fonds-voor-regionale-ontwikkeling-efro)
[EFRO-subsidies - ERAC](https://www.erac.nl/soorten-subsidies/efro/)
[EFRO-programma 2021-2027 - SNN](https://www.snn.nl/programmas/efro-2021-2027#efro-programma-2021-2027)
[Kansen voor West – Europese Unie](https://www.kansenvoorwest.nl/)
      
''')