import plotly.graph_objects as go
import streamlit as st

class Graph:
    def create_bullion_chart(self, items_df, city_name):
        bullion = items_df[items_df['group'] == 'Bullion']
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=bullion['item'],
            y=bullion['price'],
            text=[f"₹{p:,.2f}" for p in bullion['price']],
            textposition="auto",
            marker_color=['#FFD700', '#C0C0C0'],
            name="Bullion (₹)"
        ))
        fig.update_layout(
            title=f"Bullion Rates in {city_name} (Gold 10g vs Silver 1kg)",
            yaxis_title="Price (₹ INR)",
            height=320,
            template="plotly_dark",
            margin=dict(l=30, r=30, t=40, b=30)
        )
        return fig

    def create_fuel_chart(self, items_df, city_name):
        fuel = items_df[items_df['group'] == 'Fuel']
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=fuel['item'],
            y=fuel['price'],
            text=[f"₹{p:.2f} / L" for p in fuel['price']],
            textposition="auto",
            marker_color=['#FF5722', '#00BCD4'],
            name="Fuel (₹/L)"
        ))
        fig.update_layout(
            title=f"Fuel Prices in {city_name} (₹ per Litre)",
            yaxis_title="Rate (₹ / Litre)",
            height=320,
            template="plotly_dark",
            margin=dict(l=30, r=30, t=40, b=30)
        )
        return fig

    def create_history_chart(self, history_df, city_name):
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=history_df["Date"],
            y=history_df["Gold (10g)"],
            mode='lines+markers',
            name='24K Gold 10g',
            line=dict(color='#FFD700', width=2.5)
        ))
        fig.add_trace(go.Scatter(
            x=history_df["Date"],
            y=history_df["Silver (1kg)"],
            mode='lines+markers',
            name='Silver 1kg',
            line=dict(color='#00E676', width=2.5)
        ))
        fig.update_layout(
            title=f"7-Day Benchmark Trendline ({city_name})",
            xaxis_title="Date",
            yaxis_title="Price (₹ INR)",
            height=340,
            template="plotly_dark",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=30, r=30, t=50, b=30)
        )
        return fig

    def create_weather_display(self, weather_data):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Temperature", f"{weather_data['temperature']}°C", delta=f"Feels like {weather_data['feels_like']}°C")
        with col2:
            st.metric("Humidity", f"{weather_data['humidity']}%")
        with col3:
            st.metric("Wind Speed", f"{weather_data['wind_speed']} km/h")
        with col4:
            st.markdown(f"**Sky:** {weather_data['condition']}")
            st.caption(f"Source: {weather_data['source']}")

        st.info(f"💡 **Comfort Telemetry:** {weather_data['insight']}")

    def create_summary_metrics(self, items_df, city_name):
        avg_change = items_df['change'].mean()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(f"Commodities Tracked ({city_name})", len(items_df))
        with col2:
            st.metric("Avg 24h Delta", f"{avg_change:+.2f}%")
        with col3:
            st.metric("Data Status", "Live Telemetry Sync", delta="Active")