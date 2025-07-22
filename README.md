# E-Waste Recycling Center Locator

🔍 A smart environmental mapping system to locate e-waste recycling centers across India.

## Features
- Scrapes E-waste centers from JustDial (city-wise)
- Saves data to CSV
- Shows all centers on a map of India using Folium
- Interactive UI using Streamlit

## How to Run

```bash
pip install -r requirements.txt
python scraper/justdial_scraper.py
python map/map_generator.py
streamlit run app.py
```

