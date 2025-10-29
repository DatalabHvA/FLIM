import streamlit as st

st.set_page_config(page_title="Uitgebreide producentenverantwoordelijkheid (UPV)", layout="wide")

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

st.title('Uitgebreide producentenverantwoordelijkheid (UPV)')
st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en regelgeving")

st.markdown("""
    Uitgebreide producentenverantwoordelijkheid (UPV) maakt producenten (waaronder importeurs) verantwoordelijk voor het afvalbeheer van de producten die zij in Nederland in de handel brengen. Er zijn bijvoorbeeld verplichtingen voor het inzamelen en recyclen van afvalstoffen. Voor een groot aantal productgroepen is er al een UPV. 

  - **De rijksoverheid stelt als doel om in 2030 een UPV voor meubels in te stellen.** Deze moet eraan bijdragen dat meubels beter ingezameld, hergebruikt, opgeknapt, gerepareerd en gerecycled worden.

  **Relevantie voor de meubelbranche**
    De Uitgebreide Producentenverantwoordelijkheid (UPV) Meubels gaat grote impact hebben op de meubelbranche, omdat producenten verantwoordelijk gemaakt worden voor de inzameling en verwerking van hun producten aan het einde van de levensduur. 
    Dat betekent dat consumenten of bedrijven hun **oude meubels kosteloos kunnen afstaan**, dus zonder kosten voor logistiek of verwerking. Deze verantwoordelijkheid komt volledig te liggen bij de producenten. In eerste instantie leidt dit tot **hogere kosten voor producenten**, omdat zij moeten bijdragen aan het opzetten en financieren van inzamel- en verwerkingssystemen.

    Binnen de regeling wordt onder een producent niet alleen de fabrikant verstaan, maar ook **importeurs** en **wederverkopers** die meubels voor het eerst op de Nederlandse markt brengen. Ook zij dragen verantwoordelijkheid voor de producten die zij introduceren.
    
    De UPV Meubels stimuleert daarmee de hele keten (producent tot importeur) om na te denken over ontwerp voor hergebruik en demontage maar ook de materiaalkeuze, zodat producten aan het einde van hun levensduur makkelijker verwerkt en herbestemd kunnen worden. Uiteindelijk moet dit ertoe leiden dat de afvalstroom uit meubilair teruggedrongen wordt en en dat de waarde van materialen zoveel mogelijk behouden blijft.
            """)

c1, c2 = st.columns(2)
with c1: 
    st.markdown("""
        **Risico's**
                
        - **Hogere kosten**: Het opzetten van systemen om de eindverwerking en recycling van producten te organiseren kunnen in het begin leiden tot hogere operationele kosten.
        - **Verlies afzetmarkten**: Fabrikanten die niet in staat zijn om te voldoen aan de UPV-verplichtingen, kunnen het risico lopen hun producten uit bepaalde markten te verliezen, vooral in landen met strikte handhaving.
        - **Noodzaak voor vereniging**: De initiële verantwoordelijkheid voor de wettelijke regeling ligt bij individuele producenten, wat het organiseren en financieren van de eindverwerking van producten complex maakt, waardoor fabrikanten genoodzaakt zijn zich te verenigen om de verplichtingen gezamenlijk uit te voeren.
        """)
with c2: 
    st.markdown("""
        **Kansen**
                
        - **Tariefdifferentiatie** biedt een financiële prikkel voor duurzaam of circulair ontwerpen. Bijvoorbeeld: korting bij toepassing van +50% recycled content
        - Om te komen tot een goed werkend systeem wordt **samenwerking met ketenpartners** (producenten, retailers, inzamelaars, recyclers) belangrijk, dit biedt kansen voor nieuwe businessmodellen.
        - De UPV zal bijdragen aan betere inzameling van meubels en biedt kansen voor **hergebruik** en refurbishment. 
        - De UPV-wetgeving kan fabrikanten stimuleren om **innovatie in productontwikkeling** en nieuwe businessmodellen te omarmen, zoals product-as-a-service (verhuurmodellen) of circulaire productlijnen. Dit opent mogelijkheden voor het ontwikkelen van nieuwe producten met langere levenscycli.
        - Overheden en grote bedrijven stellen steeds vaker **duurzaamheidsvereisten in aanbestedingen**. Fabrikanten die proactief inspelen op de UPV-verplichtingen kunnen zich positioneren als duurzame pioniers, wat hen een concurrentievoordeel oplevert.
                
                """)

st.markdown('Meer informatie over Uitgebreide Producentenverantwoordelijkheid (UPV):    https://www.afvalcirculair.nl/uitgebreide-producentenverantwoordelijkheid-upv/') 
