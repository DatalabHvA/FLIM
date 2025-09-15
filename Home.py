# Home.py
import streamlit as st
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events

st.set_page_config(page_title="Radar Navigation Demo", layout="wide")

st.title("Interactive Radar Navigation")
st.write(
    "Use the sliders in the sidebar to set the category scores, then click a point "
    "on the spider chart to jump to that category’s page."
)

# --- Categories & defaults ---
CATEGORIES = ["Performance", "Cost", "Sustainability", "User Experience", "Risk"]
DEFAULTS = [80, 55, 72, 66, 40]  # starting values

# --- Session state init for values ---
if "scores" not in st.session_state:
    st.session_state.scores = dict(zip(CATEGORIES, DEFAULTS))

# --- Sidebar form with sliders (all-in-one) ---
with st.sidebar:
    st.header("Set Scores")
    with st.form("score_form", clear_on_submit=False):
        new_values = {}
        for cat in CATEGORIES:
            new_values[cat] = st.slider(
                cat,
                min_value=0,
                max_value=100,
                value=int(st.session_state.scores.get(cat, 50)),
                step=1,
                key=f"slider_{cat}",
            )
        submitted = st.form_submit_button("Apply")
    if submitted:
        # Update the shared scores in one go
        st.session_state.scores.update(new_values)
        st.success("Scores updated")

# --- Build radar values from session state ---
values = [st.session_state.scores[cat] for cat in CATEGORIES]

# Close the loop for radar fill
values_loop = values + values[:1]
categories_loop = CATEGORIES + CATEGORIES[:1]

# --- Radar chart ---
fig = go.Figure()
fig.add_trace(
    go.Scatterpolar(
        r=values_loop,
        theta=categories_loop,
        fill="toself",
        name="Current",
        hovertemplate="<b>%{theta}</b><br>Score: %{r}<extra></extra>",
        mode="lines+markers",
        marker=dict(size=10),
    )
)
fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    margin=dict(l=20, r=20, t=30, b=20),
    showlegend=False,
)

st.caption("Tip: click on a marker at a category vertex to navigate.")
clicked_points = plotly_events(
    fig,
    click_event=True,
    hover_event=False,
    select_event=False,
    override_height=520,
    override_width="100%",
)

# --- Page switching helper ---
def switch_to_category(cat: str):
    mapping = {
        "Performance": "pages/01_Performance.py",
        "Cost": "pages/02_Cost.py",
        "Sustainability": "pages/03_Sustainability.py",
        "User Experience": "pages/04_User_Experience.py",
        "Risk": "pages/05_Risk.py",
    }
    target = mapping.get(cat)
    if target:
        st.switch_page(target)
    else:
        st.warning(f"No page is configured for category: {cat}")

# --- Handle click: map pointIndex to the category (account for closed loop point) ---
if clicked_points:
    idx = clicked_points[0].get("pointIndex", None)
    if isinstance(idx, int):
        # Because we closed the loop, the last point repeats index 0—normalize with modulo
        idx_norm = idx % len(CATEGORIES)
        switch_to_category(CATEGORIES[idx_norm])
    else:
        st.info("Click on a marker at a category vertex to navigate.")
