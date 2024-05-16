import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima.model import ARIMA

# Згенеруємо фіктивні дані про ціни на автомобілі марки Audi
np.random.seed(42)
start_date = '2010-01-01'
end_date = '2023-12-31'
date_range = pd.date_range(start=start_date, end=end_date, freq='M')
price_data = pd.Series(np.random.uniform(30000, 100000, size=len(date_range)), index=date_range)

# Аналіз тренду та сезонності
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

# Статистичні тести
def test_stationarity(data):
    result = adfuller(data)
    print('ADF Статистика:', result[0])
    print('p-значення:', result[1])
    print('Критичні значення:')
    for key, value in result[4].items():
        print('\t{}: {}'.format(key, value))

test_stationarity(price_data)

# Прогнозування SARIMA
def sarima_forecast(data, forecast_steps):
    model = SARIMAX(data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    model_fit = model.fit(disp=False)
    forecast = model_fit.forecast(steps=forecast_steps)
    return forecast

forecast_steps = 12  # Прогнозування на 12 місяців, тобто на весь 2024 рік
forecast_sarima = sarima_forecast(price_data, forecast_steps)
forecast_dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')

# Виведемо результати прогнозу щомісячно
for date, price in zip(forecast_dates, forecast_sarima):
    print(f'Прогнозована ціна на автомобіль SARIMA Audi у {date.strftime("%B %Y")}: {price:.2f}')
    

# Прогнозування ARIMA
def arima_forecast(data, forecast_steps):
    model = ARIMA(data, order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=forecast_steps)
    return forecast

forecast_steps = 12  # Прогнозування на 12 місяців, тобто на весь 2024 рік
forecast_arima = arima_forecast(price_data, forecast_steps)
forecast_dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')

# Виведемо результати прогнозу щомісячно
for date, price in zip(forecast_dates, forecast_arima):
    print(f'Прогнозована ціна на автомобіль ARIMA Audi у {date.strftime("%B %Y")}: {price:.2f}')

# Виведення результатів прогнозу SARIMA на графіку
plt.figure(figsize=(10, 6))
plt.plot(price_data, label='Фактична Ціна')
plt.plot(forecast_dates, forecast_sarima, label='Прогноз SARIMA')
plt.title('Прогнозовані Ціни на Автомобілі Audi у 2024 році (SARIMA)')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.grid(True)
plt.show()

# Виведення результатів прогнозу ARIMA на графіку
plt.figure(figsize=(10, 6))
plt.plot(price_data, label='Фактична Ціна')
plt.plot(forecast_dates, forecast_arima, label='Прогноз ARIMA', color='orange')
plt.title('Прогнозовані Ціни на Автомобілі Audi у 2024 році (ARIMA)')
plt.xlabel('Дата')
plt.ylabel('Ціна')
plt.legend()
plt.grid(True)
plt.show()

