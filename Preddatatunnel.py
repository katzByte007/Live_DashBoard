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

# [Previous CSS styles remain unchanged]
st.markdown("""
    <style>
        /* Modern gradient background */
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #2d1b3d 50%, #1a1a2e 100%);
        }
        
        /* Gradient title */
        .gradient-text {
            background: linear-gradient(120deg, #ff6b6b, #f472b6, #9333ea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 42px !important;
            font-weight: 700 !important;
            margin-bottom: 0px !important;
        }
        
        /* Metric cards */
        [data-testid="stMetric"] {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.1), rgba(244, 114, 182, 0.1));
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 0.5rem !important;
            margin-bottom: 0.5rem !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        
        [data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.15), rgba(244, 114, 182, 0.15));
        }
        
        /* Headers */
        h2 {
            color: #f472b6 !important;
            font-weight: 600 !important;
            font-size: 1.3rem !important;
            margin-top: 1.5rem !important;
            margin-bottom: 0.8rem !important;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid rgba(244, 114, 182, 0.2);
        }
        
        /* Alert boxes */
        [data-testid="stAlert"] {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.1), rgba(244, 114, 182, 0.1));
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            color: #fce7f3;
            padding: 0.8rem;
            margin-bottom: 0.8rem;
        }
        
        /* Plotly charts container */
        .js-plotly-plot {
            max-width: 100vw !important;
            padding: 0.3rem !important;
            overflow-x: hidden !important;
            border-radius: 10px;
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.1), rgba(244, 114, 182, 0.1));
            border: 1px solid rgba(255,255,255,0.1);
            margin: 0.5rem 0;
        }
        
        /* Button styling */
        .stButton button {
            background: linear-gradient(90deg, #9333ea, #f472b6) !important;
            color: white !important;
            border: none !important;
            padding: 0.4rem 1.5rem !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton button:hover {
            opacity: 0.9;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        
        /* Timestamp styling */
        .timestamp {
            color: #f472b6;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
        }

        /* Make metrics text more visible */
        [data-testid="stMetricLabel"] {
            color: #f472b6 !important;
            font-size: 0.9rem !important;
        }

        [data-testid="stMetricValue"] {
            color: #fce7f3 !important;
        }

        [data-testid="stMetricDelta"] {
            color: #d8b4fe !important;
        }
        
        /* Power breakdown section */
        .power-breakdown {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.15), rgba(244, 114, 182, 0.15));
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            border: 1px solid rgba(255,255,255,0.1);
        }
        
        .power-item {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid rgba(244, 114, 182, 0.2);
            color: #fce7f3;
        }
        
        .power-total {
            font-weight: bold;
            padding-top: 0.5rem;
            border-top: 2px solid rgba(244, 114, 182, 0.4);
            color: #f472b6;
        }
        
        /* Top alerts section */
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

# Create sample data
hourly_data = pd.DataFrame({
    'hour': pd.date_range(start='2024-01-09 00:00', periods=24, freq='H').strftime('%H:%M'),
    'vehicles': [150, 120, 100, 80, 90, 120, 350, 580, 450, 280, 220, 250, 
                300, 280, 320, 380, 420, 380, 250, 180, 150, 120, 100, 80],
    'co2': [650, 630, 600, 580, 600, 650, 750, 800, 720, 680, 650, 670,
            700, 680, 720, 750, 780, 750, 700, 650, 620, 600, 580, 570],
    'no2': [150, 145, 140, 135, 140, 150, 180, 200, 170, 160, 150, 155,
            165, 160, 170, 180, 190, 180, 160, 150, 145, 140, 135, 130],
    'jetfan_speed': [65, 60, 55, 50, 55, 65, 85, 95, 85, 75, 70, 75,
                     80, 75, 80, 85, 90, 85, 75, 70, 65, 60, 55, 50]
})

# Critical Alerts Section at top
st.markdown('<div class="top-alerts">', unsafe_allow_html=True)
critical_alerts = [
    "🚨 HIGH PRIORITY: CO2 levels approaching threshold in Section B",
    "⚠️ URGENT: Suspected Traffic Jam inside Tunnel"
]
for alert in critical_alerts:
    st.error(alert)
st.markdown('</div>', unsafe_allow_html=True)

# Sample data with updated values
tunnel_data = {
    "totalVehicles": 1254,
    "maxTemperature": "35°C",
    "co2Level": "850 ppm",
    "no2Level": "180 µg/m³",
    "totalPower": "1850 kW",
    "predictedExhaustPower": "65%",
    "predictedCongestion": "75%",
    "predictedAirQuality": "Moderate",
    "predictedMaintenance": "Others"
}

# Current Stats Section with air quality metrics (removed Exhaust Power)
st.header('Current Statistics')
cols = st.columns(5)
metrics = [
    ("Total Vehicles", tunnel_data["totalVehicles"], "↑ 12%"),
    ("Temperature", tunnel_data["maxTemperature"], "↑ 5%"),
    ("CO₂ Level", tunnel_data["co2Level"], "↑ 15%"),
    ("NO₂ Level", tunnel_data["no2Level"], "↑ 8%"),
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
    ("Jet Fan Speed", tunnel_data["predictedExhaustPower"], "89% confidence"),
    ("Expected Traffic", tunnel_data["predictedCongestion"], "85% confidence"),
    ("Air Quality Forecast", tunnel_data["predictedAirQuality"], "92% confidence"),
    ("--", tunnel_data["predictedMaintenance"], "--")
]
for col, (label, value, conf) in zip(cols, predictions):
    with col:
        st.metric(label, value, conf)

# Traffic Flow Analysis
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

# Jet Fan Speed vs Parameters graph
st.header('Jet Fan Speed vs Parameters')
fig_params = go.Figure()

# Add traces for each parameter
fig_params.add_trace(go.Scatter(
    x=hourly_data['hour'],
    y=hourly_data['jetfan_speed'],
    name='Jet Fan Speed (%)',
    line=dict(color='#9333ea', width=2)
))

fig_params.add_trace(go.Scatter(
    x=hourly_data['hour'],
    y=hourly_data['vehicles'],
    name='Vehicles',
    line=dict(color='#f472b6', width=2)
))

fig_params.add_trace(go.Scatter(
    x=hourly_data['hour'],
    y=hourly_data['co2'].divide(10),  # Scaled for better visualization
    name='CO₂ (ppm/10)',
    line=dict(color='#60a5fa', width=2)
))

fig_params.add_trace(go.Scatter(
    x=hourly_data['hour'],
    y=hourly_data['no2'],
    name='NO₂ (µg/m³)',
    line=dict(color='#4ade80', width=2)
))

fig_params.update_layout(
    height=300,
    margin=dict(l=10, r=10, t=20, b=10),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#f472b6',
    showlegend=True,
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
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
st.plotly_chart(fig_params, use_container_width=True, config={'displayModeBar': False})

# Secondary Alerts Section
st.header('Other Alerts')
alerts = [
    "⚠️ Forecast: Air quality may deteriorate in Section C - Consider increasing ventilation",
    "🔧 Maintenance Alert: Low illumination "
]
for alert in alerts:
    st.warning(alert)

# Refresh button
col1, col2, col3 = st.columns([4,1,4])
with col2:
    st.button('🔄 Refresh Data')
