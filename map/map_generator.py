import folium
from folium.plugins import MarkerCluster

def create_map():
    df = pd.read_csv("data/e_waste_centers.csv")
    df['Latitude'] = df['Latitude'].astype(str).str.strip().astype(float)
    df['Longitude'] = df['Longitude'].astype(str).str.strip().astype(float)

    m = folium.Map(location=[21.1458, 79.0882], zoom_start=6)

    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"{row['Name']}<br>{row['Address']}<br>{row['City']}",
            icon=folium.Icon(color="green", icon="recycle", prefix='fa')
        ).add_to(marker_cluster)

    m.save("map/e_waste_map.html")
