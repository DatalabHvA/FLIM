import streamlit as st

st.set_page_config(page_title="DPP", layout="wide")

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

st.title('DPP')
st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en regelgeving")

st.markdown("""
    **Wat is het DPP?** 
            
    Een digitaal productpaspoort (DPP) is een ‘tag’ (zoals een QR-code) op een product, die gescand kan worden en informatie geeft over de duurzaamheid van een product. 

    Alternatief:
            
    Een Digitaal Product Paspoort (DPP) is een gestandaardiseerd digitaal document dat uitgebreide informatie bevat over de samenstelling, productie, gebruik en recycling van een product.

    De toekomstige wetgeving verplicht bedrijven om voor meubels een digitaal paspoort aan te leveren. 
    Het DPP moet:
    - Transparantie in productketens vergroten
    - Hergebruik, reparatie en recycling bevorderen
    - Consumenten én zakelijke afnemers helpen duurzame keuzes te maken
    - Handhaving door toezichthouders vereenvoudigen

    Verwachte invoering voor de meubelbranche: vanaf 2026. 
            
    Het Digitaal Productpaspoort (DPP) is onderdeel van de Europese Ecodesign for Sustainable Products Regulation (ESPR).

    **Relevantie voor jouw meubelbranche**
 
    De invoering van het Digitaal Productpaspoort is een systeemverandering in hoe je omgaat met productinformatie. Het DPP legt een verplichting op tot structurele dataregistratie en transparantie over de hele keten. Klanten, toezichthouders en afnemers willen weten wat erin zit, waar het vandaan komt, en hoe het weer uit elkaar kan.  
            
    Een stoel wordt geen product, maar een data-object met levenscyclusinformatie. Bijvoorbeeld:
    - Ontwerper: moet ontwerpen met demontage en registratie in gedachten
    - Inkoop: moet materiaaldata opvragen én vastleggen
    - Sales: kan duurzaamheid onderbouwen met objectieve info
    - Serviceafdeling: gebruikt DPP bij onderhoud, reparatie of retour

    **Belangrijke risico’s en kansen in de UPV**
            
""")
c1, c2 = st.columns(2)
with c1:
    st.markdown("""
        **Risico's**
                
        - De meubelbranche kent een grote variëteit aan materialen (hout, schuim, metaal, textiel), wat het vastleggen en beheren van productinformatie complex maakt.
        - Niet-naleving leidt tot marktuitsluiting (o.a. binnen aanbestedingen)
        - Hoge implementatiekosten voor MKB-bedrijven zonder datastandaarden
        - Afhankelijkheid van leveranciers voor correcte materiaaldata
        - Digitale infrastructuur ontbreekt vaak nog
    """)
with c2: 
    st.markdown("""
        **Kansen**

        - DPP is de sleutel tot markttoegang, subsidievoorwaarden, aanbestedingen én risicobeheersing bij CSRD-verantwoording.
        - Toegang tot duurzame markten en klanten (B2B en overheid)
        - Marktvoordeel bij early adopters: transparantie als onderscheidende factor
        - Restwaarde kan beter worden bepaald, dit versterkt circulaire verdienmodellen
        """)
    
st.markdown("""
    **Externe links**
            
    https://www.tno.nl/nl/digitaal/data-sharing/digitaal-product-paspoort/ 
    """)            
