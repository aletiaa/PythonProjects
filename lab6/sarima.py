import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

# Given data
years = [1, 2, 3, 4, 5, 6, 7, 8]  # Years from 2016 to 2023
prices = [32889, 29690, 25584, 23496, 19213, 16344, 13851, 12847]  # Prices for each year in GBP (£)

# Convert years to datetime index starting from 2016-01-01
start_year = 2016
price_data = pd.Series(prices, index=pd.date_range(start=f'{start_year}-01-01', periods=len(years), freq='Y'))

# Function to decompose time series into trend, seasonal, and residual components
def decompose_time_series(data):
    decomposition = seasonal_decompose(data, model='additive')
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    plt.figure(figsize=(12, 8))
    plt.subplot(411)
    plt.plot(data, label='Оригінал')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Тренд')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal, label='Сезонність')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Залишки')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()
    


decompose_time_series(price_data)
# Прогнозування SARIMA
def sarima_forecast(data, forecast_steps):
    model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))  # Встановлюємо сезонність на 12 місяців
    model_fit = model.fit(disp=False)
    forecast = model_fit.forecast(steps=forecast_steps)
    return forecast

forecast_steps = 4  # Прогнозування на 4 роки
forecast = sarima_forecast(price_data, forecast_steps)
forecast_dates = pd.date_range(start='2024-01-01', end='2027-01-01', freq='Y')

print(len(price_data))
print(len(forecast_dates))
print(len(forecast))


# Виведемо результати прогнозу щорічно
for date, price in zip(forecast_dates, forecast):
    print(f'Прогнозована ціна на автомобіль SARIMA Audi у {date.year}: £{price:.2f}')

# Виведемо результати прогнозу на графіку
plt.figure(figsize=(10, 6))
plt.plot(price_data, label='Фактична Ціна')
plt.plot(forecast_dates, forecast, label='Прогноз SARIMA')
plt.title('Прогнозовані Ціни на Автомобілі Audi у 2024-2027 роках (SARIMA)')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.grid(True)
plt.show()
