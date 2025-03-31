import requests
import os
import sqlite3

### NOTE: Include YOUR OWN EIA URL ####
EIA_API_URL = "https://api.eia.gov/series/?api_key=YOUR_EIA_KEY&series_id=ELEC.PRICE"

# Ensure "data" directory exists
os.makedirs("data", exist_ok=True)

def obtain_real_time_lmp():
    headers = {"Authorication": "Bearer YOUR_API_KEY"}
    params = {"market": "REAL_TIME", "node": "PJM_Load"}
    response = requests.get(PJM_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return [(entry["datetime"], entry["bus"], entry["price"]) for entry in data]
    else:
        print("Error fetching data:", response.status_code)
        return []
    
def store_real_lmp():
    connect1 = sqlite3.connect("data/historical_prices.db")
    cursor = connect1.cursor()

    real_lmp_data = obtain_real_time_lmp()
    for record in real_lmp_data:
        cursor.execute("INSERT INTO lmp_data (timestamp, bus, lmp_values) VALUES (?, ?, ?)", record)

    connect1.commit()
    connect1.close()

store_real_lmp()
