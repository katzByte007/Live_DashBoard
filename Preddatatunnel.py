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

# Updated CSS with better text visibility
st.markdown("""
    <style>
        /* Previous styles with improved text visibility */
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #2d1b3d 50%, #1a1a2e 100%);
            max-width: 100vw;
            padding: 0.5rem !important;
        }
        
        /* Better text visibility */
        .stMarkdown, .stText, p, span {
            color: #ffffff !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #f472b6 !important;
            font-weight: 600 !important;
        }
        
        .gradient-text {
            background: linear-gradient(120deg, #ff6b6b, #f472b6, #9333ea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 28px !important;
            font-weight: 700 !important;
            margin-bottom: 0px !important;
            text-align: center;
        }
        
        /* Enhanced metric cards */
        [data-testid="stMetric"] {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.1), rgba(244, 114, 182, 0.1));
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 0.5rem !important;
            margin: 0.2rem 0 !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        
        /* Metric text colors */
        [data-testid="stMetricLabel"] {
            color: #f472b6 !important;
            font-weight: 600 !important;
        }
        
        [data-testid="stMetricValue"] {
            color: #ffffff !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
        }
        
        [data-testid="stMetricDelta"] {
            color: #d8b4fe !important;
        }
        
        /* High priority predictions */
        .high-priority {
            background: linear-gradient(145deg, rgba(239, 68, 68, 0.15), rgba(244, 114, 182, 0.15)) !important;
            border: 2px solid rgba(239, 68, 68, 0.3) !important;
        }
        
        /* Previous styles continue... */
        .timestamp {
            color: #f472b6;
            font-size: 0.8rem;
            text-align: center;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title and timestamp remain the same
st.markdown('<p class="gradient-text">Tunnel Operations Hub</p>', unsafe_allow_html=True)
st.markdown(f'<p class="timestamp">Live Updates • {datetime.now().strftime("%H:%M:%S")}</p>', unsafe_allow_html=True)

# Enhanced sample data with more predictions
tunnel_data = {
    # Current metrics
    "totalVehicles": 1254,
    "jetFansPower": "2500 kW",
    "dgPower": "500 kW",
    "lightingPower": "350 kW",
    "totalPowerUsage": "3350 kW",
    "maxTemperature": "35°C",
    "co2Level": "850 ppm",
    "no2Level": "0.35 ppm",
    
    # Enhanced predictions
    "requiredJetFansPower": "3000 kW",
    "predictedTraffic": "1500",
    "predictedCO2": "920 ppm",
    "predictedNO2": "0.42 ppm",
    "predictedPowerSaving": "15%",
    "maintenanceUrgency": "High",
    "nextPeakHour": "17:00",
    "ventilationEfficiency": "75%"
}

# Alerts Section with more comprehensive alerts
critical_alerts = [
    "🚨 Required Jet Fan Power: Increase to 3000 kW needed based on CO2 (850 ppm)",
    "⚠️ Predicted CO2 spike in 30 mins - Increase ventilation",
    "🔄 Traffic congestion expected at 17:00 - Prepare systems"
]

for alert in critical_alerts:
    st.warning(alert)

# Current Statistics sections remain the same...
[Previous current statistics code remains unchanged]

# Enhanced Predictive Insights
st.header('Predictive Insights')

# High Priority Predictions
st.subheader('Critical Predictions')
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="high-priority">', unsafe_allow_html=True)
    st.metric(
        "Required Jet Fan Power",
        tunnel_data["requiredJetFansPower"],
        "↑ 500 kW needed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="high-priority">', unsafe_allow_html=True)
    st.metric(
        "Next Peak Traffic",
        tunnel_data["nextPeakHour"],
        tunnel_data["predictedTraffic"] + " vehicles"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Air Quality Predictions
st.subheader('Air Quality Forecast')
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Predicted CO2",
        tunnel_data["predictedCO2"],
        "↑ 8% in 30min"
    )
with col2:
    st.metric(
        "Predicted NO2",
        tunnel_data["predictedNO2"],
        "↑ 20% in 30min"
    )

# System Efficiency Predictions
st.subheader('System Efficiency')
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Ventilation Efficiency",
        tunnel_data["ventilationEfficiency"],
        "↓ 5% - Check filters"
    )
with col2:
    st.metric(
        "Power Saving Potential",
        tunnel_data["predictedPowerSaving"],
        "Optimize fan speed"
    )

# Maintenance Predictions
st.subheader('Maintenance Insights')
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Maintenance Priority",
        tunnel_data["maintenanceUrgency"],
        "⚠️ Schedule within 24h"
    )
with col2:
    st.metric(
        "Fan System Health",
        "82%",
        "↓ 3% this week"
    )

# Traffic Flow Analysis remains the same...
[Previous traffic flow code remains unchanged]

# Refresh button
st.button('🔄 Refresh Data')
