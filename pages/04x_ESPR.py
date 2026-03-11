import streamlit as st
import sys
sys.path.append("..")
from widgets import *

st.set_page_config(page_title="ESPR", layout="wide")

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

st.title('Ecodesign for Sustainable Products Regulation (ESPR)')

st.page_link("pages/04_wet_regelgeving.py", label="⬅ Terug naar Wet- en Regelgeving")

st.markdown("""
De Ecodesign for Sustainable Products Regulation (ESPR) is een kaderverordening die duurzaamheids- en circulaire eisen stelt aan producten die op de EU-markt worden gebracht. Deze wet vervangt en breidt de bestaande Ecodesign-richtlijn uit, en is gericht op het verminderen van de milieu-impact van producten gedurende hun hele levenscyclus.

Producten moeten voldoen aan strengere eisen op het gebied van **duurzaamheid, herstelbaarheid, upgradebaarheid, en recycleerbaarheid**. Producten die niet voldoen, mogen niet meer op de Europese markt worden verkocht, geïmporteerd of geëxporteerd.

**Wanneer verplicht?**\n
De verordening is op 18 juli 2024 in werking getreden. In de komende jaren zal de ESPR verder worden geïmplementeerd via specifieke maatregelen en richtlijnen per productcategorie. <u>Richtlijnen voor de meubelbranche worden naar verwachting in 2028 geïmplementeerd.</u>

**Belangrijke details over de ESPR**:
*	**Doel**: De milieu-impact van producten verminderen en de transitie naar een circulaire economie versnellen.
*	**Verplichting**: Fabrikanten, importeurs en distributeurs moeten aantonen dat hun producten voldoen aan de nieuwe eisen. Dit omvat onder andere: 
    -	Het gebruik van duurzame en gerecyclede materialen.
    -	Het bieden van reparatie- en onderhoudsdiensten.
    -	Het verstrekken van informatie over de levensduur en recyclebaarheid van het product.
*	**Digital Product Passport (DPP)**: Producten moeten voorzien zijn van een digitaal paspoort met informatie over hun milieu-impact, herkomst van materialen, en mogelijkheden voor hergebruik of recycling.
*	**Handhaving**: De Autoriteit Consument en Markt (ACM) zal toezicht houden op naleving.

[Klik hier voor meer informatie](https://afvalcirculair.nl/circulair-ontwerp/espr/)

**Verantwoordelijkheid**\n
In de basis zijn fabrikanten verantwoordelijk om hun producten zo te ontwerpen, te maken en te voorzien van de juiste informatie dat ze voldoen aan de ESPR-regels. Importeurs en distributeurs vormen een extra controlepunt: zij moeten nagaan of de fabrikant zijn werk goed heeft gedaan voordat het product in de winkel of op de markt komt. 

Let wel: Als een importeur of distributeur een product onder zijn eigen naam of merk verkoopt, of het product aanpast op een manier die invloed heeft op de naleving van de regels, dan worden zij zelf gezien als fabrikant. In dat geval moeten zij alle bijbehorende verantwoordelijkheden overnemen. (IEEP, 2025)

<u>Relevantie voor jouw meubelbranche</u>

            """, unsafe_allow_html = True)
st.image('assets/ESPR.png')

st.markdown("""
Beschrijving:


De ESPR voor meubels legt nadruk op duurzaam materiaalgebruik en recycleerbaarheid. Er worden de komende jaren richtlijnen geformuleerd op de aspecten uit de afbeelding. De richtlijnen worden naar verwachting in 2028 geimplementeerd. 

Voorbeeldrichtlijnen:  

| **Uittreksel van de verplichtingen van fabrikanten onder de ESPR (Art. 27)** | |
| ---------- | ---------- |
| Productconformiteit |	Zorg ervoor dat producten voldoen aan prestatie- en informatievereisten en dat de DPP (Digital Product Passport) beschikbaar is via een conformiteitsbeoordeling. |
| Markering en identificatie | Zorg ervoor dat producten vergezeld gaan van een type-/batch-/serienummer en correcte etikettering, zoals de conformiteitsmarkering. |
| Digitaal Productpaspoort | Zorg voor beschikbaarheid en toegankelijkheid van de DPP, inclusief contactgegevens van de fabrikant. |
| Corrigerende maatregelen | Werk samen met de nationale autoriteit betreffende corrigerende maatregelen, terugroeping of verwijdering van niet-conforme producten. |

Bron: [IEEP (Institute for European Environmental Policy), April 2025](https://ieep.eu/wp-content/uploads/2025/04/External-impacts-of-new-EU-sustainable-product-standards-IEEP-2025.pdf)

	

**Digitaal productpaspoort**\n
Een belangrijk element van de ESPR is het digitaal productpaspoort. Een digitaal productpaspoort (DPP) is een ‘tag’ (zoals een QR-code) op een product, die gescand kan worden en informatie geeft over de duurzaamheid van een product. 

**Onverkochte consumentenproducten**\n
De ESPR stelt ook eisen aan het weggooien en vernietigen van onverkochte consumentenproducten. Zo bevat de verordening een algemeen beginsel waarin staat dat marktdeelnemers passende maatregelen moeten nemen om te voorkomen dat onverkochte consumentenproducten vernietigd worden. Als een marktdeelnemer onverkochte consumentenproducten weggooit of laat weggooien, geldt een informatieplicht. Voor meer informatie, zie [ESPR – Circulaw](https://www.circulaw.nl/eu-wetgeving/ecodesign-for-sustainable-products-regulation-(espr).  


<u>Belangrijke risico’s en kansen</u>

-	Verwijdering van producten uit online marktplaatsen en zoekmachines (IEEP, 2025)

Externe links
-	[ESPR – Circulaw](https://www.circulaw.nl/eu-wetgeving/ecodesign-for-sustainable-products-regulation-(espr))
-	[ESPR – Institute for European Environmental Policy](https://ieep.eu/wp-content/uploads/2025/04/External-impacts-of-new-EU-sustainable-product-standards-IEEP-2025.pdf)


<u>Achtergrond (uit EC working plan)</u> 
Groot potentieel om aspecten van hulpbronnengebruik te verbeteren, waarbij de impact van de productie en levering van materialen vaak de belangrijkste bijdrage levert aan verschillende milieu-impactcategorieën (bijv. klimaatverandering, verzuring, eutrofiëring) en afvalproductie. Positieve impact op andere categorieën zoals lucht, bodem en biodiversiteit.

            """, unsafe_allow_html = True)
