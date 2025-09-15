import streamlit as st
st.set_page_config(page_title="Sustainability", layout="wide")

CATEGORY = "Sustainability"
st.title(CATEGORY)
st.write("Drill-down demo for **Sustainability** metrics and levers.")

TREE = {
    "Emissions": {"Scopes": ["Scope 1", "Scope 2", "Scope 3"], "Offsets": ["CDR", "RECs"]},
    "Materials": {"Recycled": ["Steel", "Plastics"], "Renewables": ["Biofuels", "Wood"]},
}

PREFIX = "sus_"
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

st.caption("Breadcrumb: Home / Sustainability")
st.page_link("Home.py", label="⬅ Back to Home")
