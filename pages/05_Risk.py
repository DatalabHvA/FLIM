import streamlit as st
st.set_page_config(page_title="Risk", layout="wide")

CATEGORY = "Risk"
st.title(CATEGORY)
st.write("Drill-down demo for **Risk**.")

TREE = {
    "Operational": {"Incidents": ["MTTR", "Change Fail"], "Resilience": ["Backups", "DR"]},
    "Supply Chain": {"Vendors": ["Concentration", "SLA"], "Geopolitics": ["Tariffs", "Sanctions"]},
}

PREFIX = "risk_"
lvl1 = st.selectbox("Choose a top-level topic:", list(TREE.keys()), key=PREFIX+"lvl1")
if lvl1:
    lvl2_keys = list(TREE[lvl1].keys())
    lvl2 = st.selectbox("Choose a subtopic:", lvl2_keys, key=PREFIX+"lvl2")
    if lvl2:
        lvl3_list = TREE[lvl1][lvl2]
        leaf = st.selectbox("Choose a detail:", lvl3_list, key=PREFIX+"lvl3")
        st.markdown(
            f"### You selected\n- **Topic:** {lvl1}\n- **Subtopic:** {lvl2}\n- **Detail:** {leaf}"
        )

st.caption("Breadcrumb: Home / Risk")
st.page_link("Home.py", label="⬅ Back to Home")
