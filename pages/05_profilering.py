import streamlit as st
import pandas as pd
import numpy as np
import sys
import plotly.graph_objects as go
from plotly.subplots import make_subplots
sys.path.append("..")

from widgets import *

ss = st.session_state

st.set_page_config(page_title="Profilering & Certificering", layout="wide")

st.markdown("""
    <style>
        /* Hide all sidebar navigation links */
        section[data-testid="stSidebar"] li {
            display: none !important;
        }
        
        /* Verminder padding bovenaan hoofdpagina */
        div.block-container {
            padding-top: 2rem !important;
            padding-bottom: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Layout / Navigation
# -----------------------------
st.title("Profilering & certificering")

with st.sidebar:
    st.header("Navigatie")
    page = st.radio(
        "Ga naar",
        [
            "Overzicht",
            "Bewijslaag",
            "Transparantie",
            "Ketenprofilering",
            "Employer branding",
        ],
        index=0
    )

    widget_klanttype()

# -----------------------------
# Pages
# -----------------------------
if page == "Overzicht":
    st.header("Profilering")
    st.write("Profilering beschrijft hoe bedrijven hun duurzaamheidsinspanningen zichtbaar, geloofwaardig en strategisch inzetten richting de markt. Het gaat daarbij om de samenhang tussen (1) de bewijslaag, (2) transparantie, (3) ketenprofilering en (4) employer branding. Door verduurzaming te onderbouwen met objectief bewijs (zoals certificeringen en meetbare prestaties), hier transparant over te rapporteren en deze informatie actief te benutten in ketensamenwerking, ontstaat een consistent en herkenbaar duurzaam profiel. Deze profilering werkt door in het werkgeversmerk, doordat medewerkers en nieuw talent zich herkennen in de maatschappelijke ambities van het bedrijf, en in de relatie met financiers, die in de toekomst duurzaamheid steeds vaker meenemen in hun risicobeoordeling en financieringsvoorwaarden. Samen laten deze categorieën binnen deze factor zien dat profilering geen los communicatie-instrument is, maar een integrale factor die inhoudelijke verduurzaming verbindt met marktpositie, vertrouwen en concurrentievoordeel.")

elif page == "Bewijslaag":
    st.header("Bewijslaag")
    st.markdown("""
                Er zijn verschillende manieren om je als bedrijf voordeel te halen uit de stappen die je onderneemt op het gebied van ontwerp, grondstoffen en keuzes in jouw toeleveringsketen. Een van de stappen om hier betrouwbaar over te kunnen publiceren, is het creëren van een bewijslaag. Dit bewijs kan de vorm aannemen van certificeringen, labels, duurzaamheidsindices (alleen B2B) en onderbouwde impactmetingen van producten en materialen (EPD) met transparante doorrekeningen van de hele levenscyclus van producten (LCA’s). Daarmee maak je zichtbaar dat verduurzaming niet alleen een ambitie is, maar gebaseerd is op meetbare en verifieerbare resultaten. Dit vormt de basis voor betrouwbare en geloofwaardige communicatie richting klanten, opdrachtgevers, ketenpartners, financiers en medewerkers.

                **Certificering**

                Certificeringen bieden een onafhankelijk en betrouwbaar kader om te laten zien dat keuzes op het gebied van grondstoffen, materialen, ontwerp, lokale productie en ketenverantwoordelijkheid voldoen aan vastgestelde normen. Door gebruik te maken van relevante certificeringen maak je inzichtelijk dat duurzaamheid is ingebed in processen en besluitvorming, en niet afhankelijk is van losse claims.
                -	B Corp
                -	Prestatieladder Circulair (BRL K11006)
                -	CO₂ Prestatieladder
                -	FSC
                -	PEFC
                -	GREENGUARD
                -	Cradle to cradle
                -	Natureplus

                """)

    st.subheader("Duurzaamheidslabel")
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
        **EU Ecolabel** - Een transnationaal toegepast label is het Europese milieukeurmerk EU Ecolabel. Dit geeft aan dat een product of dienst een verminderde milieu-impact heeft over de hele levenscyclus, van grondstofwinning tot productie, gebruik en afvalfase. Het is een strenge norm voor milieuverantwoord meubilair, die de gehele levensduur meeneemt. Deze aanduiding garandeert dat een meubelstuk, zoals een stoel, voldoet aan strenge criteria om de milieuschade vanaf de productie tot aan de verwijdering te beperken. “ bronHet label hanteert strenge en wetenschappelijk onderbouwde criteria en is breed toepasbaar als herkenbaar consumentenlabel binnen de EU. Meer lezen: [website](https://environment.ec.europa.eu/topics/circular-economy/eu-ecolabel_en)
                    """)
    with cols1[1]:
        st.image('assets/ecolabel.png')

    cols2 = st.columns([1,6])
    with cols2[0]:
        st.image('assets/oekotex.jpg')

    with cols2[1]:
                st.markdown("""
        **OEKO‑TEX** - Label voor stoffen, schuimen en bekledingsmaterialen als bio-katoen en leder dat garandeert dat geen schadelijke grondstoffen worden gebruikt, zoals zware metalen, pesticiden, formaldehyde of kankerverwekkende kleurstoffen. Het richt zich vooral op gezondheid en veiligheid voor de gebruiker, met name bij direct huidcontact. Meer lezen: [website](https://www.oeko-tex.com/)
                    """)

    cols3 = st.columns([6,1])
    with cols3[0]:
        st.markdown("""
        **Blauer Engel** - Milieukeurmerk voor producten en diensten die uit Duitsland komen of daar verkocht worden met lage emissies en een lage milieubelasting. “Binnen de interieursector vind je het keurmerk vooral op meubels, vloerbedekking en verf. Het richt zich sterk op binnenluchtkwaliteit en stelt strenge eisen aan emissies van schadelijke stoffen zoals VOS en formaldehyde. Producten met dit label dragen aantoonbaar bij aan een gezondere  leefomgeving. Meer lezen: [website](https://www.blauer-engel.de/) of [Sustanea.com](https://www.sustanea.com/blogs/blog-1-duurzaamheidscertificaten-uitgelegd-welke-certificaten-zijn-er-in-de-interieurbranche-en)
                    """)
    with cols3[1]:
        st.image('assets/blauwer_engel.jpg')

    if ss.klanttype_value == 'B2B':
        st.subheader('Duurzaamheidsindex')
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
    st.subheader('Environmental Product Declaration (EPD)')
    st.markdown("""
                EPD’s bieden onderbouwde impactmetingen van producten en materialen op basis van gestandaardiseerde en onafhankelijke methodieken. Ze maken de milieuprestaties van producten transparant en onderling vergelijkbaar, wat essentieel is voor onderbouwde keuzes in ontwerp, inkoop en aanbestedingen. Daarmee vormen EPD’s een betrouwbaar fundament voor zowel technische besluitvorming als externe communicatie.
                -	<Triboo EPD>
                -	Meubelmaker Casala heeft meerdere EPD’s voor hun producten gepubliceerd, zoals hun Lynx-model stoelen: [pdf](https://meinema.nl/ECOPaspoort/casala-lynx-epd.pdf) 
                -	Het Spaanse Steelcase S.A., is een ontwerper, producent en leverancier van interieurs en meubels die een EPD-verklaring op laten stellen voor de Lares bank (1800x1600mm): [pdf](https://www.environdec.com/library/epd7395)
                -	Leverancier van onderwijsmaterialen, meubels en creatieve leermiddelen Lekolar AB uit Zweden heeft een EPD op laten stellen van hun 12:38 tafel: [pdf](https://www.environdec.com/library/epd8173)
                """)

    st.subheader("Levens Cyclus Analyse (LCA)")
    st.markdown("""
                Een LCA geeft inzicht via transparante doorrekeningen van de hele levenscyclus van een product, van grondstofwinning tot gebruik en einde levensduur. Ze maken zichtbaar waar de grootste milieu-impact ontstaat en waar optimalisatie het meeste effect heeft. Door LCA’s toe te passen onderbouw je jouw gemaakte ontwerp- en materiaalkeuzes met data en creëer je een basis voor verdere verbetering en verantwoorde ketenbeslissingen.
                - 	(Voorbeelden)
                """)

