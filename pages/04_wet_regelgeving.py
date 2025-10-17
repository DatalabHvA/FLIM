import streamlit as st
from streamlit_plotly_events import plotly_events
import sys
sys.path.append("..")

from Home import get_heatmap_series, make_single_col_heatmap

st.set_page_config(page_title="Klantvraag", layout="wide")

CHART_HEIGHT = 300

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

st.title('Wet- en regelgeving')
st.page_link("Home.py", label="⬅ Terug naar Home")

heat_df = get_heatmap_series()

colorscale = [
    [0.0, '#ff0000'],  # strong red
    [1.0, '#ffe5e5']   # very light red
]
labels = tuple(heat_df["label"].tolist())
values = tuple(heat_df["value"].tolist())
fig = make_single_col_heatmap(labels, values, cmap = colorscale, height=CHART_HEIGHT)

clicks = plotly_events(
    fig,
    click_event=True, hover_event=False, select_event=False,
    override_height=CHART_HEIGHT+40, override_width="100%",
    key=f"evt_heatmap_{st.session_state.events_epoch}",
)
if clicks:
    # For Heatmap, Plotly returns y = row label (our 'label')
    sel_label = clicks[0].get("y")
    if sel_label:
        # Robust: set session state and (best-effort) URL param
        st.session_state["heatmap_label"] = sel_label
        st.write(sel_label)
        st.switch_page(target_page)
