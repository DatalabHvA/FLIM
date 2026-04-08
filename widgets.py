import uuid
from datetime import datetime
import pandas as pd
import streamlit as st
import textwrap
import gspread
import plotly.graph_objects as go

ss = st.session_state

def init_session_state():
    """Initialize all session state data. Call at the top of every page."""
    if "session_id" not in ss:
        ss.session_id = str(uuid.uuid4())
    if 'prijzen_df' not in ss:
        df1 = pd.read_excel('data/Analyse factoren.xlsx', sheet_name='Data per factor (incl kwal)')
        df1['Factor'] = df1['Factor'].ffill()
        df1 = df1.loc[lambda d: d.Factor == 'Prijsstijgingen']
        targets = set(df1.loc[df1['Data gebruikt'] == 'Ja']['ID'].dropna().unique().astype(int).astype(str))
        targets.add('ID')
        prijzen_indices = pd.read_excel('data/prijzen.xlsx').columns
        prijzen_indices = pd.Series(prijzen_indices).apply(lambda x: str(x).split('.')[0])
        indices = [i for i, x in enumerate(prijzen_indices) if str(x) in targets]
        ss.prijzen_df = pd.read_excel('data/prijzen.xlsx', skiprows=1).iloc[:, indices]
        ss.prijzen_df.columns = pd.Series(ss.prijzen_df.columns).apply(lambda x: x.split('.')[0])
    if 'geo_df' not in ss:
        ss.geo_df = pd.read_excel('data/material_market_share.xlsx').loc[lambda d: d.market_share > 0.03]
    if 'wgi_df' not in ss:
        ss.wgi_df = pd.read_excel('data/wgi_governance_scores_2023_with_iso3.xlsx')
    if 'klantvraag_df_b2c' not in ss:
        ss.klantvraag_df_b2c = pd.DataFrame({'Jaar': [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
                                             'Traditionele meubels': [100, 105.0, 110.1, 115.6, 121.3, 127.3, 133.6, 140.2],
                                             'Duurzame meubels': [100, 110.3, 121.7, 134.2, 148.0, 163.3, 180.1, 198.6]})
    if 'klantvraag_df_b2b' not in ss:
        ss.klantvraag_df_b2b = pd.DataFrame({'Jaar': [2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
                                             'Traditionele meubels': [100, 105.0, 110.1, 115.6, 121.3, 127.3, 133.6, 140.2],
                                             'Duurzame meubels': [100, 110.1, 121.2, 133.5, 146.9, 161.8, 178.1, 196.]})
    if 'klantvraag_overheid_df' not in ss:
        ss.klantvraag_overheid_df = pd.DataFrame({'years': [2020, 2030, 2050],
                                                  'normale': [90, 50, 0],
                                                  'circulair': [10, 50, 100]})
    if 'personeel_df' not in ss:
        ss.personeel_df = pd.DataFrame({'Categorie': ['Global Gen Z', 'Global millennials', 'Nederlandse Gen Z', 'Nederlands millennials'],
                                        'Opdracht_project': [0.5, 0.43, 0.41, 0.31],
                                        'Werkgever': [0.44, 0.4, 0.36, 0.29]})
    if 'selected_materiaal_value' not in ss:
        ss.selected_materiaal_value = 'Katoen'
    if 'selected_materials_value' not in ss:
        ss.selected_materials_value = ['Hout - Multiplex', 'Polyurethaan', 'Wol', 'RVS 305']
    if 'df_now_prijs' not in ss:
        ss.df_now_prijs = get_prijs_kpi(tuple(ss.selected_materials_value))
    if 'df_now_lev' not in ss:
        ss.df_now_lev = get_levzeker(tuple(ss.selected_materials_value))

# --- Google Sheets logging ---
_SHEET_NAME = "FLIM log"
_TAB_NAME = "Blad1"

def log_event(page: str, event_type: str, value: str = ""):
    try:
        client = gspread.service_account_from_dict(dict(st.secrets["gcp_service_account"]))
        sheet = client.open(_SHEET_NAME).worksheet(_TAB_NAME)
        sheet.append_row([datetime.utcnow().isoformat(), ss.session_id, page, event_type, value])
    except Exception:
        pass  # never crash the app due to logging

@st.cache_data(show_spinner=False)
def get_prijs_kpi(materials_list):
    variance = ss.prijzen_df.drop('Jaar', axis=1).std().rename('risk2').reset_index().rename(columns={'index': 'materiaal'})
    result = variance.loc[lambda d: d['materiaal'].isin(materials_list)]
    missing = set(materials_list) - set(result['materiaal'])
    if missing:
        result = pd.concat([result, pd.DataFrame({'materiaal': list(missing), 'risk2': float('nan')})], ignore_index=True)
    return result

@st.cache_data(show_spinner=False)
def get_levzeker(materials_list):
    wgi = ss.geo_df.merge(ss.wgi_df, on='ISO').groupby('material').apply(lambda g: (g['market_share'] * g['governance_score']).sum()).rename('wgi_score')
    result = wgi.reset_index().loc[lambda d: d['material'].isin(materials_list)][['material', 'wgi_score']].rename(columns={'wgi_score': 'supply_risk'})
    missing = set(materials_list) - set(result['material'])
    if missing:
        result = pd.concat([result, pd.DataFrame({'material': list(missing), 'supply_risk': float('nan')})], ignore_index=True)
    return result


@st.cache_data(show_spinner=False)
def make_klantvraag_scatter_b2b(sel_hist_df: pd.DataFrame):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Traditionele meubels']],
        mode='lines+markers',
        name='Traditionele meubels (CAGR 4,95%)',
        line=dict(color='black', width=3),
        marker=dict(size=6)
    ))
    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Duurzame meubels']],
        mode='lines+markers',
        name='Duurzame meubels (CAGR 10,1%)',
        line=dict(color='green', width=3),
        marker=dict(size=6)
    ))
    fig.update_layout(
        xaxis_title="Jaar", yaxis_title="Index (2023 = 100)", template="plotly_white",
        margin=dict(l=40, r=15, t=20, b=70),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
    )
    return fig

