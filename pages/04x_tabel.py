import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="Wet- en regelgevingsoverzicht", layout="wide")

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

    </style>
"""
st.markdown(hide_sidebar, unsafe_allow_html=True)

st.title("Overzicht wet- en regelgeving")
st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en Regelgeving")

st.markdown("""
| Naam | Van toepassing op | Per wanneer |
|-----|-------------------|-------------|
| [**CBAM – Carbon Border Adjustment Mechanism**](https://www.douane.nl/onderwerpen/vgem/milieu/cbam/) | - EU-bedrijven die koolstofintensieve producten importeren (o.a. staal, aluminium)<br>- Producenten buiten de EU die aan de EU leveren<br>- Indirect relevant voor meubelfabrikanten die staal/aluminium inkopen | Transitieperiode sinds okt 2023 (rapportageplicht)<br>Financiële verplichting vanaf 2026 |
| [**Circulaire Plastics Norm (schuim en verpakkingen)**](https://www.internetconsultatie.nl/nationale_circulaire_plastic_norm/b1#sectie-consultatiegegevens) | - Producenten en verwerkers van polymeren<br>- Meubelfabrikanten die schuim, kunststoffen of verpakkingsmaterialen toepassen | Vanaf 2027 (gefaseerde invoering) |
| [**Corporate Sustainability Reporting Directive (CSRD)**](https://www.rvo.nl/onderwerpen/csrd) | - Grote ondernemingen (>250 medewerkers)<br>- Beursgenoteerd MKB | Grote bedrijven (>250 werknemers): rapportageplichtig 2025<br>MKB (beursgenoteerd): rapportageplichtig in 2026 |
| [**Corporate Sustainability Reporting Directive (CSRD)***](https://www.rvo.nl/onderwerpen/csrd) | - MKB-bedrijven in de keten van CSRD-plichtige bedrijven | MKB bedrijven kunnen door CSRD-plichtige afnemers worden gevraagd om informatie voor CSRD. Hiervoor is inzicht nodig in de thema’s van CSRD. Bijvoorbeeld CO₂-emissies van producten (scope 3 ketenemissies). Zie ook VSME-richtlijn. |
| [**Voluntary Sustainability Reporting Standard for SMEs (VSME)**](https://www.rvo.nl/onderwerpen/vsme) | MKB-bedrijven die niet onder de CSRD vallen maar wel duurzaamheidsinformatie moeten aanleveren aan klanten, banken of ketenpartners | Vrijwillige standaard gepubliceerd in 2024; bedoeld om MKB te helpen gestructureerd duurzaamheidsinformatie te verzamelen en te delen, vaak als voorbereiding op vragen vanuit CSRD-plichtige bedrijven. |
| [**ESPR – Ecodesign for Sustainable Products Regulation**](https://afvalcirculair.nl/circulair-ontwerp/espr/) | Fabrikanten, importeurs en distributeurs van producten die op de EU-markt worden gebracht (incl. meubels en bouwmaterialen) | In werking sinds 18 juli 2024; implementatie gefaseerd via productgroepmaatregelen in de jaren erna (veel impact verwacht vanaf 2026 bij uitrol eerste productgroepen) |
| [**DPP – Digitaal Productpaspoort**](https://afvalcirculair.nl/circulair-ontwerp/digitaal-product-paspoort-dpp/) | Producten/verkopers; ook relevant voor reparateurs en circulaire verwerkers (reparatie/hergebruik/recycling) en consumenten | Framework nog in ontwikkeling; voor meerdere sectoren (incl. meubels) wordt verplichting vanaf 2027 genoemd |
| [**EUDR – Verordening ontbossingsvrije producten**](https://ondernemersplein.overheid.nl/duurzaam-ondernemen/milieu/verordening-ontbossingsvrije-producten-eudr-wat-betekent-dit-voor-u/) | Bedrijven die bepaalde grondstoffen/producten (o.a. hout) op de EU-markt brengen of exporteren; relevant voor meubelbedrijven met houtketens | Toepassing uitgesteld naar 30 december 2025 (meer implementatietijd) |
| [**REACH – Registratie, Evaluatie, Autorisatie en Restrictie chemische stoffen**](https://ondernemersplein.overheid.nl/wetten-en-regels/verplichtingen-bij-chemische-stoffen-reach/) | Bedrijven die chemische stoffen produceren, importeren of gebruiken (o.a. in verf, lijmen, coatings; ook meubels) | Sinds 1 juni 2007 van kracht; doorlopend geüpdatet |
| [**Right to Repair Directive – Richtlijn reparatie van goederen**](https://commission.europa.eu/law/law-topic/consumer-protection-law/directive-repair-goods_en) | Fabrikanten/verkopers van goederen binnen scope van de richtlijn (met name consumentenproducten; relevant voor meubelbedrijven wanneer productgroepen worden aangewezen en voor elektronica in meubels) | Richtlijn in werking sinds juli 2024; lidstaten hebben 2 jaar voor omzetting → praktijkdeadline juli 2026 |
| [**UPV Meubels – Uitgebreide Producentenverantwoordelijkheid**](https://afvalcirculair.nl/uitgebreide-producentenverantwoordelijkheid-upv/) | Producenten/importeurs van meubels (wettelijk regime in voorbereiding) | In NL-beleid opgenomen als prestatie: UPV voor meubels in 2029–2030 |
            """, unsafe_allow_html=True)
