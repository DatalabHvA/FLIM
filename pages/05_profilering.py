import streamlit as st
import pandas as pd
import numpy as np
import sys
import plotly.graph_objects as go
from plotly.subplots import make_subplots
sys.path.append("..")

from widgets import *

ss = st.session_state

st.set_page_config(page_title="Bedrijfsprofilering", layout="wide")

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

# -----------------------------
# Layout / Navigation
# -----------------------------
st.title("Bedrijfsprofilering")
st.page_link("Home.py", label="⬅ Terug naar Home")

# -----------------------------
# Pages
# -----------------------------
with st.expander("Overzicht", expanded = True):
    st.header("Strategisch onderscheiden voor een toekomstbestendige marktpositie")
    st.write("Hoe zichtbaar en geloofwaardig ben jij met je toekomstbestendige keuzes? Sterke profilering betekent dat je deze keuzes niet alleen maakt, maar ze ook strategisch inzet om je marktpositie te versterken. Maximaal effect bereik je door het samenspel van vier elementen: (1) bewijs, (2) transparantie, (3) ketenprofilering en (4) employer branding.")

    c1, c2, c3 = st.columns([1,3,1])
    c2.image('assets/Landing - profilering.png', )
    
    with st.container(border = True):
        st.subheader("Relevantie en urgentie")
        st.write("Door je toekomstbestendige prestaties objectief te onderbouwen, hier open over te rapporteren en dit actief te benutten in je ketensamenwerking, bouw je aan een herkenbaar en onderscheidend duurzaam profiel. Dat profiel werkt door in je aantrekkelijkheid voor klanten, opdrachtgevers én talent. Profilering is daarmee geen communicatie achteraf, maar een strategische hefboom: het verbindt inhoudelijke verduurzaming met vertrouwen, markttoegang en concurrentievoordeel.")
        st.write("In een markt waarin transparantie en aantoonbare impact steeds vaker randvoorwaarde zijn, bepaalt de manier waarop je je profileert of je wordt gekozen/gepasseerd. Wie dit niet zichtbaar en geloofwaardig positioneert, laat waarde liggen.")
        st.write("Daarom bekijken we profilering vanuit verschillende perspectieven: als werkgever (employer branding), richting andere marktpartijen (ketenprofilering en transparantie). Daarna kijken we richting consument en opdrachtgevers, waar certificeringen en labels een steeds grotere rol spelen in onderscheidend vermogen. Tenslotte richting overheid en wet- en regelgeving, waar aantoonbaarheid en verantwoording steeds belangrijker worden.")
        st.write("Samen vormen deze perspectieven jouw mogelijkheden voor strategische positionering in een veranderende markt.")

    #st.image('assets/Landing - profilering.png')

