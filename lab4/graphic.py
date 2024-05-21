import matplotlib.pyplot as plt
from db import get_all_cars

def plot_car_prices():
    cars = get_all_cars()
    car_ids = [car[0] for car in cars]  # CarID is the first column
    car_prices = [car[4] for car in cars]  # Price is the fifth column

    plt.bar(car_ids, car_prices)
    plt.xlabel('Car ID')
    plt.ylabel('Price')
    plt.title('Car Prices')
    plt.show()

plot_car_prices()
