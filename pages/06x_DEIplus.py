import streamlit as st

st.set_page_config(page_title="DEI+", layout="wide")
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

st.title('DEI+ - Circulaire Economie')
st.subheader('*Demonstratie Energie- en Klimaatinnovatie: Circulaire economie*')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")


html = generate_table("Ontwikkeling", "€50K-€350K (20%)",  "Samenwerking")
st.markdown(html, unsafe_allow_html=True)

st.markdown('''
****1. Beschrijving subsidie****

De DEI+ Circulaire Economie-subsidie ondersteunt bedrijven die innovaties die bijdragen aan de circulaire economie willen testen of demonstreren, ofwel demonstratieprojecten. De focus ligt op projecten die het gebruik van grondstoffen optimaliseren, afval verminderen, en CO₂-uitstoot reduceren. Innovaties kunnen betrekking hebben op het hergebruik van materialen, circulair ontwerp, of procesoptimalisatie.

****2. Relevantie meubelbranche**** 
            
Voor de meubelindustrie biedt de DEI+ subsidie de mogelijkheid om:
-	**Circulair ontwerp** te implementeren, zoals modulaire meubels die eenvoudig te hergebruiken of recyclen zijn.
-	**Grondstoffen te besparen** door innovatieve productieprocessen of secundaire materialen toe te passen.
-	**Afval te reduceren** door het verbeteren van scheiden en hergebruik dan wel recycling van materialen in de meubelproductie

****3. Samenwerkingsprojecten****
            
Om in aanmerking te komen voor de DEI+ Circulaire Economie-subsidie, is samenwerking met andere bedrijven, kennisinstellingen of overheden vereist. Het project moet minimaal twee onafhankelijke partijen omvatten, zoals leveranciers, producenten, verwerkers of recyclers. Samenwerking helpt om de risico’s en kosten van innovatie te verdelen en verhoogt de kans op succesvolle implementatie.

****4. Externe links****
[DEI+ - Circulaire Economie – RVO.nl](https://www.rvo.nl/subsidies-financiering/dei/circulaire-economie)            
''')