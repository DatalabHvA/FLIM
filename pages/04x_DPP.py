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

st.image('assets/DPP.png')
st.subheader("DPP (Digitaal Product Paspoort)")
st.markdown("""
Het Digital Product Passport (DPP) is een nieuwe Europese verplichting die deel uitmaakt van de **Ecodesign for Sustainable Products Regulation (ESPR)**. Het DPP is een digitaal document dat gedetailleerde informatie bevat over de duurzaamheid, herkomst, samenstelling en levenscyclus van een product. Het doel is om transparantie te vergroten en consumenten, bedrijven en toezichthouders beter te informeren over de milieu-impact van producten.
            """)
st.page_link("pages/04x_ESPR.py", label = "Ecodesign for Sustainable Products Regulation (ESPR)", icon="➡")

st.subheader("Wanneer verplicht?")
st.markdown("""
**Belangrijke details over het DPP:**
*	**Doel**: Consumenten en bedrijven informeren over de duurzaamheid en circulariteit van producten, en de transitie naar een circulaire economie versnellen.
*	**Verplichting**: Producenten en importeurs moeten voor elk product een DPP aanmaken dat minimaal de volgende informatie bevat: 
    -	**Herkomst van materialen** (inclusief geolocatie/coördinaten van winning en productie).
    -	**Samenstelling** (welke materialen en chemicaliën zijn gebruikt?).
    -	**Reparatie- en onderhoudsmogelijkheden** (hoe kan het product worden gerepareerd of geüpdaterd?).
    -	**Recyclebaarheid** (hoe kan het product aan het einde van de levensduur worden gerecycled?).
    -	**CO₂-voetafdruk** (wat is de milieu-impact van het product?).
    -	**Garantie- en retourvoorwaarden**.
*	**Toegankelijkheid**: Het DPP moet digitaal beschikbaar zijn, bijvoorbeeld via een QR-code op het product of de verpakking.
*	**Ketenverantwoordelijkheid**: Bedrijven moeten ervoor zorgen dat ook toeleveranciers en distributeurs toegang hebben tot de DPP-informatie.
*	**Handhaving**: Lidstaten zijn verantwoordelijk voor de handhaving. In Nederland zal de **Autoriteit Consument en Markt (ACM)** toezicht houden op naleving. Bedrijven die geen DPP verstrekken, riskeren boetes of marktverboden.
         
[Klik hier voor meer informatie](https://www.tno.nl/nl/digitaal/data-sharing/digitaal-product-paspoort/)
            
Beschrijving:

<u>Kern van de wet</u>
Een Digitaal Product Paspoort (DPP) is een ‘tag’ (zoals een QR-code) op een product, die gescand kan worden. Achterliggend is een gestandaardiseerd digitaal document dat uitgebreide, productspecifieke, informatie bevat over de samenstelling, productie, gebruik en recycling van een product. Het DPP is onderdeel van de Europese Ecodesign for Sustainable Products Regulation (ESPR), die bedrijven gaat veprlichten om voor meubels het digitaal paspoort op te stellen. 
Het DPP moet:
-	Vergroten van transparantie in productketens en helpen van zowel consumenten als zakelijke afnemers om duurzame keuzes te maken
-	Bevorderen van hergebruik, reparatie en recycling en het vergroten van de levensduur van producten
-	Vereenvoudigen van handhaving door toezichthouders
-	Beter geïnformeerde consumenten, die gestimuleerd worden om duurzamere producten te kiezen of geen product aan te schaffen, evenals informatie over het einde van de levenscyclus van producten (zoals recycling en hergebruik)

<u>Relevantie voor jouw branche (filter: meubel)</u>

De invoering van het Digitaal Productpaspoort is een systeemverandering in hoe je de meubelbranche om moet gaan met productinformatie. Het DPP legt een verplichting op tot structurele dataregistratie en transparantie over de hele keten. Klanten, toezichthouders en afnemers willen weten wat erin zit, waar het vandaan komt, en hoe het weer uit elkaar kan.  

*Een stoel wordt geen product, maar een data-object met levenscyclusinformatie. Bijvoorbeeld:*
-	***Ontwerper***: *moet ontwerpen met demontage en registratie in gedachten*
-	***Inkoop***: *moet materiaaldata opvragen én vastleggen*
-	***Sales***: *kan duurzaamheid onderbouwen met objectieve info*
-	***Serviceafdeling***: *gebruikt DPP bij onderhoud, reparatie of retour*

<u>Belangrijke risico’s en kansen in de UPV</u>

**Risico’s**
-	De meubelbranche kent een grote variëteit aan materialen (hout, schuim, metaal, textiel), wat het vastleggen en beheren van productinformatie complex maakt.
-	Niet-naleving leidt tot marktuitsluiting (o.a. binnen aanbestedingen)
-   Hoge implementatiekosten voor MKB-bedrijven zonder datastandaarden
-	Afhankelijkheid van leveranciers voor correcte materiaaldata
-	Digitale infrastructuur ontbreekt vaak nog

| Boetes, sancties & handhavingskosten | Markttoegang verliezen / productverboden | Ketenrisico’s |
|-----|-------------------|--------|
| Boetes bij onvolledige of foutieve digitale productpaspoorten. | Producten zonder geldige paspoorten worden geweigerd. | Incorrecte productdata kan leiden tot aansprakelijkheid voor misleidende informatie |
            
**Kansen**
-	DPP is de sleutel tot markttoegang, subsidievoorwaarden, aanbestedingen én risicobeheersing bij CSRD-verantwoording.
-	Toegang tot duurzame markten en klanten (B2B en overheid)
-	Marktvoordeel bij early adopters: transparantie als onderscheidende factor
-	Restwaarde kan beter worden bepaald, dit versterkt circulaire verdienmodellen

<u>Externe links</u>

Beschrijving: 
[https://www.tno.nl/nl/digitaal/data-sharing/digitaal-product-paspoort/](https://www.tno.nl/nl/digitaal/data-sharing/digitaal-product-paspoort/)

            """, unsafe_allow_html = True)