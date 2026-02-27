import streamlit as st

ss = st.session_state

@st.cache_data(show_spinner=False)
def get_prijs_kpi(materials_list):
    variance = ss.prijzen_df.drop('Jaar', axis = 1).std().rename('risk2').reset_index().rename(columns = {'index' : 'materiaal'})
    return variance.loc[lambda d: d['materiaal'].isin(materials_list)]

@st.cache_data(show_spinner=False)
def get_levzeker(materials_list):
        wgi = ss.geo_df.merge(ss.wgi_df, on = 'ISO').groupby('material').apply(lambda g: (g['market_share'] * g['governance_score']).sum()).rename('wgi_score')
        return wgi.reset_index().loc[lambda d: d['material'].isin(materials_list)][['material','wgi_score']].rename(columns = {'wgi_score' : 'supply_risk'})


def widget_branche():
    OPTIONS = ["Meubelmakers", "Interieurbouw"]

    if "branche_value" not in ss:
        ss.branche_value = OPTIONS[0]

    def _sync():
        ss.branche_value = ss.branche_widget

    st.selectbox(
        "Branche",
        OPTIONS,
        index=OPTIONS.index(ss.branche_value),
        key="branche_widget",
        on_change=_sync,
    )

def widget_medewerkers():
    OPTIONS = ["0–50 fte", "51–250 fte", "250+ fte"]

    if "medewerkers_value" not in ss:
        ss.medewerkers_value = OPTIONS[0]

    def _sync():
        ss.medewerkers_value = ss.medewerkers_widget

    st.selectbox(
        "Aantal medewerkers",
        OPTIONS,
        index=OPTIONS.index(ss.medewerkers_value),
        key="medewerkers_widget",
        on_change=_sync,
    )

def widget_omzet():
    OPTIONS = ["<€10M", "<€50M", ">€50M"]

    if "omzet_value" not in ss:
        ss.omzet_value = OPTIONS[0]

    def _sync():
        ss.omzet_value = ss.omzet_widget

    st.selectbox(
        "Omzet",
        OPTIONS,
        index=OPTIONS.index(ss.omzet_value),
        key="omzet_widget",
        on_change=_sync,
    )

def widget_klantsegment():
    OPTIONS = ["Laag", "Midden", "Hoog"]

    if "klantsegment_value" not in ss:
        ss.klantsegment_value = OPTIONS[0]

    def _sync():
        ss.klantsegment_value = ss.klantsegment_widget

    st.selectbox(
        "Klantsegment",
        OPTIONS,
        index=OPTIONS.index(ss.klantsegment_value),
        key="klantsegment_widget",
        on_change=_sync,
    )


def widget_klanttype():
    OPTIONS_KLANTTYPE = ["B2C", "B2B", "Overheid"]

    if 'klanttype_value' not in ss:
        ss.klanttype_value = OPTIONS_KLANTTYPE[0]

    # 2) keep widget key separate; copy -> value on change
    def _sync():
        st.session_state["klanttype_value"] = st.session_state["klanttype_widget"]

    st.selectbox(
        "Klanttype",
        OPTIONS_KLANTTYPE,
        index=OPTIONS_KLANTTYPE.index(st.session_state["klanttype_value"]),
        key="klanttype_widget",
        on_change = _sync
    )

def widget_materialen():
    OPTIONS = list(set(ss.prijzen_df.drop("Jaar", axis=1).columns.tolist()) | set(ss.geo_df['material'].unique()))

    if "selected_materials_value" not in ss:
        ss.selected_materials_value = ['Hout - Multiplex', 'Polyurethaan', 'Wol', 'RVS 305']

    if 'df_now_prijs' not in ss:
        ss.df_now_prijs = get_prijs_kpi(tuple(ss.selected_materials_value))

    if 'df_now_lev' not in ss:
        ss.df_now_lev = get_levzeker(tuple(ss.selected_materials_value))

    def _sync():
        ss.selected_materials_value = ss.selected_materials_widget
        ss.df_now_prijs = get_prijs_kpi(tuple(ss.selected_materials_value))
        ss.df_now_lev = get_levzeker(tuple(ss.selected_materials_value))

    st.multiselect(
        "Materialen",
        OPTIONS,
        default=ss.selected_materials_value,
        key="selected_materials_widget",
        on_change=_sync,
    )

def widget_materiaal_prijs():

    OPTIONS_MATERIAAL = list(set(ss.prijzen_df.drop("Jaar", axis=1).columns.tolist()))

    if 'selected_materiaal_value' not in ss:
        ss.selected_materiaal_value = 'Katoen'

    def _sync():
        ss.selected_materiaal_value = ss.selected_materiaal_widget

    st.selectbox(
        "Materiaal",
        OPTIONS_MATERIAAL,
        index=OPTIONS_MATERIAAL.index(ss["selected_materiaal_value"]),
        key = 'selected_materiaal_widget',
        on_change = _sync
    )

def widget_materiaal_lev():

    OPTIONS_MATERIAAL = list(set(ss.geo_df['material'].unique()))

    if 'selected_materiaal_value' not in ss:
        ss.selected_materiaal_value = 'Katoen'

    def _sync():
        ss.selected_materiaal_value = ss.selected_materiaal_widget

    st.selectbox(
        "Materiaal",
        OPTIONS_MATERIAAL,
        index=OPTIONS_MATERIAAL.index(ss["selected_materiaal_value"]),
        key = 'selected_materiaal_widget',
        on_change = _sync
    )