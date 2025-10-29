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

st.title('MIT - Haalbaarheid')
st.subheader('*MKB Innovatiestimulering Topsectoren - Haalbaarheidstrajecten*')

st.page_link("Home.py", label="⬅ Terug naar Home")

st.image('assets/MIT.jpg', width = 1000)

st.markdown('''
****1. Beschrijving subsidie****
           
De MIT Haalbaarheidssubsidie (Mkb-Innovatiestimulering Regio en Topsectoren) is een Nederlandse regeling bedoeld om mkb-ondernemers te helpen bij het verkennen van de haalbaarheid van een innovatieproject.

De subsidie ondersteunt bedrijven in de beginfase van innovatie, waarin nog onderzocht wordt of een idee technisch, economisch en organisatorisch uitvoerbaar is.

In deze fase kan het mkb marktonderzoek doen, technische analyses uitvoeren of de benodigde partners en grondstoffen in kaart brengen. De MIT Haalbaarheid is vaak een opstap naar een groter R&D-project of naar andere subsidie-instrumenten zoals MIT-R&D-samenwerkingsprojecten of Europese regelingen (zoals Horizon of ERDF).

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
