# pages/03_Klantvraag_Bars.py
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Klantvraag • Analyse", layout="wide")

st.title("Klantvraag — Analyse")
st.page_link("Home.py", label="⬅ Terug naar Home")

# Demo horizontal bars — replace with your own dataset
rng = np.random.default_rng(3)
labels = ["Segment A", "Segment B", "Segment C", "Segment D", "Segment E"]
vals = np.clip(rng.normal(70, 12, size=len(labels)), 20, 100).round(1)

fig = go.Figure(
    data=[go.Bar(x=vals, y=labels, orientation="h",
                 hovertemplate="%{y}: %{x:.1f}<extra></extra>")]
)
fig.update_layout(
    height=520, margin=dict(l=10, r=10, t=30, b=10),
    xaxis_title="Index", yaxis_title=None, showlegend=False
)
st.plotly_chart(fig, use_container_width=True)
