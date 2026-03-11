import streamlit as st
from streamlit_plotly_events import plotly_events
import sys
sys.path.append("..")
from widgets import *

ss = st.session_state


st.set_page_config(page_title="Klantvraag", layout="wide")
st.markdown(
    """
    <style>
      /* pull content up */
      .block-container { padding-top: 0.9rem !important; }
      /* compact header */
      header[data-testid="stHeader"] { height: 1.2rem; }
      [data-testid="stSidebarNav"] {display: none;}
      [data-testid="stSidebar"] .block-container {
          padding-top: 0 !important;
      }

    section[data-testid="stSidebar"] .block-container > div:first-child,
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] > div:first-child {
    margin-top: -60px !important;   /* <- adjust this number */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.page_link("Home.py", label="⬅ Terug naar Home")

    st.header("Filters")
    widget_omzet()
    widget_klantsegment()

st.title('Wet- en regelgeving')

# Sample content and row colors
labels1 = ['<b>Klein</b>','<50 medewerkers','<€10 miljoen','','','','','','','','','','']
labels2 = ['<b>Midden</b>','50-250 medewerkers','<€50 miljoen','EUDR [2025]','ESPR [2026]','Right to repair directive','Circulaire plastics norm (schuim en verpakkingen) [2027-2030]','REACH [2007]','<a href="/b_DPP", target = "_self"<u>DPP [2027]</u></a>','<a href="/a_UPV", target = "_self"<u>UPV [2029-2030]</u></a>','(indirect via keten)','(indirect via keten)','']
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

with st.container():
    st.subheader("Wet- en regelgeving: wat verandert er voor de meubelbranche?")
    st.markdown("""
    De Europese Unie zet met nieuwe wetgeving stevig in op een **zuiniger en slimmer gebruik van grondstoffen**. Hierdoor is het bewust omgaan met grondstoffen niet langer vrijblijvend, maar wordt het een wettelijke verplichting.

Voor de meubelbranche betekent dit dat de manier waarop producten ontworpen, geproduceerd en verwerkt worden fundamenteel gaat veranderen. 
                
Bedrijven moeten aantonen waar hun materialen vandaan komen, hoe producten zijn opgebouwd, hoe ze onderhouden of gerepareerd kunnen worden, en wat ermee gebeurt na gebruik.
-	**Ecodesign for Sustainable Products Regulation (ESPR)**: stelt eisen aan ontwerp, repareerbaarheid, levensduur en het gebruik van hernieuwbare of gerecyclede materialen.
-	**Digitaal Productpaspoort (DPP)**: verplicht producenten om productinformatie digitaal vast te leggen en te delen met klanten, leveranciers en recyclers.
-	**Uitgebreide Producentenverantwoordelijkheid (UPV)**: maakt fabrikanten verantwoordelijk voor de inzameling, verwerking en recycling van hun producten aan het einde van de levensduur.
Samen vormen deze wetten een systeem dat bedrijven **verplicht om grip te krijgen op hun materiaalstromen** en hun producten zó te ontwikkelen dat ze in de toekomst kunnen worden teruggenomen, hersteld of als grondstof opnieuw ingezet.

De Europese regelgeving verandert stap voor stap de manier waarop meubelmakers met hun producten en materialen om moeten gaan. De te ontwikkelen **Uitgebreide Producentenverantwoordelijkheid (UPV)** legt de basis: producenten blijven verantwoordelijk voor de inzameling, verwerking en recycling van hun meubels aan het einde van de levensduur. Dat vraagt om producten die makkelijker te demonteren, te hergebruiken of te recyclen zijn. Daarom stelt de **Ecodesign for Sustainable Products Regulation (ESPR)** eisen aan het ontwerp van meubels, gericht op een langere levensduur, betere repareerbaarheid en het gebruik van hernieuwbare of gerecyclede materialen. Om deze verbeteringen inzichtelijk te maken en informatie over materialen, onderhoud en recycling te kunnen delen, komt daarbovenop het **Digitaal Productpaspoort (DPP)**. Dit digitale systeem maakt het mogelijk om elke stap in de levenscyclus van een meubel te volgen en de oplossingen die onder ESPR zijn bedacht bekend te maken bij reparateur, consument en uiteindelijk de reststroomverwerker. Samen zorgen deze regelgevingen voor meer grip op grondstoffen- en productstromen binnen de EU, waarmee de meubelbranche beter kan sturen op toekomstbestendig materiaalgebruik en daarbij toekomstbestendig ondernemen.

            """)

c1, c2 = st.columns(2)
with c1: 
    st.subheader("KANSEN")
    st.markdown("""          
Voor bedrijven die nu al voorsorteren, liggen grote voordelen:
-	**Kostenbesparing**: slimmer ontwerp en hergebruik verlagen materiaalkosten.
-	**Nieuwe verdienmodellen**: reparatie, leasing en retourstromen leveren langdurige klantrelaties op.
-	**Concurrentievoordeel**: aantoonbare circulariteit wordt een sterk verkoopargument in de veranderende klantvraag.
-	**Toegang tot aanbestedingen en subsidies**: overheden vragen om circulaire producten.
        """)
with c2: 
    st.subheader("RISICO’S")
    st.markdown("""         
Wie niet tijdig inspeelt op deze regels, loopt risico’s:
-	**Marktuitsluiting**: producten die niet voldoen, mogen in de toekomst niet meer verkocht worden.
-	**Kostenstijging**: late aanpassing leidt tot hogere grondstof- en nalevingskosten.
-	**Datadruk**: nieuwe eisen vragen om transparantie in de hele keten – van leverancier tot eindgebruiker.
-	**Verlies aan concurrentiekracht**: bedrijven die niet voldoen, verliezen terrein aan spelers die wel voldoen en hun circulaire waarde kunnen aantonen.

                """)

st.subheader('FINANCIËLE RISICO’S')
st.markdown("""
| **Boetes, sancties & handhavingskosten** | **Markttoegang verliezen / productverboden** | **Ketenrisico’s** |
|---|---|---|
| *Directe financiële consequenties vanuit toezichthouders.* | *Producten mogen niet in de EU worden ingevoerd of verkocht.* | *Non-compliance veroorzaakt schadeclaims door klanten, retailers, financiers of afnemers.* |            
| EUDR (2025) – forse boetes (tot 4% van omzet), inbeslagname goederen, exportstop.<br><br>ESPR (2026) – boetes bij schending ecodesign- en duurzaamheidseisen; productverboden.<br><br>Right to Repair – sancties bij niet naleven reparatieplicht / informatieplicht.<br><br>Circulaire plastics norm (2027–2030) – boetes voor niet halen van recyclaat- en ontwerpnormen.<br><br>REACH – hoge boetes, stillegging productie, recall-opdrachten.<br><br>DPP – boetes bij onvolledige of foutieve digitale productpaspoorten.<br><br>UPV – boetes bij onderbetaling of onderregistratie van producentenverantwoordelijkheid.<br><br>CBAM/CO₂ (2026) – naheffingen bij verkeerde rapportage. | EUDR – blokkade van grondstoffen/halffabricaten (risicogrondstoffen).<br><br>ESPR – producten zonder vereiste ecodesign- of circulariteitswaarden kunnen worden geweerd.<br><br>Circulaire plastics norm – niet-conforme verpakkingen en schuimen mogen worden verboden.<br><br>REACH – verboden stoffen maken producten onverkoopbaar.<br><br>DPP – producten zonder geldige paspoorten worden geweigerd.<br><br>CBAM – import zonder correcte CO₂-verklaring kan worden tegengehouden. | EUDR – retailers/merken kunnen claims indienen als ketenonderbouwing niet klopt.<br><br>ESPR – OEM’s kunnen leveranciers aansprakelijk stellen voor ontbrekende conformiteit.<br><br>DPP – incorrecte productdata → aansprakelijkheid voor misleidende informatie.<br><br>UPV / plastics norm – kosten en claims voor verpakkings-non-compliance door brand-owners.<br>CSRD (2026/2027, indirect) – bedrijven leggen contractueel verplichtingen op aan leveranciers (data quality, emissie-info). Niet leveren = contractbreuk. |
""", unsafe_allow_html = True)

st.subheader("Wat betekent dit voor de branche?")

st.markdown("""
-	**MKB-bedrijven** moeten anticiperen op verplichtingen met hulp van tools (zoals FLIM).
-	**Ketenregie** wordt cruciaal: de informatie- en materiaalstromen moeten traceerbaar worden.
-	**Collectieve actie** (via brancheverenigingen zoals CBM) wordt noodzakelijk om de regeldruk behapbaar te maken.
-	**Compliance = concurrentiekracht** – bedrijven die voorbereid zijn, worden aantrekkelijker voor investeerders, klanten en partners.
""")