@st.cache_data(show_spinner=False)
def make_klantvraag_scatter_b2c(sel_hist_df: pd.DataFrame):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Traditionele meubels']],
        mode='lines+markers',
        name='Traditionele meubels (CAGR 4,95%)',
        line=dict(color='black', width=3),
        marker=dict(size=6)
    ))
    fig.add_trace(go.Scatter(
        x=[str(x) for x in sel_hist_df['Jaar']],
        y=[float(x) for x in sel_hist_df['Duurzame meubels']],
        mode='lines+markers',
        name='Duurzame meubels (CAGR 10,3%)',
        line=dict(color='green', width=3),
        marker=dict(size=6)
    ))
    fig.update_layout(
        xaxis_title="Jaar", yaxis_title="Index (2023 = 100)", template="plotly_white",
        margin=dict(l=40, r=15, t=20, b=70),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
    )
    return fig

def widget_branche():
    OPTIONS = ["Meubelmakers", "Interieurbouw"]

    if "branche_value" not in ss:
        ss.branche_value = OPTIONS[0]

    def _sync():
        ss.branche_value = ss.branche_widget
        log_event("sidebar", "widget_branche", ss.branche_value)

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
        log_event("sidebar", "widget_medewerkers", ss.medewerkers_value)

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
        log_event("sidebar", "widget_omzet", ss.omzet_value)

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
        log_event("sidebar", "widget_klantsegment", ss.klantsegment_value)

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
        log_event("sidebar", "widget_klanttype", st.session_state["klanttype_value"])

    st.selectbox(
        "Klanttype",
        OPTIONS_KLANTTYPE,
        index=OPTIONS_KLANTTYPE.index(st.session_state["klanttype_value"]),
        key="klanttype_widget",
        on_change = _sync
    )

def widget_materialen():
    OPTIONS = sorted(set(ss.prijzen_df.drop("Jaar", axis=1).columns.tolist()) | set(ss.geo_df['material'].unique()))

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
        log_event("sidebar", "widget_materialen", ", ".join(ss.selected_materials_value))

    st.multiselect(
        "Grondstoffen en materialen",
        OPTIONS,
        default=ss.selected_materials_value,
        key="selected_materials_widget",
        on_change=_sync,
    )

def widget_materiaal_prijs():

    OPTIONS_MATERIAAL = sorted(set(ss.prijzen_df.drop("Jaar", axis=1).columns.tolist()))

    if 'selected_materiaal_value' not in ss:
        ss.selected_materiaal_value = 'Katoen'

    def _sync():
        ss.selected_materiaal_value = ss.selected_materiaal_widget
        log_event("Prijsstijgingen", "widget_materiaal", ss.selected_materiaal_value)

    st.selectbox(
        "Materiaal",
        OPTIONS_MATERIAAL,
        index=OPTIONS_MATERIAAL.index(ss["selected_materiaal_value"]),
        key = 'selected_materiaal_widget',
        on_change = _sync
    )

def widget_materiaal_lev():

    OPTIONS_MATERIAAL = sorted(set(ss.geo_df['material'].unique()))

    if 'selected_materiaal_value' not in ss:
        ss.selected_materiaal_value = 'Katoen'

    def _sync():
        ss.selected_materiaal_value = ss.selected_materiaal_widget
        log_event("Leveringszekerheid", "widget_materiaal", ss.selected_materiaal_value)

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
