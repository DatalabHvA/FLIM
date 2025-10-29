import streamlit as st
from streamlit_plotly_events import plotly_events
import sys
sys.path.append("..")

st.set_page_config(page_title="Klantvraag", layout="wide")

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

st.title('Wet- en regelgeving')
st.page_link("Home.py", label="⬅ Terug naar Home")
st.write('Belangrijke wet- en regelgeving m.b.t. grondstoffen.')

# Sample content and row colors
labels1 = ['<b>Klein</b>','<50 medewerkers','<€10 miljoen','','','','','','','','','','']
labels2 = ['<b>Midden</b>','50-250 medewerkers','<€50 miljoen','EUDR [2025]','EUDR [2026]','Right to repair directive','Circulaire plastics norm (schuim en verpakkingen) [2027-2030]','REACH [2007]','<a href="/b_DPP", target = "_self"<u>DPP [2027]</u></a>','<a href="/a_UPV", target = "_self"<u>UPV [2029-2030]</u></a>','(indirect via keten)','(indirect via keten)','']
labels3 = ['<b>Groot</b>','>250 medewerkers of beursgenoteerd','>€50 miljoen','','','','','','','','CSRD [2026]','CSRD [2027]','CBAM/CO2 [2026]']
row_colors = [
    "#FFFFFF", "#FFFFFF", "#FFFFFF","#e60026", "#e65a41",
    "#eea896", "#f2d6c2", "#f7e9cd", "#fdeea3", "#f5dcb7",
    "#f9dd9e","#e0e0e0","#CFD6BB"
]

# Build HTML table
html = '<table style="width:100%;">'
for i in range(len(labels1)):
    bg = row_colors[i]
    label1 = labels1[i]
    label2 = labels2[i]
    label3 = labels3[i]
    html += f'<tr style="background-color:{bg};"> <td style="font-size: 16px; padding: 2px; text-align: center;">{label1}</td> <td style="font-size: 16px; padding: 2px; text-align: center">{label2}</td> <td style="font-size: 16px; padding: 2px; text-align: center">{label3}</td> </tr>'
html += '</table>'

# Render table in Streamlit
st.markdown(html, unsafe_allow_html=True)



c1, c2 = st.columns(2)
with c1:
    with st.container():
        st.subheader("Wet- en regelgeving: wat verandert er voor de meubelbranche?")
        st.markdown("""
                    
De Europese Unie zet met nieuwe wetgeving stevig in op een zuiniger en slimmer gebruik van grondstoffen. Hierdoor is het bewust omgaan met grondstoffen niet langer vrijblijvend, maar wordt het een **wettelijke verplichting**. 

Voor de meubelbranche betekent dit dat de manier waarop *producten worden ontworpen, geproduceerd en verwerkt* fundamenteel verandert .

Bedrijven moeten aantonen waar hun materialen vandaan komen, hoe producten zijn opgebouwd, hoe ze onderhouden of gerepareerd kunnen worden, en wat ermee gebeurt na gebruik.

***Samenhang wet- en regelgeving***
De Europese regelgeving verandert stap voor stap de manier waarop meubelmakers met hun producten en materialen om moeten gaan. De te ontwikkelen **Uitgebreide Producentenverantwoordelijkheid (UPV)** legt de basis: producenten blijven verantwoordelijk voor de inzameling, verwerking en recycling van hun meubels aan het einde van de levensduur. Dat vraagt om producten die makkelijker te demonteren, te hergebruiken of te recyclen zijn. 
Daarom stelt de **Ecodesign for Sustainable Products Regulation (ESPR)** eisen aan het ontwerp van meubels, gericht op een langere levensduur, betere repareerbaarheid en het gebruik van hernieuwbare of gerecyclede materialen. 
Om deze verbeteringen inzichtelijk te maken en informatie over materialen, onderhoud en recycling te kunnen delen, komt daarbovenop het **Digitaal Productpaspoort (DPP)**. Dit digitale systeem maakt het mogelijk om elke stap in de levenscyclus van een meubel te volgen en de oplossingen die onder ESPR zijn bedacht bekend te maken bij reparateur, consument en uiteindelijk de reststroomverwerker. 
Samen zorgen deze regelgevingen voor meer grip op grondstoffen- en productstromen binnen de EU, waarmee de meubelbranche beter kan sturen op toekomstbestendig materiaalgebruik en daarbij toekomstbestendig ondernemen.

Samen vormen deze wetten een systeem dat bedrijven verplicht om grip te krijgen op hun materiaalstromen en hun producten zó te ontwikkelen dat ze in de toekomst kunnen worden teruggenomen, hersteld of als grondstof opnieuw ingezet.
                """)

c1, c2 = st.columns(2)
with c1: 
    st.markdown("""
        **Risico's**
        
    Wie niet tijdig inspeelt op deze regels, loopt risico’s:                
        - Kostenbesparing: slimmer ontwerp en hergebruik verlagen materiaalkosten.
                - Nieuwe verdienmodellen: reparatie, leasing en retourstromen leveren langdurige klantrelaties op.
                - Concurrentievoordeel: aantoonbare circulariteit wordt een sterk verkoopargument in de veranderende klantvraag.
        - Toegang tot aanbestedingen en subsidies: overheden vragen om circulaire producten.
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

