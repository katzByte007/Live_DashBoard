import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Set page config - set to wide but will be overridden by CSS for mobile
st.set_page_config(
    page_title="Tunnel Operations Hub",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Updated CSS with mobile-friendly adjustments
st.markdown("""
    <style>
        /* Mobile-first responsive layout */
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #2d1b3d 50%, #1a1a2e 100%);
            max-width: 100vw;
            padding: 0.5rem !important;
        }
        
        /* Smaller, mobile-friendly title */
        .gradient-text {
            background: linear-gradient(120deg, #ff6b6b, #f472b6, #9333ea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 28px !important;
            font-weight: 700 !important;
            margin-bottom: 0px !important;
            text-align: center;
        }
        
        /* Compact metric cards for mobile */
        [data-testid="stMetric"] {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.1), rgba(244, 114, 182, 0.1));
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 0.5rem !important;
            margin: 0.3rem 0 !important;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        
        /* Smaller font size for metric labels on mobile */
        [data-testid="stMetricLabel"] {
            color: #f472b6 !important;
            font-size: 0.8rem !important;
        }
        
        [data-testid="stMetricValue"] {
            color: #fce7f3 !important;
            font-size: 1.1rem !important;
        }
        
        [data-testid="stMetricDelta"] {
            color: #d8b4fe !important;
            font-size: 0.8rem !important;
        }
        
        /* Mobile-friendly headers */
        h2 {
            color: #f472b6 !important;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            margin-top: 1rem !important;
            margin-bottom: 0.5rem !important;
            padding-bottom: 0.3rem;
            border-bottom: 1px solid rgba(244, 114, 182, 0.2);
        }
        
        /* Compact alert boxes for mobile */
        [data-testid="stAlert"] {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.1), rgba(244, 114, 182, 0.1));
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            color: #fce7f3;
            padding: 0.5rem;
            margin-bottom: 0.5rem;
            font-size: 0.9rem;
        }
        
        /* Timestamp for mobile */
        .timestamp {
            color: #f472b6;
            font-size: 0.8rem;
            margin-bottom: 1rem;
            text-align: center;
        }
        
        /* Mobile-friendly button */
        .stButton button {
            background: linear-gradient(90deg, #9333ea, #f472b6) !important;
            color: white !important;
            border: none !important;
            padding: 0.4rem 1rem !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            width: 100% !important;
            margin: 0.5rem 0 !important;
        }
        
        /* Make columns stack on mobile */
        [data-testid="column"] {
            width: 100% !important;
            margin-bottom: 0.5rem !important;
        }
        
        /* Adjust chart padding for mobile */
        .js-plotly-plot {
            padding: 0.3rem !important;
        }
        
        /* Hide plotly modebar on mobile */
        .modebar {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title and timestamp
st.markdown('<p class="gradient-text">Tunnel Operations Hub</p>', unsafe_allow_html=True)
st.markdown(f'<p class="timestamp">Live Updates • {datetime.now().strftime("%H:%M:%S")}</p>', unsafe_allow_html=True)

# Sample data
tunnel_data = {
    "totalVehicles": 1254,
    "jetFansPower": "2500 kW",
    "maxTemperature": "35°C",
    "totalPowerUsage": "1850 kW",
    "dgPower": "500 kW",
    "lightingPower": "350 kW",
    "predictedExhaustPower": "2800 kW",
    "predictedCongestion": "75%",
    "predictedAirQuality": "Moderate",
    "predictedMaintenance": "4 days"
}

# Current Stats Section - Now in 2 columns for better mobile view
st.header('Current Statistics')
col1, col2 = st.columns(2)

# First column metrics
with col1:
    st.metric("Total Vehicles", tunnel_data["totalVehicles"], "↑ 12%")
    st.metric("Jet Fans Power", tunnel_data["jetFansPower"], "→ 0%")
    st.metric("DG Power", tunnel_data["dgPower"], "↑ 3%")

# Second column metrics
with col2:
    st.metric("Total Power Usage", tunnel_data["totalPowerUsage"], "↓ 8%")
    st.metric("Lighting Power", tunnel_data["lightingPower"], "↓ 2%")
    st.metric("Temperature", tunnel_data["maxTemperature"], "↑ 5%")

# Predictive Insights - Also in 2 columns
st.header('Predictive Insights')
col1, col2 = st.columns(2)

# Split predictions between columns
with col1:
    st.metric("Required Power", tunnel_data["predictedExhaustPower"], "89% conf.")
    st.metric("Expected Congestion", tunnel_data["predictedCongestion"], "85% conf.")

with col2:
    st.metric("Air Quality", tunnel_data["predictedAirQuality"], "92% conf.")
    st.metric("Next Maintenance", tunnel_data["predictedMaintenance"], "87% conf.")

# Traffic Flow Analysis - Simplified for mobile
st.header('Traffic Flow')
hourly_data = pd.DataFrame({
    'hour': ['06:00', '07:00', '08:00', '09:00', '10:00'],
    'vehicles': [120, 350, 580, 450, 280]
})

fig_traffic = px.area(hourly_data, x='hour', y='vehicles')
fig_traffic.update_layout(
    height=200,  # Reduced height for mobile
    margin=dict(l=10, r=10, t=10, b=10),  # Minimal margins
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font_color='#f472b6',
    showlegend=False,
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)'
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(244, 114, 182, 0.1)',
        linecolor='rgba(244, 114, 182, 0.2)'
    )
)
fig_traffic.update_traces(
    fill='tozeroy',
    line=dict(color='#f472b6'),
    fillcolor='rgba(244, 114, 182, 0.2)'
)
st.plotly_chart(fig_traffic, use_container_width=True, config={'displayModeBar': False})

# Alerts Section - More compact for mobile
st.header('Alerts')
alerts = [
    "🚨 Jet Fans power +25% in 2h",
    "⚠️ Air quality alert in Section C",
    "🔧 Fan maintenance needed in 4d"
]
for alert in alerts:
    st.warning(alert)

# Full-width refresh button
st.button('🔄 Refresh Data')