import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_justdial(city="Nagpur"):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    base_url = f"https://www.justdial.com/{city}/E-Waste-Recycling-Centres"
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for item in soup.find_all("li", class_="cntanr"):
        try:
            name = item.find("span", class_="lng_cont_name").text.strip()
            phone = item.find("p", class_="contact-info").text.strip()
            address = item.find("span", class_="cont_sw_addr").text.strip()
            data.append([name, phone, address, city])
        except:
            continue

    df = pd.DataFrame(data, columns=["Name", "Phone", "Address", "City"])
    df.to_csv("data/e_waste_centers.csv", index=False)
    print("Scraping done and saved to data/e_waste_centers.csv")

if __name__ == "__main__":
    scrape_justdial()
