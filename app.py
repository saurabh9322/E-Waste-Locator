
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from geopy.geocoders import Nominatim

# Load data
df = pd.read_csv("data/e_waste_centers.csv")

# Sidebar: City filter
city_list = ['All'] + sorted(df['City'].unique().tolist())
selected_city = st.sidebar.selectbox("🔍 Filter by City", city_list)

# Sidebar: Search by name
search_term = st.sidebar.text_input("🔍 Search by Center Name")

# Filter based on selection
filtered_df = df.copy()
if selected_city != 'All':
    filtered_df = filtered_df[filtered_df['City'] == selected_city]
if search_term:
    filtered_df = filtered_df[filtered_df['Name'].str.contains(search_term, case=False)]

# Title and subtitle
st.markdown("<h1 style='text-align: center;'>📍 E-Waste Recycling Center Locator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Search, filter and explore recycling facilities across India</p>", unsafe_allow_html=True)
st.markdown("---")

# Generate Map
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add user location pin using Nominatim (optional)
try:
    geolocator = Nominatim(user_agent="geoapi")
    user_location = geolocator.geocode("Nagpur, India")
    if user_location:
        folium.Marker(
            location=[user_location.latitude, user_location.longitude],
            popup="📍 You are here (Nagpur)",
            icon=folium.Icon(color="blue")
        ).add_to(m)
except:
    pass

# Add center markers
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['Name']}</b><br>{row['Address']}<br>{row['City']}",
        tooltip=row['Name'],
        icon=folium.Icon(color="green", icon="recycle", prefix="fa")
    ).add_to(m)

# Show map in Streamlit
st_data = st_folium(m, width=1000, height=600)
