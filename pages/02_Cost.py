import streamlit as st
st.set_page_config(page_title="Cost", layout="wide")

CATEGORY = "Cost"
st.title(CATEGORY)
st.write("Simple drill-down for **Cost**. Replace the tree with your own structure.")

TREE = {
    "CapEx": {"Hardware": ["Servers", "Switches"], "Facilities": ["Racks", "Cooling"]},
    "OpEx": {"Energy": ["kWh", "Demand Charges"], "Licenses": ["SaaS", "Support"]},
}

PREFIX = "cost_"
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

st.caption("Breadcrumb: Home / Cost")
st.page_link("Home.py", label="⬅ Back to Home")