with st.expander("**1. Bewijslaag**"):
    st.header("Bewijslaag")
    st.write("Er zijn verschillende manieren om je als bedrijf voordeel te halen uit de stappen die je onderneemt op het gebied van ontwerp, grondstoffen en keuzes in jouw toeleveringsketen. Een van de stappen om hier betrouwbaar over te kunnen publiceren, is het creëren van een bewijslaag. Dit bewijs kan de vorm aannemen van certificeringen, labels, duurzaamheidsindices (alleen B2B) en onderbouwde impactmetingen van producten en materialen (EPD) met transparante doorrekeningen van de hele levenscyclus van producten (LCA’s). Daarmee maak je zichtbaar dat verduurzaming niet alleen een ambitie is, maar gebaseerd is op meetbare en verifieerbare resultaten. Dit vormt de basis voor betrouwbare en geloofwaardige communicatie richting klanten, opdrachtgevers, ketenpartners, financiers en medewerkers.")
    
    with st.container(border = True):
        st.subheader("Certificeringen")
        st.write("Certificeringen bieden een onafhankelijk en betrouwbaar kader om te laten zien dat keuzes op het gebied van grondstoffen, materialen, ontwerp, lokale productie en ketenverantwoordelijkheid voldoen aan vastgestelde normen. Door gebruik te maken van relevante certificeringen maak je inzichtelijk dat duurzaamheid is ingebed in processen en besluitvorming, en niet afhankelijk is van losse claims. Klik op onderstaande logo van certificeringen om meer te lezen.")

        st.markdown("""
        <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:25px; text-align:center;">

        <a href="https://www.bcorpbenelux.com/" target="_blank">
        <img src="https://tse1.mm.bing.net/th/id/OIP.AW6-CEhFzNxFzrmKGEUVeQHaHa"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://www.kiwa.com/nl/nl/expertisegebieden/duurzaamheid/circulair-ondernemen/brl-k11006-prestatieladder-circulair/" target="_blank">
        <img src="https://tse3.mm.bing.net/th/id/OIP.pHw7USyv97ejUAktZz7aTwHaHY?pid=Api"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://www.co2-prestatieladder.nl/" target="_blank">
        <img src="https://tse1.mm.bing.net/th/id/OIP.j-1A2AENEes7A_uVHemnmQHaFW"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://nl.fsc.org/nl-nl" target="_blank">
        <img src="https://tse2.mm.bing.net/th/id/OIP.k7bSDCFeVqW9zQICeyIKdQHaFj?pid=Api"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://pefc.nl/" target="_blank">
        <img src="https://cdn.pefc.org/igen/pefc.org/media/2020-02/cb2334c4-b4a8-4570-95dd-00cd266bbbbc/b155e4b5-439a-5b1a-9465-4e39c7ab8585.png?m%5B%5D=t%28inside%2C900%2C900%29"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://www.stip.org/stip-certificering/" target="_blank">
        <img src="https://tse1.mm.bing.net/th/id/OIP.BCIl8XB-Sp4rAKhCsaLFagHaHZ?pid=Api"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://greenguard.nl/" target="_blank">
        <img src="https://climatecoating.nl/cc-content/uploads/2023/01/ul-greenguard-gold-vector-logo.svg"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://www.keurmerkenwijzer.nl/alle-keurmerken/overig/cradle-to-cradle-certified" target="_blank">
        <img src="https://tse2.mm.bing.net/th/id/OIP.a3LQpSz-lYnvqv_rTn9GfwHaE8"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        <a href="https://natureplus.org/" target="_blank">
        <img src="https://tse4.mm.bing.net/th/id/OIP.fw6giwPUeZJr9IlWDkJBYQHaIu"
        style="max-width:160px; max-height:110px; object-fit:contain;">
        </a>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("Lees in [dit artikel van Artisan Furniture](https://www.artisanfurniture.net/nl/furniture-trends/certifications-for-sustainable-furniture/) verder over de invloed van certificeringen op meubelwaarde maar ook de toepassingen, authenticatie en kosten die hierbij kunnen komen kijken.")


    with st.container(border = True):
        st.subheader("Duurzaamheidslabels")
        st.write("Betrouwbare duurzaamheidslabels maken in één oogopslag zichtbaar dat producten of materialen voldoen aan duidelijke duurzaamheidscriteria. Ze vertalen complexe eisen rond grondstoffen, productie en ketenverantwoordelijkheid naar herkenbare en vergelijkbare signalen. Door erkende labels te voeren, verlaag je de informatie­drempel voor retailers, opdrachtgevers, consumenten en partners en versterk je het vertrouwen dat duurzame keuzes onafhankelijk zijn getoetst.")

        rows = [
            ("sep-14",  2, "39"),
            ("mar-15",  2, "39"),
            ("sep-15",  3, "42"),
            ("mar-16",  3, "42"),
            ("sep-16",  3, "42"),
            ("mar-17",  3, "42"),
            ("sep-17",  0, "-"),
            ("mrt-18",  1, "38"),
            ("sep-18",  1, "38"),
            ("mrt-19",  2, "42"),
            ("sep-19",  6, "64"),
            ("mrt-20", 10, "477"),
            ("sep-20", 16, "743"),
            ("mrt-21", 17, "790"),
            ("sep-21", 28, "892"),
            ("mrt-22", 35, "1,572"),
            ("sep-22", 37, "1,548"),
            ("mrt-23", 38, "1,550"),
            ("sep-23", 51, "1,916"),
            ("mrt-24", 60, "2,420"),
            ("sep-24", 83, "3,944"),
            ("mrt-25", 99, "4,451"),
            ("sep-25",109, "4,997"),
        ]

        df = pd.DataFrame(rows, columns=["Category", "Multi-product licenties", "Producten_raw"])

        df["Producten"] = (
            df["Producten_raw"]
            .replace("-", np.nan)
            .astype(str)
            .str.replace(",", "", regex=False)
        )
        df["Producten"] = pd.to_numeric(df["Producten"], errors="coerce")

        # --- Figure with secondary y-axis ---
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Bars (left y-axis)
        fig.add_trace(
            go.Bar(
                x=df["Category"],
                y=df["Producten"],
                name="Producten",
                marker=dict(color="#2FA84F"),
                hovertemplate="%{x}<br>Producten: %{y:,.0f}<extra></extra>",
            ),
            secondary_y=False,
        )

        # Line (right y-axis)
        fig.add_trace(
            go.Scatter(
                x=df["Category"],
                y=df["Multi-product licenties"],
                name="Multi-product licenties",
                mode="lines+markers",
                line=dict(color="black", width=3),
                marker=dict(color="black", size=7),
                hovertemplate="%{x}<br>Multi-product licenties: %{y}<extra></extra>",
            ),
            secondary_y=True,
        )

        fig.update_layout(
            title=dict(
                text="Ontwikkeling van EU Ecolabel licenties en producten in de meubelair<br>productgroep (2014-2025)",
                x=0.5,
                xanchor="center",
            ),
            plot_bgcolor="white",
            paper_bgcolor="white",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.32,
                xanchor="center",
                x=0.5,
            ),
            margin=dict(l=70, r=70, t=90, b=0),
            height=450,
        )

        fig.update_xaxes(tickangle=-45, showgrid=False)

        # Left axis (Producten)
        fig.update_yaxes(
            range=[0, 6000],
            showgrid=True,
            gridcolor="#D9D9D9",
            zeroline=False,
            tickformat=",",
            secondary_y=False,
        )

        # Right axis (Licenties)
        fig.update_yaxes(
            range=[0, 120],
            showgrid=False,
            zeroline=False,
            secondary_y=True,
        )

        # Annotations last points (109 and 4,997)
        last_x = df["Category"].iloc[-1]
        last_lic = int(df["Multi-product licenties"].iloc[-1])
        last_prod = int(df["Producten"].iloc[-1])

        fig.add_annotation(
            x=last_x, y=last_lic,
            xref="x", yref="y2",
            text=f"<b>{last_lic}</b>",
            showarrow=True, arrowhead=2, ax=-30, ay=-30,
            font=dict(color="black"),
        )

        fig.add_annotation(
            x=last_x, y=last_prod,
            xref="x", yref="y",
            text=f"<b>{last_prod:,}</b>",
            showarrow=True, arrowhead=2, ax=30, ay=0,
            font=dict(color="black"),
        )


        st.plotly_chart(fig)
        st.caption("Binnen de Europese markt hebben inmiddels bijna 5.000 meubels het EU Ecolabel toegekend gekregen, dit aantal groeit gestaag met meer dan 50% jaar op jaar. (bron: Europese Commissie)")

        cols1 = st.columns([6,1])
        with cols1[0]:
            st.markdown("""
            **EU Ecolabel** - Een transnationaal toegepast Europees milieukeurmerk en tevens strenge norm voor milieuvriendelijke producten waaronder meubilair. Dit keurmerk geeft aan dat een product of dienst een verminderde milieu-impact heeft over diens gehele levenscyclus, van grondstofwinning tot productie, gebruik en afvalfase. Deze aanduiding garandeert dat een meubelstuk, zoals een stoel, voldoet aan strenge criteria om de milieuschade gedurende deze levenscyclus te beperken. “ bronHet label hanteert strenge en wetenschappelijk onderbouwde criteria en is breed toepasbaar als herkenbaar consumentenlabel binnen de EU. Meer lezen: [EU Ecolabel](https://environment.ec.europa.eu/topics/circular-economy/eu-ecolabel_en)
                        """)
        with cols1[1]:
            st.image('assets/ecolabel.png')

        cols2 = st.columns([1,6])
        with cols2[0]:
            st.image('assets/oekotex.jpg')

        with cols2[1]:
                    st.markdown("""
            **OEKO‑TEX** - Label voor stoffen, schuimen en bekledingsmaterialen als bio-katoen en leder dat garandeert dat geen schadelijke grondstoffen worden gebruikt, zoals zware metalen, pesticiden, formaldehyde of kankerverwekkende kleurstoffen. Het richt zich vooral op gezondheid en veiligheid voor de gebruiker, met name bij direct huidcontact. Meer lezen: [OEKO-TEX](https://www.oeko-tex.com/)
                        """)

        cols3 = st.columns([6,1])
        with cols3[0]:
            st.markdown("""
            **Blauer Engel** - Milieukeurmerk voor producten en diensten die uit Duitsland komen of daar verkocht worden met lage emissies en een lage milieubelasting. “Binnen de interieursector vind je het keurmerk vooral op meubels, vloerbedekking en verf. Het richt zich sterk op binnenluchtkwaliteit en stelt strenge eisen aan emissies van schadelijke stoffen zoals VOS en formaldehyde. Producten met dit label dragen aantoonbaar bij aan een gezondere leefomgeving. Meer lezen: [Blauer Engel](https://www.blauer-engel.de/) of [Sustanea.com](https://www.sustanea.com/blogs/blog-1-duurzaamheidscertificaten-uitgelegd-welke-certificaten-zijn-er-in-de-interieurbranche-en)
                        """)
        with cols3[1]:
            st.image('assets/blauwer_engel.jpg')

    

        # RIJ 4 — WELL
        cols4 = st.columns([1,6])
        with cols4[0]:
            st.image("https://buildingrevolution.nl/wp-content/uploads/2021/11/well-building-institute-logo.jpg")
        with cols4[1]:
            st.markdown("""
            **WELL Building Standard** - Internationaal certificeringssysteem voor gezonde gebouwen dat zich richt op het welzijn van gebruikers, met aandacht voor onder andere luchtkwaliteit, materialen, licht, comfort en ergonomie. Binnen de meubel- en interieurbranche is WELL relevant omdat meubels, stoffering en afwerkingsmaterialen direct invloed hebben op binnenluchtkwaliteit en gebruikersgezondheid. Producten met lage emissies, veilige materialen en ergonomisch ontwerp dragen bij aan WELL-credits binnen gebouwcertificering. Dit maakt het label toepasbaar bij projectinrichting, kantoorconcepten en zorg- en onderwijsomgevingen waar gezondheid centraal staat. 
            Meer lezen: [WELL](https://www.wellcertified.com/)
            """)
        
        
        # RIJ 5 — BREEAM
        cols5 = st.columns([6,1])
        with cols5[0]:
            st.markdown("""
            **BREEAM** - Internationaal duurzaamheidskeurmerk voor gebouwen dat prestaties beoordeelt op thema’s zoals materialen, gezondheid, circulariteit en milieubelasting. Binnen de meubel- en interieurbranche is BREEAM relevant omdat meubilair en interieur bijdragen aan credits voor materiaalgebruik, losmaakbaarheid, levensduur en emissies naar de binnenlucht. Circulair ontworpen meubels, hergebruikte materialen en producten met lage milieubelasting helpen bij het behalen van BREEAM-scores in nieuwbouw en renovatieprojecten. Hierdoor is het label breed toepasbaar bij projectinrichting, aanbestedingen en duurzame vastgoedontwikkeling. Meer lezen:
            Meer lezen: [BREEAM](https://www.breeam.com/)
            """)
        with cols5[1]:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/BREEAM_logo.svg/3840px-BREEAM_logo.svg.png")
            
        
    if ss.klanttype_value == 'B2B':
        with st.container(border = True):
            st.subheader('Duurzaamheidsindices')
            st.write("Duurzaamheidsindices plaatsen de prestaties van een organisatie in een bredere context en maken vergelijking met andere bedrijven (benchmarking) mogelijk. Ze geven inzicht in hoe duurzaamheidsbeleid en -resultaten zich verhouden tot markt en sector. Door goed te scoren op relevante indices wordt herkenbaarheid en daarmee zichtbaarheid gecreëerd, wat bijdraagt aan duurzame positionering en profilering van de organisatie richting keten en financiers.")
            cols4 = st.columns([1,6])
            with cols4[0]:
                st.image('assets/ecovadis.png')
            with cols4[1]:
                
                st.markdown("""
            - **EcoVadis** – Veel gebruikt in B2B-ketens voor bedrijven om hun leveranciers te screenen op duurzaamheid. EcoVadis is een duurzaamheidsindex-platforms, bekend om zijn beoordeling van de acties van bedrijven op het gebied van duurzaamheid (ESG-rating). Het wordt gebruikt door duizenden organisaties, waaronder grote internationale bedrijven om zich te benchmarken. Slechts 1% van de beoordeelde bedrijven krijgt de hoogste onderscheiding (platina), wat een bewijs is van zeer hoge normen op het gebied van bedrijfsverantwoordelijkheid en ethiek. Lees meer: [website](https://ecovadis.com/nl/)
                            """)
            st.markdown("""
                        -	**CDP** – Transparantie over klimaat- en milieuprestaties, vooral richting investeerders en stakeholders.
                        -	**Dow Jones Sustainability Index** - De eerste wereldwijde duurzaamheidsindex en beoordeelt de duurzaamheidsprestaties van bedrijven in verschillende sectoren en regio's. Vooral bedoeld voor het beursgenoteerd grootbedrijf, is DJSI is ontworpen om beleggers inzicht te geven in bedrijven die vooroplopen op het gebied van duurzaamheid. 
                        -	**Sustainalytics** –  Een platform waar bedrijven vrijwillig hun CO₂-uitstoot, watergebruik en ontbossingsrisico’s rapporteren. ESG-risicoprofielen relevant voor financiers

                        """)
    
    with st.container(border = True):
        st.subheader('Environmental Product Declaration (EPD)')
        st.markdown("""
                    EPD’s bieden onderbouwde impactmetingen van producten en materialen op basis van gestandaardiseerde en onafhankelijke methodieken. Ze maken de milieuprestaties van producten transparant en onderling vergelijkbaar, wat essentieel is voor onderbouwde keuzes in ontwerp, inkoop en aanbestedingen. Daarmee vormen EPD’s een betrouwbaar fundament voor zowel technische besluitvorming als externe communicatie.
                    -	Meubelmaker Casala heeft meerdere EPD’s voor hun producten gepubliceerd, zoals hun Lynx-model stoelen: [pdf](https://meinema.nl/ECOPaspoort/casala-lynx-epd.pdf) 
                    -	Het Spaanse Steelcase S.A., is een ontwerper, producent en leverancier van interieurs en meubels die een EPD-verklaring op laten stellen voor de Lares bank (1800x1600mm): [pdf](https://www.environdec.com/library/epd7395)
                    -	Leverancier van onderwijsmaterialen, meubels en creatieve leermiddelen Lekolar AB uit Zweden heeft een EPD op laten stellen van hun 12:38 tafel: [pdf](https://www.environdec.com/library/epd8173)
                    """)

    with st.container(border = True):
        st.subheader("Levens Cyclus Analyse (LCA)")
        st.markdown("""
                    Een LCA geeft inzicht via transparante doorrekeningen van de hele levenscyclus van een product, van grondstofwinning tot gebruik en einde levensduur. Ze maken zichtbaar waar de grootste milieu-impact ontstaat en waar optimalisatie het meeste effect heeft. Door LCA’s toe te passen onderbouw je jouw gemaakte ontwerp- en materiaalkeuzes met data en creëer je een basis voor verdere verbetering en verantwoorde ketenbeslissingen.
                    - 	(Voorbeelden)
                    """)

with st.expander("**2. Transparantie**"):
    st.header("Transparantie")
    st.write("Naast het opbouwen van een bewijslaag is transparantie vanuit het eigen bedrijf essentieel voor een betrouwbare bedrijfsprofilering op je duurzame keuzes. Waar de bewijslaag draait om externe erkenning, gaat transparantie over de mate waarin een bedrijf openheid geeft over het totale duurzaamheidsprofiel richting klanten, opdrachtgevers, ketenpartners en financiers. Transparantie betekent dat doelen, risico’s en prestaties systematisch inzichtelijk worden gemaakt via rapportages en meetbare prestatie indicatoren. Dit raakt aan nieuwe wet- en regelgeving zoals de CSRD/VSME waarbij niet alleen successen, maar ook risico’s en verbeterpunten zichtbaar worden gemaakt. Transparantie versterkt zo het duurzame profiel, vergroot marktvertrouwen en draagt bij aan concurrentiekracht.")
    
    with st.container(border = True):
        st.subheader("CSRD")
        st.markdown("""
                    Hoewel de Corporate Sustainability Reporting Directive (CSRD) rapportageverplichting vooral geldt voor grotere organisaties, heeft deze richtlijn ook duidelijke belang voor kleine en middelgrote bedrijven. De grote bedrijven moeten namelijk transparant rapporteren over hun volledige waardeketen, dus niet alleen hun eigen activiteiten maar ook die van hun (keten)partners. [RVO](https://www.rvo.nl/onderwerpen/csrd)
                    
                    <div style="
                        font-size: 32px;
                        font-style: italic;
                        text-align: center;
                        margin: 3rem 1rem;
                        line-height: 1.4;
                    ">
                    Uit onderzoek blijkt dat 38% van de bedrijven CSRD ervaart als een concurrentievoordeel. <a href='https://www.pwc.nl/nl/actueel-en-publicaties/themas/duurzaamheid/global-csrd-survey-2024.html' target="_blank"> PwC, 2024</a>.
                    </div>
                    
                    """ , unsafe_allow_html = True)
        
    with st.container(border = True):
        st.subheader("VSME")
        st.markdown("""
        Voor kleinere bedrijven biedt het gebruik van VSME-rapportage een laagdrempelige manier om duurzaamheidsdoelen en prestaties inzichtelijk te maken en zich te onderscheiden binnen de markt. Dit maakt hen een aantrekkelijkere en beter voorbereide ketenpartner. CSRD-plichtige organisaties zullen bij voorkeur samenwerken met bedrijven die hun duurzaamheidsinformatie op orde hebben, omdat dit het rapportageproces vereenvoudigt en risico’s op duurzaamheidsprestaties verlaagt. Op deze manier kan transparantie over duurzaamheid voor kleinere bedrijven uitgroeien tot een strategisch voordeel zonder dat zij zelf CSRD-plichtig zijn: betere kansen bij samenwerkingen, aanbestedingen en langdurige klantrelaties. [VIO](https://www.vlaio.be/nl/begeleiding-advies/duurzaam-ondernemen/duurzaamheidsverslag/vrijwillige-duurzaamheidsrapportering-voor-kmos-vsme)

        Lees meer over de CSRD en VSME binnen de factor Wet- en Regelgeving.
        """)
        st.page_link("pages/04_wet_regelgeving.py", label="-> Ga naar Wet- en Regelgeving")


with st.expander("**3. Ketenprofilering**"):
    st.header("Ketenprofilering")
    st.markdown("""
    Naast bewijs en transparantie speelt ook de manier waarop een bedrijf zich positioneert binnen de keten een belangrijke rol in duurzame bedrijfsprofilering. Ketenprofilering gaat over het zichtbaar maken van strategische samenwerkingen, partnerschappen en collectieve initiatieven waarin duurzaamheid gezamenlijk wordt opgepakt.

    Door actief deel te nemen aan sector- of regionale coalities zoals klimaattafels, branche brede MVO-programma’s of collectieven binnen de branche en deze samenwerking expliciet te tonen in proposities en aanbestedingen, laat een bedrijf zien dat verduurzaming niet op zichzelf staat, maar onderdeel is van een bredere ketenaanpak. Zaak is om deze dan ook zichtbaar te maken richting klant en opdrachtgever. [TNO](https://repository.tno.nl/SingleDoc?docId=55561)

    Voorbeelden van bestaande meubelbranche collectieven:
    -	[Future > Factory > Furniture (FFF)](http://www.futurefactoryfurniture.com/)
    -	[Branchevereniging Koninklijke CBM](https://cbm.nl/)
    -	[Wood Loop (sectoraal systeem)](https://www.wood-loop.nl/)

    Ketenprofilering maakt daarmee zichtbaar dat een bedrijf inzet op gedeelde impact en strategische samenwerking, wat bijdraagt aan een sterker marktprofiel, grotere geloofwaardigheid en een sterkere concurrentiepositie.

                """)

with st.expander("**4. Employer branding**"):
    st.header("Employer branding")
    st.write("Naast positionering richting markt en keten wordt duurzame profilering als werkgever steeds belangrijker voor het aantrekken en behouden van medewerkers. Dit wordt aangeduid als employer branding (werkgeversimago): de manier waarop een organisatie haar duurzame propositie, ambities en maatschappelijke bijdrage inzet om talent aan te trekken, te binden en te motiveren.")
    st.markdown("""
                <div style="
                    font-size: 32px;
                    font-style: italic;
                    text-align: center;
                    margin: 3rem 1rem;
                    line-height: 1.4;
                ">
                Bijna 70% van de ondervraagde branchepartijen bevestigt de samenhang tussen concurrentie binnen de sector met de ervaren wervingsproblemen. <a href='https://cbm.nl/publicatie' target="_blank"> Conjunctuurmonitor 2024, CBM</a>.
                </div>

                Juist in een sector waar de concurrentie op personeel groot is, wordt onderscheidend vermogen op de arbeidsmarkt een strategische noodzaak. Duurzaamheid en maatschappelijke verantwoordelijkheid worden vooral voor de jongere generaties steeds vaker een harde eis in hun loopbaankeuze. Uit onder meer de [Deloitte Global Millennial Survey (2024)](https://www.deloitte.com/nl/nl/services/consulting/research/2024-gen-z-and-millennial-survey.html) blijkt dat Millennials en Generatie Z verwachten dat bedrijven actief bijdragen aan maatschappelijke en ecologische vraagstukken. Zingeving en impact wegen daarbij voor veel werkzoekenden zwaarder dan salaris of functietitel. Ook recent onderzoek van [Gallup (2023)](https://advisor.visualcapitalist.com/wp-content/uploads/2023/06/state-of-the-global-workplace-2023-download.pdf) en [PwC (2024)](https://www.pwc.com.tr/global-workforce-sustainability-study-2024)  laat zien dat betekenisvol werk en authentieke duurzaamheidsambities bijdragen aan hogere betrokkenheid en langer behoud van jong talent.
                
                <div style="
                    font-size: 32px;
                    font-style: italic;
                    text-align: center;
                    margin: 3rem 1rem;
                    line-height: 1.4;
                ">
                Ruim 50% van de Gen Z'ers zegt ‘NEE’ tegen werkgevers/opdrachten die niet matchen met hun persoonlijke ethiek of overtuigingen. <a href='https://www.deloitte.com/content/dam/assets-zone2/nl/nl/docs/about/2024/deloitte-nl-con-genz-millennial-survey-2024-country-report-netherlands.pdf' target="_blank"> Deloitte - Gen Z en Millennial Survey 2024</a>.
                </div>

                Door duurzaamheidsinspanningen expliciet te communiceren en te verbinden aan bredere maatschappelijke doelen – bijvoorbeeld die van publieke opdrachtgevers of sectorale transities – vergroot een bedrijf zijn aantrekkelijkheid als werkgever, stelt [TNO (2024)](https://repository.tno.nl/SingleDoc?docId=55561). Dit versterkt niet alleen de instroom van (jong) talent, maar vergroot ook trots, betrokkenheid en loyaliteit onder bestaande medewerkers, doordat betekenisvol en impactgericht werk aantoonbaar samenhangt met hogere employee engagement en retentie [Gallup (2023)](https://advisor.visualcapitalist.com/wp-content/uploads/2023/06/state-of-the-global-workplace-2023-download.pdf),[PwC (2024)](https://www.pwc.com.tr/global-workforce-sustainability-study-2024). Employer branding maakt daarmee dat duurzame profilering niet alleen extern waardevol is, maar ook intern bijdraagt aan continuïteit en concurrentiekracht.

                
                """, unsafe_allow_html=True)
