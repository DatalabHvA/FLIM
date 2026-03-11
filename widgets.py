import streamlit as st
import textwrap

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
        "Grondstoffen en materialen",
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

def generate_table(fase, budget, vorm):

    markdown = f"""
        <table style="border-collapse: collapse; width: 70%; text-align: center; font-family: Arial;">
        <tr style="background-color:#d9d9d9;">
        <th style="border:1px solid #666; padding:12px;">
        Fase<br><br>
        <img src="https://raw.githubusercontent.com/DatalabHvA/FLIM/refs/heads/main/assets/route.png" width="60">
        </th>

        <th style="border:1px solid #666; padding:12px;">
        Aanvraagbaar budget<br>(dekking)<br><br>
        <img src="https://raw.githubusercontent.com/DatalabHvA/FLIM/refs/heads/main/assets/envelope.png" width="70">
        </th>

        <th style="border:1px solid #666; padding:12px;">
        Vorm<br><br>
        <img src="https://raw.githubusercontent.com/DatalabHvA/FLIM/refs/heads/main/assets/people.png" width="70">
        </th>
        </tr>

        <tr style="background-color:#efefef;">
        <td style="border:1px solid #666; padding:25px; font-style:italic; font-size:22px;">
        {fase}
        </td>

        <td style="border:1px solid #666; padding:25px; font-style:italic; font-size:22px;">
        {budget}
        </td>

        <td style="border:1px solid #666; padding:25px; font-style:italic; font-size:22px;">
        {vorm}
        </td>
        </tr>
        </table>
        """ 

    return markdown

def generate_badge(badge_number):

    html = textwrap.dedent(f"""
    <div style="
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding-top: 0px;
    padding-bottom: 8px;
    box-sizing: border-box;
    ">
        <div style="
        position: relative;
        width: 230px;
        height: 160px;
        border: 1.5px solid #bfbfbf;
        border-radius: 24px;
        background-color: #efefef;
        box-sizing: border-box;
        padding: 20px 16px 28px 16px;
        font-family: Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        ">

            <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 12px;
            ">
                <img src="https://raw.githubusercontent.com/DatalabHvA/FLIM/3a681e8c94d252c537ac0b57c8426e8cb0ead105/assets/coins.svg"
                style="width:64px;">
                <img src="https://raw.githubusercontent.com/DatalabHvA/FLIM/3a681e8c94d252c537ac0b57c8426e8cb0ead105/assets/hammer.svg"
                style="width:64px;">
            </div>

            <div style="
            text-align: center;
            font-size: 15px;
            font-weight: 700;
            line-height: 1.2;
            max-width: 150px;
            ">
                Boetes en Sancties
            </div>

            <div style="
            position:absolute;
            top:8px;
            right:10px;
            width:36px;
            height:36px;
            border-radius:50%;
            background:#e00000;
            color:white;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:18px;
            font-weight:700;
            box-shadow:0 2px 6px rgba(0,0,0,0.25);
            ">
                {badge_number}
            </div>

        </div>
    </div>
    """)

    return html

def generate_badge2(badge_number):

    html = textwrap.dedent(f"""
    <div style="
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding-top: 0px;
    padding-bottom: 18px;
    box-sizing: border-box;
    ">
        <div style="
        position: relative;
        width: 230px;
        height: 140px;
        border: 1.5px solid #bfbfbf;
        border-radius: 24px;
        background-color: #efefef;
        box-sizing: border-box;
        padding: 20px 16px 28px 16px;
        font-family: Arial, sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        ">

            <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 12px;
            ">
                <img src="https://raw.githubusercontent.com/DatalabHvA/FLIM/821c9d21b308180cc61e372fd6399e053f43dd9e/assets/cubes.svg"
                    style="width:72px; height:auto;">
            </div>

            <div style="
            text-align: center;
            font-size: 15px;
            font-weight: 700;
            line-height: 1.2;
            max-width: 180px;
            ">
                Keten en Markt
            </div>

            <div style="
            position:absolute;
            top:8px;
            right:10px;
            width:36px;
            height:36px;
            border-radius:50%;
            background:#e00000;
            color:white;
            display:flex;
            align-items:center;
            justify-content:center;
            font-size:18px;
            font-weight:700;
            box-shadow:0 2px 6px rgba(0,0,0,0.25);
            ">
                {badge_number}
            </div>

        </div>
    </div>
    """)

    return html
