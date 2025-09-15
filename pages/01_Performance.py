import streamlit as st

st.set_page_config(page_title="Performance", layout="wide")

CATEGORY = "Performance"
st.title(CATEGORY)
st.write(
    "This page shows details and a small drill-down tree for **Performance**. "
    "You can adapt the tree structure below to your real content."
)

# --- Simple, extensible drill-down tree demo ---
# You can replace this structure (dict of dicts) with your real tree.
TREE = {
    "CPU": {
        "Single-Core": ["Latency", "IPC", "Thermals"],
        "Multi-Core": ["Throughput", "Scaling"],
    },
    "GPU": {
        "Rendering": ["Raster", "Ray Tracing"],
        "Compute": ["Tensor Ops", "FP16/FP32"],
    },
    "Storage": {
        "SSD": ["Sequential", "Random I/O"],
        "HDD": ["Throughput", "Reliability"],
    },
}

# Keep a unique key prefix per page to avoid widget collisions across pages
PREFIX = "perf_"

# Level 1
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

# Optional: show a breadcrumb
st.caption("Breadcrumb: Home / Performance")
st.page_link("Home.py", label="⬅ Back to Home")
