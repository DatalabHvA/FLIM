import streamlit as st
from streamlit_plotly_events import plotly_events
import sys
sys.path.append("..")
from widgets import *

ss = st.session_state


st.set_page_config(page_title="Wet- en regelgeving - Landingspagina", layout="wide")
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

if not ((ss.omzet_value == ">€50M") | (ss.medewerkers_value == "250+ fte")):
    st.subheader("Waar wordt de meubelbranche de komende jaren mee geconfronteerd?")
    st.markdown("""
De Europese Unie zet met nieuwe wetgeving stevig in op een zuiniger en slimmer gebruik van grondstoffen. 
Hierdoor is het bewust omgaan met grondstoffen niet langer vrijblijvend, maar wordt het een wettelijke verplichting.

_**De belangrijkste voor jouw organisatie zijn:**_ 

De Europese regelgeving verandert stap voor stap de manier waarop meubelmakers met hun producten en materialen om moeten gaan. De **Uitgebreide Producentenverantwoordelijkheid (UPV)** vormt daarbij de basis: producenten worden financieel verantwoordelijk voor de inzameling, verwerking en recycling van hun meubels aan het einde van de levensduur. Dat vraagt om producten die makkelijker te demonteren, te hergebruiken of te recyclen zijn.
De **Ecodesign for Sustainable Products Regulation (ESPR)** stelt daarnaast eisen aan hoe producten worden ontworpen, zoals een langere levensduur, betere repareerbaarheid en het gebruik van hernieuwbare of gerecyclede materialen. Om deze eigenschappen inzichtelijk te maken komt daarbovenop het **Digitaal Productpaspoort (DPP)**. Hierin leggen producenten informatie vast over materialen, onderhoud en recyclingmogelijkheden. Zo kan de volledige levenscyclus van een meubel inzichtelijk worden gemaakt voor reparateurs, consumenten en verwerkers.
Andere regels richten zich op de grondstoffen en ketens achter het product. De **EU-verordening ontbossingsvrije producten (EUDR)** verplicht bedrijven om aan te tonen dat grondstoffen zoals hout niet afkomstig zijn van recent ontboste gebieden. Dit vraagt om meer inzicht in de herkomst van materialen en transparantie in de toeleveringsketen.
Deze inzichten worden vervolgens steeds belangrijker in duurzaamheidsrapportages. Via de **Corporate Sustainability Reporting Directive (CSRD)** moeten grote bedrijven rapporteren over hun CO₂-uitstoot, grondstoffengebruik en ketenimpact. Veel MKB-bedrijven krijgen hier indirect mee te maken doordat klanten of financiers deze informatie opvragen. De **VSME-standaard** helpt kleinere bedrijven om deze gegevens gestructureerd te verzamelen en te delen.
Samen vormen deze wetten een systeem dat bedrijven gaat **verplichten om bewust om te gaan met- en grip te krijgen op hun materiaalstromen** en hun producten zo te ontwikkelen dat ze in de toekomst kunnen worden teruggenomen, hersteld of als grondstof opnieuw ingezet.

                """, unsafe_allow_html = True)
    c1, c2 = st.columns(2)
    with c1: 
        st.subheader("KANSEN")
        st.markdown("""
Voor bedrijven die nu al voorsorteren, liggen grote voordelen:
-	**Nieuwe verdienmodellen**: reparatie, leasing en retourstromen leveren langdurige klantbinding en -relaties op.
-	**Kostenbesparing**: slimmer ontwerp en hergebruik verlagen materiaalkosten.
-	**Concurrentievoordeel**: aantoonbare circulariteit wordt een sterk verkoopargument in de toekomstige markt.
-	**Toegang tot aanbestedingen en subsidies**: overheden vragen steeds meer om circulaire producten, circulair aanbod biedt toegang tot een grote klantgroep. 
                    """)
    with c2: 
        st.subheader("RISICO’S")
        st.markdown("""
Wie niet tijdig inspeelt op deze regels, loopt risico’s:
-	**Marktuitsluiting**: producten die niet voldoen, mogen in de toekomst niet meer verkocht worden.
-	**Kostenstijging**: late aanpassing leidt tot hogere grondstof- en nalevingskosten.
-	**Datadruk**: nieuwe eisen vragen om transparantie in de hele keten – van leverancier tot eindgebruiker.
-	**Verlies aan concurrentiekracht**: bedrijven die niet voldoen, verliezen terrein aan spelers die wel voldoen en hun circulaire waarde kunnen aantonen.
-	**Verlies van ketenpartners**: Gebrek aan transparantie en inzicht verlaagt de incentive voor rapportageplichtige bedrijven om met je samen te werken

                    """)
    st.subheader("FINANCIËLE RISICO’S")
    with st.container(border = True):
        v1, v2, v3 = st.columns(3)
        v1.markdown("**Boetes, sancties & handhavingskosten**")
        v2.markdown("**Markttoegang verliezen / productverboden**")
        v3.markdown("**Ketenrisico’s**")

        b1, b2, b3 = st.columns(3)
        b1.markdown("Directe financiële consequenties vanuit toezichthouders.")
        b2.markdown("Producten mogen niet in de EU worden ingevoerd of verkocht.")
        b3.markdown("Non-compliance veroorzaakt schadeclaims door klanten, retailers, financiers of afnemers.")
        st.markdown("---")
        n1, n2, n3 = st.columns(3)
        n1.markdown("Naheffingen bij verkeerde rapportage. ")
        n1.page_link("pages/04x_CBAM.py", label = "CBAM", icon="➡") 
        n1.markdown("Forse boetes (tot 4% van omzet), inbeslagname goederen, exportstop.")
        n1.page_link("pages/04x_EUDR.py", label = "EUDR", icon="➡") 
        n1.markdown("Boetes bij schending ecodesign- en duurzaamheidseisen; productverboden. ")
        n1.page_link("pages/04x_ESPR.py", label = "ESPR", icon="➡") 
        n1.markdown("Sancties bij niet naleven reparatieplicht / informatieplicht.  ")
        n1.page_link("https://commission.europa.eu/law/law-topic/consumer-protection-law/directive-repair-goods_en", label = "Right to repair", icon="➡") 
        n1.markdown("Hoge boetes, stillegging productie, recall-opdrachten. ")
        n1.page_link("https://ondernemersplein.overheid.nl/wetten-en-regels/verplichtingen-bij-chemische-stoffen-reach/", label = "REACH", icon="➡") 
        n1.markdown("Boetes bij onvolledige of foutieve digitale productpaspoorten. ")
        n1.page_link("pages/04x_DPP.py", label = "DPP", icon="➡") 
        n1.markdown("Boetes bij onderbetaling of onderregistratie van producenten-verantwoordelijkheid. ")
        n1.page_link("pages/04x_UPV.py", label = "UPV", icon="➡") 

        n2.markdown("Import zonder correcte CO₂-verklaring kan worden tegengehouden. ")
        n2.page_link("pages/04x_CBAM.py", label = "CBAM", icon="➡") 
        n2.markdown("Blokkade van grondstoffen/halffabricaten (risicogrondstoffen). ")
        n2.page_link("pages/04x_EUDR.py", label = "EUDR", icon="➡") 
        n2.markdown("Producten zonder vereiste ecodesign- of circulariteitswaarden kunnen worden geweerd.")
        n2.page_link("pages/04x_ESPR.py", label = "ESPR", icon="➡")
        n2.markdown("Niet-conforme verpakkingen en schuimen mogen worden verboden. ")
        n2.page_link("https://www.internetconsultatie.nl/nationale_circulaire_plastic_norm/b1#sectie-consultatiegegevens", label = "Circulaire plastics norm", icon="➡")
        n2.markdown("Verboden stoffen maken producten onverkoopbaar.")
        n2.page_link("https://ondernemersplein.overheid.nl/wetten-en-regels/verplichtingen-bij-chemische-stoffen-reach/", label = "REACH", icon="➡") 
        n2.markdown("Producten zonder geldige paspoorten worden geweigerd.")
        n2.page_link("pages/04x_DPP.py", label = "DPP", icon="➡") 

        n3.markdown("Retailers/merken kunnen claims indienen als ketenonderbouwing niet klopt. ")
        n3.page_link("pages/04x_EUDR.py", label = "EUDR", icon="➡") 
        n3.markdown("OEM’s kunnen leveranciers aansprakelijk stellen voor ontbrekende conformiteit. ")
        n3.page_link("pages/04x_ESPR.py", label = "ESPR", icon="➡")
        n3.markdown("Incorrecte productdata → aansprakelijkheid voor misleidende informatie")
        n3.page_link("pages/04x_DPP.py", label = "DPP", icon="➡")
        n3.markdown("Kosten en claims voor non-compliance van producenten. ")
        n3.page_link("pages/04x_UPV.py", label = "UPV", icon="➡") 
        n3.markdown("Contractuele verplichtingen bedrijven aan leveranciers (data quality, emissie-info). Niet leveren = contractbreuk. ")
        n3.page_link("pages/04x_VSME.py", label = "CSRD, bij MKB via VSME", icon="➡") 

    st.page_link("pages/04x_tabel.py", label = "_**Klik hier voor een volledig overzicht van relevante wet- en regelgeving**_")

else: 
    st.title('Andere titel')
