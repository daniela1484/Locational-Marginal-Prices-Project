import pandas as pd
import sqlite3
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load historical LMP data
connect1 = sqlite3.connect("data/historical_prices.db")
df = pd.read_sql_query("SELECT timestamp, lmp_value FROM lmp_data ORDER BY timestamp", connect1)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

# Train the ARIMA model
model = ARIMA(df["lmp_value"], order=(2,1,2))
model_fit = model.fit()

# Forecast the next 24 hours
forecast_hrs = 24
forecast = model_fit.forecast(steps=forecast_hrs)

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["lmp_value"], label="Historical LMP")
plt.plot(pd.date_range(start=df.index[-1], periods=forecast_hrs, freq="h"), forecast, label="Forecasted LMP", linestyle="dashed")
plt.legend()
plt.xlabel("Time")
plt.ylabel("LMP ($/MWh)")
plt.title("LMP Forecast (ARIMA Model)")
plt.show()