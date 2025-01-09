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

# Complete CSS with all styles
st.markdown("""
    <style>
        /* Existing styles remain the same... */
        
        /* Enhanced Critical Alerts Styling */
        .top-alerts {
            margin-bottom: 1.5rem;
            background: linear-gradient(145deg, rgba(255, 0, 0, 0.15), rgba(147, 51, 234, 0.2));
            border-radius: 10px;
            padding: 0.5rem;
            border: 1px solid rgba(255, 107, 107, 0.3);
        }
        
        /* Brighten the error alerts */
        [data-testid="stAlert"] {
            background: linear-gradient(145deg, rgba(255, 0, 0, 0.15), rgba(255, 0, 0, 0.05)) !important;
            border: 1px solid rgba(255, 107, 107, 0.3) !important;
            border-radius: 10px !important;
            color: #fff !important;
            padding: 0.8rem !important;
            margin-bottom: 0.8rem !important;
            text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.1);
        }
        
        /* Style the alert icon and text */
        [data-testid="stAlert"] > div:first-child {
            color: #ff6b6b !important;
            font-weight: 600 !important;
        }
        
        /* Make the alert text brighter */
        [data-testid="stAlert"] p {
            color: #fff !important;
            font-weight: 500 !important;
            letter-spacing: 0.3px;
        }
        
        /* Add pulsing animation for urgent alerts */
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 107, 107, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(255, 107, 107, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 107, 107, 0); }
        }
        
        [data-testid="stAlert"] {
            animation: pulse 2s infinite;
        }
    </style>
""", unsafe_allow_html=True)

# Critical Alerts Section remains the same
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
    ("Expected Traffic", tunnel_data["predictedCongestion"], "85% confidence"),
    ("Air Quality Forecast", tunnel_data["predictedAirQuality"], "92% confidence"),
    ("Next Maintenance", tunnel_data["predictedMaintenance"], "87% confidence")
]
for col, (label, value, conf) in zip(cols, predictions):
    with col:
        st.metric(label, value, conf)

# Traffic Flow Analysis with mobile optimization
st.header('Traffic Flow Analysis')
fig_traffic = px.area(hourly_data, x='hour', y='vehicles')
fig_traffic.update_layout(
    height=250,
    margin=dict(l=10, r=10, t=20, b=10),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#f472b6',
    showlegend=False,
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True
    )
)
fig_traffic.update_traces(
    fill='tozeroy',
    line=dict(color='#f472b6'),
    fillcolor='rgba(244, 114, 182, 0.2)'
)
st.plotly_chart(fig_traffic, use_container_width=True, config={'displayModeBar': False})

# Power Prediction graph with mobile optimization
st.header('Predicted vs Actual Exhaust Power')
fig_power = go.Figure()
fig_power.add_trace(go.Scatter(
    x=prediction_data['time'],
    y=prediction_data['predicted'],
    name='Predicted Power',
    line=dict(color='#9333ea', width=2)
))
fig_power.update_layout(
    height=250,
    margin=dict(l=10, r=10, t=20, b=10),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#f472b6',
    showlegend=False,
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)',
        fixedrange=True
    )
)
st.plotly_chart(fig_power, use_container_width=True, config={'displayModeBar': False})

# Secondary Alerts Section
st.header('Other Alerts')
alerts = [
    "⚠️ Forecast: Air quality may deteriorate in Section C - Consider increasing ventilation",
    "🔧 Maintenance Alert: Fan system efficiency predicted to drop below threshold in 4 days"
]
for alert in alerts:
    st.warning(alert)

# Refresh button
col1, col2, col3 = st.columns([4,1,4])
with col2:
    st.button('🔄 Refresh Data')
