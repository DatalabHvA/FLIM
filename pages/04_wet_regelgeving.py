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
        st.subheader("Samenhang en doel wet- en regelgevingen")
        st.markdown("""
        **1. Wet- en regelgeving: wat verandert er voor de meubelbranche?** 
                    
De Europese Unie zet met nieuwe wetgeving stevig in op een zuiniger en slimmer gebruik van grondstoffen. Hierdoor is het bewust omgaan met grondstoffen niet langer vrijblijvend, maar wordt het een wettelijke verplichting. 
Voor de meubelbranche betekent dit dat de manier waarop producten worden ontworpen, geproduceerd en verwerkt fundamenteel verandert .
Bedrijven moeten aantonen waar hun materialen vandaan komen, hoe producten zijn opgebouwd, hoe ze onderhouden of gerepareerd kunnen worden, en wat ermee gebeurt na gebruik.


Niet langer is circulariteit vrijblijvend of alleen “maatschappelijk wenselijk” – het wordt wettelijk verplichtend, met eisen over ontwerp, materialen, hergebruik en afvalfase.**

        - Producttransparantie via het Digitaal Productpaspoort (DPP)
        - Verschuiving van verantwoordelijkheid naar producenten (UPV)
            
        **2. Greenwashing tegengaan en speelveld gelijk maken**
                    
        Door het gebrek aan een uniforme standaard in Nederland kunnen bedrijven ongefundeerde duurzaamheidsclaims maken. Nieuwe wetgeving moet dit tegengaan en een gelijk speelveld creëren voor Nederlandse producenten. 
                    
        **3. Financiële risico's voor niet-actieve bedrijven**
                    
        Het niet tijdig inspelen op deze wetgeving heeft financiële risico's. Denk aan:
        - Kosten van non-compliance.
        - Geen toegang tot markten die circulariteit vereisen.
        - Verlies aan concurrentiekracht t.o.v. bedrijven die wél voldoen
                """)

st.subheader("Wat betekent dit voor de branche?")
st.markdown("""
    - **MKB-bedrijven** moeten anticiperen op verplichtingen met hulp van tools (zoals FLIM).
    - **Ketenregie** wordt cruciaal: de informatie- en materiaalstromen moeten traceerbaar worden.
    - **Collectieve actie** (via brancheverenigingen zoals CBM) wordt noodzakelijk om de regeldruk behapbaar te maken.
    - **Compliance = concurrentiekracht** – bedrijven die voorbereid zijn, worden aantrekkelijker voor investeerders, klanten en partners.    
    """)    


