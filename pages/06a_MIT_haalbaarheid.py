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
            
Voor de meubel- en interieurbranche is de MIT Haalbaarheid een kans om circulaire innovatieprojecten goed voor te bereiden.
De regeling helpt bedrijven bij het onderzoeken of een circulair product- of productie-idee technisch uitvoerbaar en economisch rendabel is. Denk aan:

- **Nieuwe circulaire productconcepten**: Onderzoeken of meubels ontworpen kunnen worden voor demontage, hergebruik of modulair onderhoud.
- **Biobased materialen**: Testen van de sterkte, kwaliteit en beschikbaarheid van alternatieve grondstoffen, zoals hennep, vlas, of gerecycled textiel.
- **Procesinnovatie**: Verkennen van mogelijkheden voor efficiënter materiaalgebruik, minder verspilling of energiezuinige productie.
- **Nieuwe businessmodellen**: Onderzoek naar haalbaarheid van terugname-, lease- of refurbished-concepten.            

Zo vormt de MIT Haalbaarheid vaak de eerste stap richting concrete circulaire productontwikkeling.

****3. Samenwerkingspojecten****
            
Hoewel de MIT Haalbaarheid bedoeld is voor individuele mkb-bedrijven, kan samenwerking met kennisinstellingen of ketenpartners (zoals toeleveranciers of ontwerpers) de aanvraag versterken.

Let op: voor grotere gezamenlijke innovatieprojecten is er de MIT R&D-Samenwerkingsprojectenregeling.

****4. Details van de subsidie****
            
|**Fase** | **Subsidie** | **Bedrag per aanvraag** | **Potgrootte** | **Looptijd regeling** | **Deadline (huidige ronde) aanvraag** | **Partij** |
| -------- | ------ | -------- | ------ | -------- | ------ | -------- |
| Verkenning  | MIT Haalbaarheid | Max €20.000 (tot 40% van de kosten) | €5 miljoen | Jaarlijks geopend | Per regio verschillende deadlines | Regionale ontwikkelings-maatschappijen |

****5. De aanvraag****
            
Over het algemeen volgt de aanvraagprocedure voor de MIT-subsidie de volgende stappen:

1. Voorbereiding: Breng de technische, economische en organisatorische haalbaarheid van het project in kaart.
2. Aanvraag indienen: Via het loket van de regionale uitvoeringsorganisatie (ROM's).
3. Beoordeling: De aanvragen worden beoordeeld op innovatiegehalte, haalbaarheid en verwachte economische impact
4. Toekenning en uitvoering: Na goedkeuring heeft de aanvrager maximaal één jaar om het haalbaarheidsonderzoek uit te voeren en te rapporteren.
           
****6. Externe links****
            
[MIT Haalbaarheid – RVO.nl](https://www.rvo.nl/subsidies-financiering/mit-haalbaarheid)
[MIT Haalbaarheidsprojecten – Provincie Zuid-Holland](https://www.zuid-holland.nl/online-regelen/subsidies/subsidies/mit-haalbaarheidsprojecten/)
[MIT R&D – Samenwerkingsprojecten – RVO.nl](https://www.rvo.nl/subsidies-financiering/mit-rd-samenwerkingsprojecten)
''')
