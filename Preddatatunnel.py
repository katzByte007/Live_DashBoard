import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Tunnel Operations Hub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with updated colors and mobile responsiveness
st.markdown("""
    <style>
        /* Previous CSS styles remain the same until metrics section */
        
        /* Updated metrics styling for mobile */
        [data-testid="stMetric"] {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.1), rgba(244, 114, 182, 0.1));
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 0.5rem !important;
            margin-bottom: 0.5rem !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        
        /* Make graphs more mobile-friendly */
        .js-plotly-plot {
            max-width: 100vw !important;
            padding: 0.3rem !important;
            overflow-x: hidden !important;
        }
        
        /* Power breakdown section */
        .power-breakdown {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.15), rgba(244, 114, 182, 0.15));
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
        }
        
        .power-item {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(244, 114, 182, 0.2);
        }
        
        .power-total {
            font-weight: bold;
            padding-top: 0.5rem;
            border-top: 2px solid rgba(244, 114, 182, 0.4);
        }
        
        /* Alert section at top */
        .top-alerts {
            margin-bottom: 1.5rem;
            background: linear-gradient(145deg, rgba(255, 107, 107, 0.1), rgba(147, 51, 234, 0.1));
            border-radius: 10px;
            padding: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title with gradient
st.markdown('<p class="gradient-text">Tunnel Operations Hub</p>', unsafe_allow_html=True)
st.markdown(f'<p class="timestamp">Live Updates • {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>', unsafe_allow_html=True)

# Critical Alerts Section - Moved to top
st.markdown('<div class="top-alerts">', unsafe_allow_html=True)
critical_alerts = [
    "🚨 HIGH PRIORITY: CO2 levels approaching threshold in Section B",
    "⚠️ URGENT: Predicted power surge in next 30 minutes"
]
for alert in critical_alerts:
    st.error(alert)
st.markdown('</div>', unsafe_allow_html=True)

# Sample data with updated values
tunnel_data = {
    "totalVehicles": 1254,
    "maxExhaustPower": "2500 kW",
    "maxTemperature": "35°C",
    "co2Level": "850 ppm",
    "no2Level": "180 µg/m³",
    "lightingPower": "450 kW",
    "jetfanPower": "850 kW",
    "dgPower": "550 kW",
    "totalPower": "1850 kW",
    "predictedExhaustPower": "2800 kW",
    "predictedCongestion": "75%",
    "predictedAirQuality": "Moderate",
    "predictedMaintenance": "4 days"
}

# Current Stats Section with air quality metrics
st.header('Current Statistics')
cols = st.columns(6)
metrics = [
    ("Total Vehicles", tunnel_data["totalVehicles"], "↑ 12%"),
    ("Temperature", tunnel_data["maxTemperature"], "↑ 5%"),
    ("CO₂ Level", tunnel_data["co2Level"], "↑ 15%"),
    ("NO₂ Level", tunnel_data["no2Level"], "↑ 8%"),
    ("Exhaust Power", tunnel_data["maxExhaustPower"], "→ 0%"),
    ("Total Power", tunnel_data["totalPower"], "↓ 8%")
]
for col, (label, value, delta) in zip(cols, metrics):
    with col:
        st.metric(label, value, delta)

# Power Breakdown Section
st.markdown("""
    <div class="power-breakdown">
        <div class="power-item">
            <span>Lighting Power</span>
            <span>450 kW</span>
        </div>
        <div class="power-item">
            <span>Jetfan Power</span>
            <span>850 kW</span>
        </div>
        <div class="power-item">
            <span>DG Power</span>
            <span>550 kW</span>
        </div>
        <div class="power-item power-total">
            <span>Total Power Usage</span>
            <span>1850 kW</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Predictive Insights Section
st.header('Predictive Insights')
cols = st.columns(4)
predictions = [
    ("Required Exhaust Power", tunnel_data["predictedExhaustPower"], "89% confidence"),
    ("Expected Congestion", tunnel_data["predictedCongestion"], "85% confidence"),
    ("Air Quality Forecast", tunnel_data["predictedAirQuality"], "92% confidence"),
    ("Next Maintenance", tunnel_data["predictedMaintenance"], "87% confidence")
]
for col, (label, value, conf) in zip(cols, predictions):
    with col:
        st.metric(label, value, conf)

# Updated Traffic Flow Analysis with better mobile responsiveness
st.header('Traffic Flow Analysis')
fig_traffic = px.area(hourly_data, x='hour', y='vehicles')
fig_traffic.update_layout(
    height=250,  # Further reduced height
    margin=dict(l=10, r=10, t=20, b=10),  # Minimal margins
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#f472b6',
    showlegend=False,
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True  # Disable zoom on mobile
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True  # Disable zoom on mobile
    )
)
fig_traffic.update_traces(
    fill='tozeroy',
    line=dict(color='#f472b6'),
    fillcolor='rgba(244, 114, 182, 0.2)'
)
st.plotly_chart(fig_traffic, use_container_width=True, config={'displayModeBar': False})  # Hide mode bar for mobile

# Updated Power Prediction graph
st.header('Predicted vs Actual Exhaust Power')
fig_power = go.Figure()
fig_power.add_trace(go.Scatter(
    x=prediction_data['time'],
    y=prediction_data['predicted'],
    name='Predicted Power',
    line=dict(color='#9333ea', width=2)
))
fig_power.update_layout(
    height=250,  # Further reduced height
    margin=dict(l=10, r=10, t=20, b=10),  # Minimal margins
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#f472b6',
    showlegend=False,
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True  # Disable zoom on mobile
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True  # Disable zoom on mobile
    )
)
st.plotly_chart(fig_power, use_container_width=True, config={'displayModeBar': False})  # Hide mode bar for mobile

# Secondary Alerts Section
st.header('Other Alerts')
alerts = [
    "⚠️ Forecast: Air quality may deteriorate in Section C - Consider increasing ventilation",
    "🔧 Maintenance Alert: Fan system efficiency predicted to drop below threshold in 4 days"
]
for alert in alerts:
    st.warning(alert)

# Add refresh button with custom styling
col1, col2, col3 = st.columns([4,1,4])
with col2:
    st.button('🔄 Refresh Data')