elif page == "Transparantie":
    st.header("Transparantie")
    st.write("Naast het opbouwen van een bewijslaag is transparantie vanuit het eigen bedrijf essentieel voor een betrouwbare bedrijfsprofilering op je duurzame keuzes. Waar de bewijslaag draait om externe erkenning, gaat transparantie over de mate waarin een bedrijf openheid geeft over het totale duurzaamheidsprofiel richting klanten, opdrachtgevers, ketenpartners en financiers. Transparantie betekent dat doelen, risico’s en prestaties systematisch inzichtelijk worden gemaakt via rapportages en meetbare prestatie indicatoren. Dit raakt aan nieuwe wet- en regelgeving zoals de CSRD/VSME waarbij niet alleen successen, maar ook risico’s en verbeterpunten zichtbaar worden gemaakt. Transparantie versterkt zo het duurzame profiel, vergroot marktvertrouwen en draagt bij aan concurrentiekracht.")
    
    st.subheader("CSRD")
    st.markdown("""
                Hoewel de Corporate Sustainability Reporting Directive (CSRD) rapportageverplichting vooral geldt voor grotere organisaties, heeft deze richtlijn ook duidelijke belang voor kleine en middelgrote bedrijven. De grote bedrijven moeten namelijk transparant rapporteren over hun volledige waardeketen, dus niet alleen hun eigen activiteiten maar ook die van hun (keten)partners. [RVO](https://www.rvo.nl/onderwerpen/csrd)
                > Uit onderzoek blijkt dat 38% van de bedrijven CSRD ervaart als een concurrentievoordeel.
                > [PwC, 2024](https://www.pwc.nl/nl/actueel-en-publicaties/themas/duurzaamheid/global-csrd-survey-2024.html)                
                """ )
    
    st.subheader("VSME")
    st.markdown("""
    Voor kleinere bedrijven biedt het gebruik van VSME-rapportage een laagdrempelige manier om duurzaamheidsdoelen en prestaties inzichtelijk te maken en zich te onderscheiden binnen de markt. Dit maakt hen een aantrekkelijkere en beter voorbereide ketenpartner. CSRD-plichtige organisaties zullen bij voorkeur samenwerken met bedrijven die hun duurzaamheidsinformatie op orde hebben, omdat dit het rapportageproces vereenvoudigt en risico’s op duurzaamheidsprestaties verlaagt. Op deze manier kan transparantie over duurzaamheid voor kleinere bedrijven uitgroeien tot een strategisch voordeel zonder dat zij zelf CSRD-plichtig zijn: betere kansen bij samenwerkingen, aanbestedingen en langdurige klantrelaties. [VIO](https://www.vlaio.be/nl/begeleiding-advies/duurzaam-ondernemen/duurzaamheidsverslag/vrijwillige-duurzaamheidsrapportering-voor-kmos-vsme)

    Lees meer over de CSRD en VSME binnen de factor Wet- en Regelgeving.
    """)
    st.page_link("pages/04_wet_regelgeving.py", label="-> Ga naar Wet- en Regelgeving")


