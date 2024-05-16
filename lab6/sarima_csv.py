import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
from tabulate import tabulate  # Import the tabulate function

# Step 1: Load data from CSV
data = pd.read_csv('audi.csv', parse_dates=['Date'])

# Step 2: Set 'Date' as index
data.set_index('Date', inplace=True)

# Step 3: Ensure 'Price' column is numeric
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Handle missing values, if any
data.dropna(inplace=True)

# Step 4: Train the SARIMA model
sarima_model = SARIMAX(data['Price'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
sarima_model_fit = sarima_model.fit(disp=False)

# Step 5: Train the ARIMA model for comparison
arima_model = ARIMA(data['Price'], order=(1, 1, 1))
arima_model_fit = arima_model.fit()

# Step 6: Make forecasts for the next 3 months using SARIMA
forecast_steps = 3  # Forecasting for 3 months
sarima_forecast = sarima_model_fit.forecast(steps=forecast_steps)

# Step 7: Make forecasts for the next 3 months using ARIMA
arima_forecast = arima_model_fit.forecast(steps=forecast_steps)

# Step 8: Define actual values
actual_values = [27359.415376482368, 27417.068153893506, 27627.879906094528]

# Step 9: Print the forecasts and differences
forecast_dates = pd.date_range(start=data.index[-1] + pd.DateOffset(months=1), periods=forecast_steps, freq='MS')

# Prepare data for tabulate
table_data = []
for date, sarima_price, arima_price, actual_price in zip(forecast_dates, sarima_forecast, arima_forecast, actual_values):
    sarima_diff = sarima_price - actual_price
    arima_diff = arima_price - actual_price
    table_data.append([date.strftime('%Y-%m-%d'), sarima_price, arima_price, actual_price, sarima_diff, arima_diff])

# Print table
headers = ["Date", "SARIMA Forecast", "ARIMA Forecast", "Actual", "SARIMA Diff.", "ARIMA Diff."]
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Plot the forecasted values
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['Price'], label='Historical Price')
plt.plot(forecast_dates, sarima_forecast, label='SARIMA Forecast', color='red', marker='o')
plt.plot(forecast_dates, arima_forecast, label='ARIMA Forecast', color='blue', marker='o')
plt.title('Forecasted Prices for the Last 3 Months (SARIMA vs ARIMA)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
