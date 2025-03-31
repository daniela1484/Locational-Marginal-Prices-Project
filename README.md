## Overview
The project implements a Locational Marginal Pricing (LMP) model to estimate electricity prices based on generator costs, demand, and transmission constraints. It also integrates real-world market data (EIA) and forecasting models (ARIMA, Machine Learning) to enhance price predictions.

## Project Structure
📦 lmp_project
 ┣ 📂 data/                # Contains historical and real-time LMP data
 ┃ ┗ 📜 historical_prices.db  # SQLite database storing LMP records
 ┣ 📂 scripts/             
 ┃ ┣ 📜 network_analysis.py    # Models power grid and transmission constraints
 ┃ ┣ 📜 lmp_model.py          # Runs LMP calculations using linear programming
 ┃ ┣ 📜 db_utils.py           # Stores and retrieves LMP data from SQLite
 ┃ ┣ 📜 forecast_lmp.py       # Forecasts future LMP using ARIMA
 ┃ ┣ 📜 api_integration.py    # Fetches real market data from PJM/EIA
 ┃ ┣ 📜 visualization.py      # Plots LMP trends and forecasts
 ┃ ┗ 📜 run_all.py            # Automates all steps in one script
 ┣ 📜 requirements.txt        # List of dependencies
 ┣ 📜 README.md               # Project documentation
 ┗ 📜 .gitignore              # Ignore unnecessary files


## Key Features
- **Locational Marginal Pricing (LMP) Model**: Calculates LMP based on supply, demand, and transmission constraints.
- **Multi-Time Interval Support**: Has the option to obtain **EIA** data for validation.
- **Forecasting (ARIMA, Machine Learning)**: Predicts future LMPs based on historical trends.
- **Database Storage (SQLite)**: Saves and retrieves LMP calculations.
- **Data Visualization**: Generates interactive plots for price trends.

## Installation and Setup
1. Clone the Repository
   ```
   git clone https://github.com/daniela1484/Locational_Marginal_Pricing_Project.git
   cd Locational_Marginal_Pricing_Project
   ```
   
2. Create a Virtual Environment
   ```
   python -m venv env
   source env/bin/activate # Mac/Linux
   env\Scripts\activate    # Windows
   ```
   
3. Set Up the Database
   ```
   python scripts/db_utils.py
   ```
   > This will create `historical_prices.db` and initialize the table.
   
5. Run the Full Model
   ```
   python scripts/run_all.py
   ```
   > This will:
   >  - Model the power grid and constraints,
   >  - Compute LMPs,
   >  - Obtain real market data,
   >  - Forecast future LMPs,
   >  - Store and visualize results.

## Example Output
```
LMPs: {'Total_Demand': 30.0, 'GenA_Capacity': -10.0, 'GenB_Capacity': 0.0}
GenA Output: 60.0 MW, GenB Output: 20.0 MW
```
> **Interpreting Results**
>  - LMP at Demand Bus = $30/MWh (Cost of supplying 1 extra MW)
>  - GenA is at max capacity (-10.0 shadow price), which means that it is not a limiting factor.
>  - GenB has an available capacity (0.0 shadow price), it is not a limiting factor.

## API Integration
Obtaining EIA Historical Price Data
```
EIA_API_URL = "https://api.eia.gov/series/?api_key=YOUR_EIA_KEY&series_id=ELEC.PRICE"
```

## Forecasting Future LMPs
For time series forecasting, **ARIMA** will be used:
```
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(df["lmp_value"], order=(2, 1, 2))
forecast = model.fit().forecast(steps=24)
```
> Outputs a 24-hour price forecast.

## Visualization
Use `matplotlib` to plot price trends:
```
import matplotlib.pyplot as plt
plt.plot(df.index, df["lmp_value"], label="Historical LMP")
plt.plot(forecast_dates, forecast, label="Forecasted LMP", linestyle="dashed")
plt.legend()
plt.show()
```
