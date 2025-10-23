import streamlit as st

st.set_page_config(page_title="MIT - Haalbaarheid", layout="wide")

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

st.page_link("Home.py", label="⬅ Terug naar Home")

st.image('assets/ERDF.PNG')

st.markdown('''
****1. Beschrijving subsidie****
           
Het European Regional Development Fund (ERDF) is een belangrijke Europese subsidieregeling die gericht is op het ondersteunen van regionale ontwikkeling en economische groei in Europa. Het ondersteunt samenwerkingsprojecten die bijdragen aan het versterken van de regionale economie, waaronder projecten in:
- de circulaire economie, 
- duurzame productie 
- en innovatie in verschillende sectoren. 
De regeling is in de basis gericht op minder ontwikkelde en overgangsregio's, maar bedrijven in heel Europa, inclusief Nederland, kunnen profiteren van de subsidiemogelijkheden. 

Binnen het kader van de circulaire economie biedt de ERDF subsidies voor projecten die gericht zijn op duurzame productontwikkeling, innovatie en hergebruik van materialen.

****2. Relevantie meubelbranche**** 
            
De ERDF is zeer relevant voor Nederlandse mkb-meubelmakers, omdat het hen de kans biedt om circulaire economie-initiatieven op te schalen, nieuwe duurzame productiemethoden te ontwikkelen en te investeren in innovatieve oplossingen voor materiaalhergebruik en recycling. Specifiek kunnen meubelbedrijven de ERDF-subsidie gebruiken voor de volgende projecten:
- **Circulaire productontwikkeling**: Het ontwikkelen van nieuwe meubelconcepten die circulair zijn, bijvoorbeeld meubels die eenvoudig gedemonteerd kunnen worden voor hergebruik van materialen.
- **Materialeninnovatie**: Het inzetten van innovatieve materialen (biobased of gerecycled materiaal) in meubelproductie.
- **Procesoptimalisatie**: Investeren in technologieën die de productieprocessen verduurzamen en afval verminderen, zoals het verbeteren van het recyclingproces of het sluiten van de materialenkringloop.
- **Lokaal hergebruik van materialen**: Het opzetten van terugname en refurbish systemen voor meubels, of het stimuleren van regionale samenwerking voor het hergebruik van materialen in de meubelindustrie.            

****3. Samenwerkingspojecten****
            
Voor veel ERDF-projecten is samenwerking een belangrijke vereiste. In veel gevallen is het noodzakelijk om samen te werken met andere bedrijven, kennisinstellingen, gemeenten, of onderzoeksorganisaties die expertise in de circulaire economie en duurzame productie kunnen leveren.

****4. Details van de subsidie****
            
|**Fase** | **Subsidie** | **Bedrag per aanvraag** | **Potgrootte** | **Looptijd regeling** | **Deadline (huidige ronde) aanvraag** | **Partij** |
| -------- | ------ | -------- | ------ | -------- | ------ | -------- |
| Implementatie  | ERDF - Circular Economy | Tussen €500.000 en €10 miljoen per consortium | €313 miljoen | 2021–2027 | Per regio (verschillende deadlines) | Regio afhankelijk |

****5. De aanvraag****
            
Over het algemeen volgt de aanvraagprocedure voor de ERDF-subsidie de volgende stappen:

1. Projectvoorstel indienen: Meubelmakers dienen een gedetailleerd projectvoorstel in waarin ze de doelen, resultaten, en begroting van het project beschrijven.
2. Beoordeling door de uitvoeringsinstantie: Het voorstel wordt beoordeeld door de regionale uitvoeringsinstantie, die bepaalt of het project in aanmerking komt voor subsidie.
3. Toekenning en uitbetaling: Indien goedgekeurd, wordt de subsidie verstrekt op basis van de goedgekeurde begroting en de afgesproken projectresultaten.

De deadlines voor aanvragen verschillen per regio. Er worden meestal jaarlijkse calls gehouden, dus het is belangrijk om goed op de hoogte te blijven van de regio-specifieke deadlines.
            
****6. Externe links****
            
[ERDF (website Europese Commissie)](https://ec.europa.eu/regional_policy/funding/erdf_en)
''')
