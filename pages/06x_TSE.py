import streamlit as st
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="TSE", layout="wide")
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

st.title('TSE Industrie - Studies')
st.subheader('*Topsector Energie Industrie - Studies*')

st.page_link("pages/06_subsidies.py", label="⬅ Terug naar Subsidies")

html = generate_table("Verkenning", "€25K-€4M",  "Individueel óf<br>samenwerking")
st.markdown(html, unsafe_allow_html=True)

st.markdown("""
****1. Beschrijving subsidie****
De Topsector Industrie Studies is een subsidieregeling voor bedrijven die hun productie willen verduurzamen en minder CO₂ willen uitstoten. Het gaat hierbij om vooronderzoek: je krijgt geld om eerst te onderzoeken of en hoe een duurzaam idee technisch en financieel haalbaar is, voordat je investeert in nieuwe machines of processen.Er zijn drie typen studies waarvoor aangevraagd kan worden:

1.	**Haalbaarheidsstudie** - Je onderzoekt of een idee haalbaar is. Denk aan: kan een nieuwe, schonere productielijn werken in jouw fabriek? Wat kost het? Wat levert het op?
2.	**Milieustudie** - Je onderzoekt welke milieumaatregelen nodig zijn om een nieuwe techniek of productieproces in te voeren. Bijvoorbeeld: wat heb je nodig om te werken met een CO₂-arme droger, pers, lakstraat of warmtetechniek?

****2. Relevantie meubelbranche**** 
Bedrijven in de meubel- en interieursector horen bij de industrie als zij fysieke producten maken en grondstoffen verwerken. In dat geval kunnen zij gebruikmaken van de TSE Industrie studies wanneer hun project:
-	**Helpt om CO₂-uitstoot te verminderen in de productie**, bijvoorbeeld door schoner te werken, slimmer met materialen om te gaan of over te stappen op duurzame energie;
-	**Gericht is op technologische vernieuwing**, zoals circulaire ontwerpen, elektrificatie van machines, gebruik van hernieuwbare warmtebronnen of nieuwe duurzame chemische processen;
-	**In kaart brengt welke milieumaatregelen of investeringen nodig zijn** om de fabriek of werkplaats verder te verduurzamen.

Voorbeelden die passen bij de meubelindustrie zijn:
-	**Biobased en hergebruikte materialen**: onderzoeken naar het gebruik van biobased of circulaire materialen;
-	**Emissiereductie bij productietechnieken**: haalbaarheidsstudies naar productietechnieken met minder emissies;
-	**Ombouw machines**: studies naar elektrificatie van machines of het gebruik van groene waterstof;
-	**Energiezuinige productielijnen en logistiek**: onderzoeken naar nieuwe, energiezuinige productielijnen of verbeterde logistieke processen.

****3. Samenwerkingsprojecten****
Voor TSE-projecten is samenwerking geen vereiste. De subsidie kan worden aangevraagd door een individuele onderneming of door een samenwerkingsverband. 

In een samenwerkingsverband kunnen bedrijven samenwerken met andere ondernemingen en/of onderzoeksorganisaties. Gemeenten en provincies mogen meedoen als partner, maar kunnen zelf geen subsidie ontvangen.

****4. Externe links****
[TSE Industrie Studies – RVO.nl](https://www.rvo.nl/subsidies-financiering/tse-industrie-studies)
[Regeling Topsector Energie – (TSE)](https://www.topsectorenergie.nl/)

""")