elif page == "Ketenprofilering":
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

elif page == "Employer branding":
    st.header("Employer branding")
    st.write("Naast positionering richting markt en keten wordt duurzame profilering als werkgever steeds belangrijker voor het aantrekken en behouden van medewerkers. Dit wordt aangeduid als employer branding (werkgeversimago): de manier waarop een organisatie haar duurzame propositie, ambities en maatschappelijke bijdrage inzet om talent aan te trekken, te binden en te motiveren.")
    st.markdown("""
                > **Bijna 70% van de ondervraagde branchepartijen bevestigt de samenhang tussen concurrentie binnen de sector met de ervaren wervingsproblemen.**
                > [Conjunctuurmonitor 2024, CBM](https://cbm.nl/publicatie)

                Juist in een sector waar de concurrentie op personeel groot is, wordt onderscheidend vermogen op de arbeidsmarkt een strategische noodzaak. Duurzaamheid en maatschappelijke verantwoordelijkheid worden vooral voor de jongere generaties steeds vaker een harde eis in hun loopbaankeuze. Uit onder meer de [Deloitte Global Millennial Survey (2024)](https://www.deloitte.com/nl/nl/services/consulting/research/2024-gen-z-and-millennial-survey.html) blijkt dat Millennials en Generatie Z verwachten dat bedrijven actief bijdragen aan maatschappelijke en ecologische vraagstukken. Zingeving en impact wegen daarbij voor veel werkzoekenden zwaarder dan salaris of functietitel. Ook recent onderzoek van [Gallup (2023)](https://advisor.visualcapitalist.com/wp-content/uploads/2023/06/state-of-the-global-workplace-2023-download.pdf) en [PwC (2024)](https://www.pwc.com.tr/global-workforce-sustainability-study-2024)  laat zien dat betekenisvol werk en authentieke duurzaamheidsambities bijdragen aan hogere betrokkenheid en langer behoud van jong talent.
                
                > **Ruim 50% van de Gen Z'ers zegt ‘NEE’ tegen werkgevers/opdrachten die niet matchen met hun persoonlijke ethiek of overtuigingen**
                > [Deloitte - Gen Z en Millennial Survey 2024](https://www.deloitte.com/content/dam/assets-zone2/nl/nl/docs/about/2024/deloitte-nl-con-genz-millennial-survey-2024-country-report-netherlands.pdf)
                
                Door duurzaamheidsinspanningen expliciet te communiceren en te verbinden aan bredere maatschappelijke doelen – bijvoorbeeld die van publieke opdrachtgevers of sectorale transities – vergroot een bedrijf zijn aantrekkelijkheid als werkgever, stelt [TNO (2024)](https://repository.tno.nl/SingleDoc?docId=55561). Dit versterkt niet alleen de instroom van (jong) talent, maar vergroot ook trots, betrokkenheid en loyaliteit onder bestaande medewerkers, doordat betekenisvol en impactgericht werk aantoonbaar samenhangt met hogere employee engagement en retentie [Gallup (2023)](https://advisor.visualcapitalist.com/wp-content/uploads/2023/06/state-of-the-global-workplace-2023-download.pdf),[PwC (2024)](https://www.pwc.com.tr/global-workforce-sustainability-study-2024). Employer branding maakt daarmee dat duurzame profilering niet alleen extern waardevol is, maar ook intern bijdraagt aan continuïteit en concurrentiekracht.

                
                """)
