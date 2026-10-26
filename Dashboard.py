import streamlit as st
from datetime import datetime as dt
from Data import Data, fetch_live_weather
from Graph import Graph

st.set_page_config(
    page_title="BharatPulse - Realtime Analytics Engine",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    st.title("BHARATPULSE REALTIME ANALYTICS 🇮🇳 📊")
    st.caption("City-Specific Live Commodity, Fuel & Meteorological Telemetry Across India")
    st.markdown("---")

    ds = Data()
    graph = Graph()

    # Sidebar Controls
    st.sidebar.header("Regional & Sync Controls")

    selected_city = st.sidebar.selectbox(
        "Select Target City",
        options=list(ds.cities.keys()),
        index=0
    )

    auto_refresh = st.sidebar.checkbox("Enable Auto Refresh", value=True)
    refresh_seconds = st.sidebar.slider("Refresh Interval (Seconds)", min_value=5, max_value=60, value=15, step=5)

    st.sidebar.markdown("### Engine Features:")
    st.sidebar.write(" ◉ Live Regional Commodity Spot Rates")
    st.sidebar.write(" ◉ Open-Meteo REST API (Cached 300s)")
    st.sidebar.write(" ◉ City-Specific Fuel & Bullion Delta")
    st.sidebar.write(" ◉ Native `st.fragment` Auto-Refresh")

    city_coords = ds.cities[selected_city]
    interval_arg = refresh_seconds if auto_refresh else None

    @st.fragment(run_every=interval_arg)
    def render_live_dashboard():
        current_time = dt.now().strftime("%H:%M:%S")
        st.success(f"Dashboard synchronized for **{selected_city}** at `{current_time} IST`")

        # 1. Fetch Real-time City Data
        items_df, history_df = ds.get_market_data(city_name=selected_city)
        weather_data = fetch_live_weather(city_coords["lat"], city_coords["lon"], selected_city)

        # 2. Summary Metrics
        st.subheader(f"Market Summary — {selected_city}")
        graph.create_summary_metrics(items_df, city_name=selected_city)

        # 3. Weather Telemetry
        st.subheader(f"Meteorological Telemetry — {selected_city}")
        graph.create_weather_display(weather_data)

        st.markdown("---")

        # 4. Market Visualizations
        st.subheader(f"Commodity & Fuel Rates — {selected_city}")

        # Trendline Chart
        st.plotly_chart(graph.create_history_chart(history_df, selected_city), use_container_width=True)

        # Grouped Charts (Bullion & Fuel separated)
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(graph.create_bullion_chart(items_df, selected_city), use_container_width=True)
        with c2:
            st.plotly_chart(graph.create_fuel_chart(items_df, selected_city), use_container_width=True)

        with st.expander(f"View {selected_city} Price Breakdown Table"):
            display_df = items_df[['group', 'item', 'price', 'unit', 'change']].copy()
            st.dataframe(display_df, use_container_width=True)

    # Render dashboard
    render_live_dashboard()

    st.markdown("---")
    c_left, c_right = st.columns(2)
    with c_left:
        st.caption("Engine: Streamlit | Plotly | Open-Meteo REST API | Pandas")
    with c_right:
        if st.button("Manual Force Refresh", key="manual_refresh"):
            st.rerun()


if __name__ == "__main__":
    main()