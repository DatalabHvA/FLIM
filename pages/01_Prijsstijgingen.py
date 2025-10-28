# pages/02_Leveringszekerheid_Map.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

COMMON_LAYOUT = dict(
    margin=dict(l=40, r=5, t=20, b=60),
    xaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
    yaxis=dict(showline=True, linecolor="black", mirror=True, tickfont=dict(size=11), title_standoff=10),
)
CHART_HEIGHT = 320

ss = st.session_state

st.set_page_config(page_title="Prijsontwikkelingen", layout="wide")

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

st.title("Prijsontwikkelingen")
st.page_link("Home.py", label="⬅ Terug naar Home")

st.caption(f"Gefilterd op materiaal: **{ss.selected_material_prijs}**")
filtered_df = ss.prijzen_df[['Jaar',ss.selected_material_prijs]].dropna()

# Ensure datetime
x_dt = pd.to_datetime(filtered_df['Jaar'])

# Convert to numeric for regression
x_num = x_dt.dt.year + (x_dt.dt.month - 1) / 12
x_labels = x_dt.dt.strftime('%Y-%m')
y = filtered_df[ss.selected_material_prijs].astype(float)*100

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
    with st.container(border = True):
        st.metric("Trend (slope)", f"{model.params[1]:.2f} PPI punten per jaar")
        st.write(f'Dit is gemiddelde stijging van de prijs van {ss.selected_material_prijs} in procentpunten ten opzichte van het 2015 niveau.')

with col2:
    with st.container(border = True):
        st.metric("Spreiding (σ)", f"{std_dev:.2f} PPI punten")
        st.write(f'Dit is gemiddelde fluctuatie van de prijs van {ss.selected_material_prijs} bovenop de trend in procentpunten ten opzichte van het 2015 niveau.')

# Plot
fig = go.Figure()

# Original data
fig.add_trace(go.Scatter(
    x=x_labels,
    y=y,
    mode='lines+markers',
    name=f"Historisch prijs van {ss.selected_material_prijs}",
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

# Layout
fig.update_layout(
    xaxis_title="Jaar",
    yaxis_title="Producentenprijsindex (2015 = 100)",
    template="plotly_white",
    **COMMON_LAYOUT,
)

st.plotly_chart(fig, use_container_width=True)
