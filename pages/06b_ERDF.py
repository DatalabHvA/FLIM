import streamlit as st

st.set_page_config(page_title="ERDF", layout="wide")

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

st.title('ERDF: Circular Economy')
st.subheader('(European Regional Development Fund for Circular Economy)')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")

st.image('assets/ERDF.jpg', width = 1000)

st.markdown('''
****1. Beschrijving subsidie****
           
Het European Regional Development Fund (ERDF) is een Europese subsidieregeling die gericht is op het ondersteunen van regionale ontwikkeling en economische groei in Europa. Het ondersteunt samenwerkingsprojecten die bijdragen aan het versterken van de regionale economie. Binnen het kader van de circulaire economie biedt de ERDF subsidies voor projecten die gericht zijn op duurzame productontwikkeling, innovatie en hergebruik van materialen.

De regeling is in de basis gericht op minder ontwikkelde en overgangsregio's, maar bedrijven in heel Europa, inclusief Nederland, kunnen ook gebruik maken van de subsidiemogelijkheden.

****2. Relevantie meubelbranche**** 
            
Subsidies zoals de ERDF zijn relevant voor Nederlandse mkb-meubelmakers omdat het hen de kans biedt om circulaire economie-initiatieven op te schalen. Specifiek kunnen meubelbedrijven de ERDF-subsidie gebruiken voor de volgende projecten:
- **Circulaire productontwikkeling**: Het ontwikkelen van nieuwe meubelconcepten die circulair zijn, bijvoorbeeld meubels die eenvoudig gedemonteerd kunnen worden voor hergebruik van materialen.
- **Materialeninnovatie**: Het inzetten van innovatieve materialen (biobased of gerecycled materiaal) in meubelproductie.
- **Procesoptimalisatie**: Investeren in technologieën die de productieprocessen verduurzamen en afval verminderen, zoals het verbeteren van het recyclingproces of het sluiten van de materialenkringloop.
- **Lokaal hergebruik van materialen**: Het opzetten van terugname en refurbish systemen voor meubels, of het stimuleren van regionale samenwerking voor het hergebruik van materialen in de meubelindustrie.            

****3. Samenwerkingspojecten****
            
Voor veel ERDF-projecten is samenwerking een belangrijke vereiste. In veel gevallen is het noodzakelijk om samen te werken met andere bedrijven, kennisinstellingen, gemeenten, of onderzoeksorganisaties die expertise in de circulaire economie en duurzame productie kunnen leveren.

****4. Externe links****
            
[ERDF (website Europese Commissie)](https://ec.europa.eu/regional_policy/funding/erdf_en)
''')