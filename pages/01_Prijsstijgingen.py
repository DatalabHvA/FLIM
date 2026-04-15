# Layout
fig.update_layout(
    xaxis_title="Jaar",
    yaxis_title="Producentenprijsindex (2015 = 100)",
    template="plotly_white",
    **COMMON_LAYOUT,
)

# Grafiek eerst tonen
st.plotly_chart(fig, width='stretch')

# Daarna de twee kolommen
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.metric("Trend (helling)", f"{model.params.iloc[1]:.2f} PPI punten per jaar")
        st.write(
            f"De helling toont de gemiddelde stijging van de prijs van {ss.selected_materiaal_value} "
            "in PPI-punten per jaar. Startindexwaarde (2015) = 100."
        )

        with st.expander("ℹ️ Uitleg (klik om uit te klappen)"):
            st.markdown(f"""
                **Wat betekent dit?**  
                - De *helling* is de gemiddelde jaarlijkse verandering in de PPI-index (punten/jaar).  
                - Bijvoorbeeld: **+2.5** betekent dat de prijsindex gemiddeld **2.5 punten per jaar** stijgt.

                **Hoe lees je dit t.o.v. 2015 met startindex 100?**  
                - Bij een start rond 100 betekent +2.5 dat je na 4 jaar ongeveer rond **110** kunt zitten (ruwe trend, zonder schommelingen).

                **Let op**  
                - Dit is een trend met een rechte lijn: kortdurende pieken/dalen (bv. corona, energiecrisis) worden “gemiddeld”.  
                - Kijk ook naar het betrouwbaarheidsinterval / p-value als je wil weten hoe zeker de trend is.
                """)
with col2:
    with st.container(border=True):
        st.metric("Spreiding (σ)", f"{std_dev:.2f} PPI punten")
        st.write(
            f"Dit is de gemiddelde schommeling van de prijs van {ss.selected_materiaal_value} "
            "rond de trendlijn (in PPI-indexpunten). Startindexwaarde (2015) = 100."
        )

        with st.expander("ℹ️ Uitleg (klik om uit te klappen)"):
            st.markdown(f"""
                **Wat betekent de spreiding (σ)?**  
                - De spreiding (σ) is de standaardafwijking ten opzichte van de trendlijn.
                - Deze maat geeft aan hoe sterk de prijs schommelt rond de structurele prijsontwikkeling.

                **Hoe lees je dit?**  
                - Bijvoorbeeld: **σ = 4.2** betekent dat de prijs typisch ongeveer ±4.2 indexpunten rond de trend beweegt.
                - Ongeveer 68% van de meetpunten ligt binnen ±1σ.
                - Ongeveer 95% ligt binnen ±2σ (bij benadering normaal verdeeld).

                **Uitleg in beleid / risico-context**  
                - Een Lage spreiding σ betekent een stabiele markt met een lage prijsonzekerheid.
                - Een hoge spreiding σ betekent volatiele markt met een hoge prijsonzekerheid.
                - Vergelijk spreiding σ tussen materialen of grondstoffen om prijsonzekerheid zelf te beoordelen.
                """)
