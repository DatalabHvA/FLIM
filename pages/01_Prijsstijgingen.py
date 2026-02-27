# pages/02_Leveringszekerheid_Map.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
import sys

sys.path.append("..")
from widgets import *


COMMON_LAYOUT = dict(
    margin=dict(l=40, r=5, t=20, b=60),
    xaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
    yaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
)
CHART_HEIGHT = 320

ss = st.session_state
st.set_page_config(page_title="Prijsontwikkelingen", layout="wide")

st.markdown("""
    <style>
        /* Hide all sidebar navigation links */
        section[data-testid="stSidebar"] li {
            display: none !important;
        }
        
        /* Verminder padding bovenaan hoofdpagina */
        div.block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.page_link("Home.py", label="⬅ Terug naar Home")

    st.header("Filters")
    widget_materiaal_prijs()

st.title("Prijsontwikkelingen")

st.caption(f"Gefilterd op materiaal: **{ss.selected_materiaal_value}**")
filtered_df = ss.prijzen_df[['Jaar',ss.selected_materiaal_value]].dropna()

st.markdown("""
    De prijsontwikkelingen zijn uitdrukt met behulp van de **producentenprijsindex (PPI) over de geselecteerde materialen**. De PPI is een **economische indicator** die de gemiddelde prijsveranderingen meet die **producenten ontvangen voor deze geleverde materialen**. Het gaat dus om prijzen op het **niveau van de producent**. Dit maakt de PPI een belangrijke maatstaf voor inflatie voor de inkopers van de materialen (bron: investingnomads.nl).
            """)

# Ensure datetime
x_dt = pd.to_datetime(filtered_df['Jaar'])

# Convert to numeric for regression
x_num = x_dt.dt.year + (x_dt.dt.month - 1) / 12
x_labels = x_dt.dt.strftime('%Y-%m')
y = filtered_df[ss.selected_materiaal_value].astype(float)*100

# Fit linear regression
X = sm.add_constant(x_num)
model = sm.OLS(y, X).fit()
y_fit = model.predict(X)

# Calculate residuals and std deviation
residuals = y - y_fit
std_dev = np.std(residuals)

# Create ±1 std deviation band around the trendline
ci_upper = y_fit + std_dev
ci_lower = y_fit - std_dev

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.metric("Trend (slope)", f"{model.params[1]:.2f} PPI punten per jaar")
        st.write(
            f"Dit is de gemiddelde stijging van de prijs van {ss.selected_materiaal_value} "
            "in PPI-punten per jaar (index t.o.v. 2015 = 100)."
        )

        with st.expander("ℹ️ Interpretatie (klik om uit te klappen)"):
            st.markdown(f"""
                **Wat betekent dit?**  
                - De *slope* is de gemiddelde jaarlijkse verandering in de PPI-index (punten/jaar).  
                - Bijvoorbeeld: **+2.5** betekent dat de index gemiddeld **2.5 punten per jaar** stijgt.

                **Hoe lees je dit t.o.v. 2015=100?**  
                - Bij een start rond 100 betekent +2.5 dat je na 4 jaar grofweg rond **110** kunt zitten (ruwe trend, zonder schommelingen).

                **Let op**  
                - Dit is een lineaire trend: pieken/dalen (bv. corona, energiecrisis) worden “gemiddeld”.  
                - Kijk ook naar het betrouwbaarheidsinterval / p-value als je wil weten hoe zeker de trend is.
                """)
with col2:
    with st.container(border=True):
        st.metric("Spreiding (σ)", f"{std_dev:.2f} PPI punten")
        st.write(
            f"Dit is de gemiddelde fluctuatie van de prijs van {ss.selected_materiaal_value} "
            "rond de lineaire trend (in PPI-indexpunten, 2015=100)."
        )

        with st.expander("ℹ️ Interpretatie (klik om uit te klappen)"):
            st.markdown(f"""
                **Wat betekent σ?**  
                - σ is de standaarddeviatie van de residuen (de afwijkingen t.o.v. de trend).
                - Het geeft aan hoe sterk de prijs schommelt rond de structurele ontwikkeling.

                **Hoe lees je dit?**  
                - Bijvoorbeeld: **σ = 4.2** betekent dat de prijs typisch ongeveer ±4.2 indexpunten rond de trend beweegt.
                - Ongeveer 68% van de observaties ligt binnen ±1σ.
                - Ongeveer 95% ligt binnen ±2σ (bij benadering normaal verdeeld).

                **Interpretatie in beleid / risico-context**  
                - Lage σ → stabiele markt.
                - Hoge σ → volatiele markt (meer onzekerheid).
                - Vergelijk σ tussen materialen om volatiliteit te beoordelen.
                """)

st.markdown("""
   
    Deze pagina toont de volgende informatie voor de gekozen grondstof:
    1.	de **trendlijn** (stijging of daling over een periode) en 
    2.	de **fluctuatie** van de materiaalprijzen over een periode.

    Voor meubelproductenten heeft de **trendlijn** betrekking op de prijsstrategiën, investeringsbeslissingen en het risicobeheer bij de productie van meubels. Bij een stijgende trendlijn betekent dit: 
    - Hogere grondstofkosten. Meubelmakers zijn sterk afhankelijk van de gekozen grondstoffen. Een stijgende PPI betekent dat deze materialen duurder worden, wat direct de productiekosten verhoogt.
    - Druk op marges en prijsstrategie. Als meubelmakers de hogere kosten niet volledig kunnen doorberekenen aan klanten, daalt hun winstgevendheid. Dit kan leiden tot prijsindexatie in contracten of het zoeken naar goedkopere materialen: 
    - Invloed op vraag en concurrentie. Hogere verkoopprijzen kunnen de vraag naar meubels verminderen, vooral in prijsgevoelige segmenten. Dit dwingt meubelmakers tot innovatie of kostenbesparing. 

    Een sterke **fluctuatie** zorgt voor onzekerheid in kosten, prijsbeleid contractafspraken en margedruk.

            """)

events = [
    {"date": "2020-03-11", "label": "COVID-19", "color": "gray", "dash": "dot", "width": 3},
    {"date": "2022-02-24", "label": "Invasie Oekraïne", "color": "green", "dash": "dash", "width": 4,},
    #{"date": "2023-12-06", "label": "Pieter Jarig", "color": "purple", "dash": "solid", "width": 10,}
]

#Mogelijke dash opties: "solid", "dot", "dash", "longdash", "dashdot", "longdashdot"

# Plot
fig = go.Figure()

# Original data
fig.add_trace(go.Scatter(
    x=x_labels,
    y=y,
    mode='lines+markers',
    name=f"Historisch prijs van {ss.selected_materiaal_value}",
    line=dict(color='blue', width=3),
    marker=dict(size=6)
))

# Trendline
fig.add_trace(go.Scatter(
    x=x_labels,
    y=y_fit,
    mode='lines',
    name='Lineaire trend',
    line=dict(color='red', dash='dash')
))

# ±1σ prediction band
fig.add_trace(go.Scatter(
    x=list(x_labels) + list(x_labels[::-1]),
    y=list(ci_upper) + list(ci_lower[::-1]),
    fill='toself',
    fillcolor='rgba(0,100,255,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    name='Spreiding (±1σ)'
))



for e in events:
    x = pd.to_datetime(e["date"])
    fig.add_shape(
        type="line",
        x0=x, x1=x,
        y0=0, y1=1,
        xref="x", yref="paper",          # y in [0..1] over hele plothoogte
        line=dict(color=e["color"], width=e["width"], dash=e["dash"]),
        opacity=0.7,
    )
    fig.add_annotation(
        x=x, y=1, xref="x", yref="paper",
        text=e["label"],
        showarrow=False,
        xanchor="left",
        yanchor="bottom",
        bgcolor="white",
        bordercolor=e["color"],
        borderwidth=1,
        opacity=0.9,
    )

# Layout
fig.update_layout(
    xaxis_title="Jaar",
    yaxis_title="Producentenprijsindex (2015 = 100)",
    template="plotly_white",
    **COMMON_LAYOUT,
)

st.plotly_chart(fig, use_container_width=True)


