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

# CSS remains same as before, adding new styles for air quality metrics
st.markdown("""
    <style>
        /* Previous styles remain the same */
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #2d1b3d 50%, #1a1a2e 100%);
            max-width: 100vw;
            padding: 0.5rem !important;
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
        
        /* Air quality metrics styling */
        .air-quality-metrics [data-testid="stMetric"] {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.15), rgba(244, 114, 182, 0.15));
        }
        
        /* Previous styles continue... */
        .total-power {
            background: linear-gradient(145deg, rgba(147, 51, 234, 0.2), rgba(244, 114, 182, 0.2)) !important;
            border: 2px solid rgba(244, 114, 182, 0.3) !important;
            margin-top: 0.5rem !important;
        }
        
        .power-divider {
            border-top: 2px dashed rgba(244, 114, 182, 0.3);
            margin: 0.5rem 0;
            width: 100%;
        }
        
        /* Rest of the previous styles... */
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="gradient-text">Tunnel Operations Hub</p>', unsafe_allow_html=True)
st.markdown(f'<p class="timestamp">Live Updates • {datetime.now().strftime("%H:%M:%S")}</p>', unsafe_allow_html=True)

# Alerts Section at top
alerts = [
    "🚨 High CO2 Level: 850 ppm - Above threshold",
    "⚠️ NO2 Level increasing in Section C",
    "🔧 Fan maintenance needed in 4 days"
]
for alert in alerts:
    st.warning(alert)

# Sample data with added air quality metrics
jet_fans_power = 2500
dg_power = 500
lighting_power = 350
total_power = jet_fans_power + dg_power + lighting_power

tunnel_data = {
    "totalVehicles": 1254,
    "jetFansPower": f"{jet_fans_power} kW",
    "dgPower": f"{dg_power} kW",
    "lightingPower": f"{lighting_power} kW",
    "totalPowerUsage": f"{total_power} kW",
    "maxTemperature": "35°C",
    "co2Level": "850 ppm",
    "no2Level": "0.35 ppm",
    "predictedAirQuality": "Poor",
    "airQualityConfidence": "92%"
}

# Current Statistics with Air Quality
st.header('Current Statistics')

# Air Quality Metrics
st.subheader('Air Quality')
col1, col2 = st.columns(2)
with col1:
    st.metric("CO2 Level", tunnel_data["co2Level"], "↑ 15%")
with col2:
    st.metric("NO2 Level", tunnel_data["no2Level"], "↑ 8%")

# Power Usage Section
st.subheader('Power Usage')
# Individual power components
st.metric("Jet Fans Power", tunnel_data["jetFansPower"], "→ 0%")
st.metric("DG Power", tunnel_data["dgPower"], "↑ 3%")
st.metric("Lighting Power", tunnel_data["lightingPower"], "↓ 2%")
# Visual divider
st.markdown('<hr class="power-divider">', unsafe_allow_html=True)
# Total power
st.markdown('<div class="total-power">', unsafe_allow_html=True)
st.metric("Total Power Usage", tunnel_data["totalPowerUsage"], "↑ 5%")
st.markdown('</div>', unsafe_allow_html=True)

# Other Key Metrics
st.subheader('Other Metrics')
col1, col2 = st.columns(2)
with col1:
    st.metric("Total Vehicles", tunnel_data["totalVehicles"], "↑ 12%")
with col2:
    st.metric("Temperature", tunnel_data["maxTemperature"], "↑ 5%")

# Predictive Insights with enhanced air quality prediction
st.header('Predictive Insights')
col1, col2 = st.columns(2)

with col1:
    # Air quality prediction based on current CO2 and NO2 levels
    air_quality_color = "🔴" if tunnel_data["predictedAirQuality"] == "Poor" else "🟢"
    st.metric(
        "Predicted Air Quality",
        f"{air_quality_color} {tunnel_data['predictedAirQuality']}",
        f"Confidence: {tunnel_data['airQualityConfidence']}"
    )
with col2:
    st.metric("Next Maintenance", "4 days", "87% conf.")

# Traffic Flow Analysis
st.header('Traffic Flow')
hourly_data = pd.DataFrame({
    'hour': ['06:00', '07:00', '08:00', '09:00', '10:00'],
    'vehicles': [120, 350, 580, 450, 280]
})

fig_traffic = px.area(hourly_data, x='hour', y='vehicles')
fig_traffic.update_layout(
    height=180,
    margin=dict(l=5, r=5, t=5, b=5),
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

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.plotly_chart(fig_traffic, use_container_width=True, config={
    'displayModeBar': False,
    'responsive': True
})
st.markdown('</div>', unsafe_allow_html=True)

# Refresh button
st.button('🔄 Refresh Data')
