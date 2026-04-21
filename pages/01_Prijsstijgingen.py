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
init_session_state()
st.set_page_config(page_title="Prijsontwikkelingen", layout="wide")
log_event("Prijsstijgingen", "page_load")

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
    widget_materiaal_prijs()

st.title("Prijsontwikkelingen")

st.caption(f"Gefilterd op materiaal: **{ss.selected_materiaal_value}**")
filtered_df = ss.prijzen_df[['Jaar',ss.selected_materiaal_value]].dropna()

st.markdown("""
    De prijsontwikkelingen zijn berekend met de **producentenprijsindex (PPI)** voor de gekozen materialen.
    De PPI laat zien hoe de **gemiddelde prijzen veranderen die grondstoffen- of materiaalfabrikanten krijgen** voor hun producten. Het gaat dus om **prijzen bij de meubelproducent**, niet in de winkel.
    Voor inkopers is de PPI belangrijk, omdat hij laat zien **hoeveel duurder of goedkoper materialen worden**. Dat helpt om de **inflatie** (algemene prijsstijgingen) en **prijsschommelingen** voor deze materialen in te schatten.
    (bron: investingnomads.nl).
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
    name=f"Historische prijs van {ss.selected_materiaal_value}",
    line=dict(color='blue', width=3),
    marker=dict(size=6)
))

# Trendline
fig.add_trace(go.Scatter(
    x=x_labels,
    y=y_fit,
    mode='lines',
    name='Trendlijn',
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

st.plotly_chart(fig, width='stretch')


col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.metric("Trend (helling)", f"{model.params.iloc[1]:.2f} PPI punten per jaar")
        st.write(
            f"De helling toont de gemiddelde stijging van de prijs van {ss.selected_materiaal_value} "
            "in PPI-punten per jaar. Startindexwaarde (2015) = 100."
        )

        with st.expander("ℹ️ Uitleg (klik om uit te klappen)"):
            st.markdown(f"""
                **Wat betekent dit?**  
                - De *helling* is de gemiddelde jaarlijkse verandering in de PPI-index (punten/jaar).  
                - Bijvoorbeeld: **+2.5** betekent dat de prijsindex gemiddeld **2.5 punten per jaar** stijgt.

                **Hoe lees je dit t.o.v. 2015 met startindex 100?**  
                - Bij een start rond 100 betekent +2.5 dat je na 4 jaar ongeveer rond **110** kunt zitten (ruwe trend, zonder schommelingen).

                **Let op**  
                - Dit is een trend met een rechte lijn: kortdurende pieken/dalen (bv. corona, energiecrisis) worden “gemiddeld”.  
                - Kijk ook naar het betrouwbaarheidsinterval / p-value als je wil weten hoe zeker de trend is.
                """)
with col2:
    with st.container(border=True):
        st.metric("Spreiding (σ)", f"{std_dev:.2f} PPI punten")
        st.write(
            f"Dit is de gemiddelde schommeling van de prijs van {ss.selected_materiaal_value} "
            "rond de trendlijn (in PPI-indexpunten). Startindexwaarde (2015) = 100."
        )

        with st.expander("ℹ️ Uitleg (klik om uit te klappen)"):
            st.markdown(f"""
                **Wat betekent de spreiding (σ)?**  
                - De spreiding (σ) is de standaardafwijking ten opzichte van de trendlijn.
                - Deze maat geeft aan hoe sterk de prijs schommelt rond de structurele prijsontwikkeling.

                **Hoe lees je dit?**  
                - Bijvoorbeeld: **σ = 4.2** betekent dat de prijs typisch ongeveer ±4.2 indexpunten rond de trend beweegt.
                - Ongeveer 68% van de meetpunten ligt binnen ±1σ.
                - Ongeveer 95% ligt binnen ±2σ (bij benadering normaal verdeeld).

                **Uitleg in beleid / risico-context**  
                - Een Lage spreiding σ betekent een stabiele markt met een lage prijsonzekerheid.
                - Een hoge spreiding σ betekent volatiele markt met een hoge prijsonzekerheid.
                - Vergelijk spreiding σ tussen materialen of grondstoffen om prijsonzekerheid zelf te beoordelen.
                """)


# Toelichtende tekst onder grafiek
st.markdown("""
   
    Deze grafiek toont de volgende informatie voor de gekozen grondstof:
    1.	de **trendlijn** (stijging of daling van de grondstof- of materiaalprijzen over een periode) en 
    2.	de **schommeling** van de grondstof- of materiaalprijzen over een periode.

    Voor meubelproductenten heeft de **trendlijn** betrekking op de prijsstrategiën, investeringsbeslissingen en het risicobeheer bij de productie van meubels. Bij een **stijgende trendlijn** betekent dit: 
    - **Hogere grondstofkosten**. Meubelproducenten zijn **sterk afhankelijk van de gekozen grondstoffen**. Een **stijgende PPI** betekent dat deze **materialen duurder** worden. Dit verhoogt de productiekosten direct.
    - Druk op marges en prijsbeleid. Als meubelmakers de **hogere kosten** niet volledig kunnen doorberekenen aan klanten, **daalt hun winstgevendheid**. Dit kan leiden tot prijsindexatie in contracten of het zoeken naar goedkopere materialen: 
    - Invloed op vraag en concurrentie. Als hogere kosten leiden tot **hogere verkoopprijzen**, kann de vraag naar meubels verminderen. Dit dwingt meubelmakers tot **innovatie of kostenbesparing**. 

    Een sterke **schommeling** zorgt voor **onzekerheid in kosten**. Dit heeft invloed op het margedruk, prijsbeleid en contractafspraken.

            """)
