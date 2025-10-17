import streamlit as st
from streamlit_plotly_events import plotly_events
import sys
sys.path.append("..")

from Home import get_heatmap_series, make_single_col_heatmap

st.set_page_config(page_title="Klantvraag", layout="wide")
ss = st.session_state
ss.setdefault("events_epoch", 0)       # to invalidate plotly_events widget state


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
st.write('Belangrijke wet- en regelgeving m.b.t. grondstoffen.')

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

c1, c2 = st.columns(2)
with c1:
    with st.container():
        st.subheader("Samenhang en doel wet- en regelgevingen")
        st.markdown("""
        **1. De circulaire economie wordt steeds vaker juridisch verankerd in zowel Nederlandse als Europese wetgeving.** 
                    
        Niet langer is circulariteit vrijblijvend of alleen “maatschappelijk wenselijk” – het wordt wettelijk verplichtend, met eisen over ontwerp, materialen, hergebruik en afvalfase.**

        - Producttransparantie via het Digitaal Productpaspoort (DPP)
        - Verschuiving van verantwoordelijkheid naar producenten (UPV)
            
        **2. Greenwashing tegengaan en speelveld gelijk maken**
                    
        Door het gebrek aan een uniforme standaard in Nederland kunnen bedrijven ongefundeerde duurzaamheidsclaims maken. Nieuwe wetgeving moet dit tegengaan en een gelijk speelveld creëren voor Nederlandse producenten. 
                    
        **3. Financiële risico's voor niet-actieve bedrijven**
                    
        Het niet tijdig inspelen op deze wetgeving heeft financiële risico's. Denk aan:
        - Kosten van non-compliance.
        - Geen toegang tot markten die circulariteit vereisen.
        - Verlies aan concurrentiekracht t.o.v. bedrijven die wél voldoen
                """)
with c2: 
    st.image('assets/wetgeving.png')

st.subheader("Wat betekent dit voor de branche?")
st.markdown("""
    - **MKB-bedrijven** moeten anticiperen op verplichtingen met hulp van tools (zoals FLIM).
    - **Ketenregie** wordt cruciaal: de informatie- en materiaalstromen moeten traceerbaar worden.
    - **Collectieve actie** (via brancheverenigingen zoals CBM) wordt noodzakelijk om de regeldruk behapbaar te maken.
    - **Compliance = concurrentiekracht** – bedrijven die voorbereid zijn, worden aantrekkelijker voor investeerders, klanten en partners.    
    """)    


