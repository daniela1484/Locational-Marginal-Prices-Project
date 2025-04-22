import requests
import pandas as pd
from datetime import datetime

### This script alerts when load exceeds key thresholds or when generation data shows rapid changes. 
### EIA API is used to pull hourly demand data for regions such as Texas.

EIA_API_key = "GcdSVebgcbQ442EUDFnvdJNj39wQ3UdpDk6PkhUs" # different for each user
region = "tx" # ERCOT
series_id = f"ELEC.LOAD.RESID.H.TX.A" # Residential hourly load for Tx

# fcn to get EIA data
def get_eia_hrly_load(series_id, api_key):
    url = f"https://api.eia.gov/series/?api_key={api_key}&series_id={series_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data.")
    data = response.json()["series"][0]["data"]

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["timestamp", "load_MW"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], format= "%Y%m%dT%HZ")
    df = df.sort_values("timestamp").reset_index(drop=True)
    return df

try: 
    load_df = get_eia_hrly_load(series_id, EIA_API_key)
    recent_load = load_df.tail(6) # last 6 hrs
    print("Hourly Load Data (Residential, TX):\n")
    print(recent_load)

    # ex. simple alert
    if recent_load["load_MW"].max() > 15000: # example threshold
        print("Alert: High residential load-investigate further for congestion risk.")
except Exception as e:
    print("Error:", e)
