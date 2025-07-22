import pandas as pd
import folium

def create_map(csv_path="data/e_waste_centers.csv", save_path="map/e_waste_map.html"):
    df = pd.read_csv(csv_path)
    m = folium.Map(location=[21.1458, 79.0882], zoom_start=5)

    for _, row in df.iterrows():
        folium.Marker(
            location=[21.1458, 79.0882],  # static for now
           popup=f"{row['Name']}<br>{row['Address']}",

            tooltip=row['Name']
        ).add_to(m)

    m.save(save_path)
    print(f"Map saved to {save_path}")

if __name__ == "__main__":
    create_map()
