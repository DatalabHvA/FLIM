import streamlit as st

st.set_page_config(page_title="CKP", layout="wide")
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

st.title('CKP-subsidie')
st.subheader('*Subsidie Circulaire Ketenprojecten*')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")


html = generate_table("Implementatie", "€20K per ondernemer in de keten",  "Samenwerking")
st.markdown(html, unsafe_allow_html=True)

st.markdown('''
****1. Beschrijving subsidie****
           
Subsidies zoals de Circulaire Ketenprojecten subsidie ondersteunen mkb-ondernemers en grootbedrijven die samenwerken om een circulaire keten te realiseren. De subsidie bevordert de ontwikkeling van duurzame producten, processen en diensten die grondstoffen besparen en CO₂-uitstoot reduceren. Door grondstofketens te sluiten en samen te werken aan circulair ontwerp, productie en logistiek.

****2. Relevantie meubelbranche**** 
Voor de meubelindustrie bieden samenwerkingssubsidies zoals de CKP kansen om:
-	**Ketenintegratie** te realiseren tussen producenten, leveranciers, verwerkers, en recyclers.
-	**Circulair ontwerp** van meubels te bevorderen, waarbij gerecycled materiaal en herbruikbare onderdelen centraal staan.
-	**Procesoptimalisatie** te stimuleren door gesloten kringlopen voor meubilair te creëren.
-	**Grondstoffen te besparen** door circulaire service- en productontwikkeling en materiaalinnovatie.
    

****3. Samenwerkingsprojecten****
Om in aanmerking te komen voor specifiek deze subsidie, is samenwerking met andere mkb-ondernemers of grootbedrijven nodig. Ten minste 3 schakels in de keten, zoals grondstoffenleveranciers, producenten en verwerkers. Voordeel is dat hiermee ook de risico’s van implementatie verdeeld wordt over de deelnemers in het samenwerkingsverband.   

****4. Externe links****
[CKP Subsidie - RVO](https://www.rvo.nl/subsidies-financiering/circulaire-ketenprojecten)
''')