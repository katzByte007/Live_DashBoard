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
    'power': [1500, 1450, 1400, 1350, 1400, 1500, 2000, 2500, 2200, 1800, 1700, 1750,
              1850, 1800, 1900, 2000, 2100, 2000, 1800, 1600, 1500, 1400, 1350, 1300]
})

# Prediction data for future hours
prediction_data = pd.DataFrame({
    'time': pd.date_range(start='2024-01-09 00:00', periods=6, freq='H').strftime('%H:%M'),
    'predicted': [2100, 2300, 2600, 2400, 2200, 2000],
    'confidence': [0.85, 0.82, 0.78, 0.75, 0.72, 0.70]
})

# Critical Alerts Section at top
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
