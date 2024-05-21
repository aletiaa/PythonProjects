import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('car_shop.db')
cursor = conn.cursor()

# Define the schema for the car shop database
create_tables_query = '''
CREATE TABLE IF NOT EXISTS cars (
    CarID INTEGER PRIMARY KEY,
    Make TEXT NOT NULL,
    Model TEXT NOT NULL,
    Year INTEGER NOT NULL,
    Price REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS sales (
    SaleID INTEGER PRIMARY KEY,
    CarID INTEGER,
    CustomerID INTEGER,
    SaleDate TEXT,
    FOREIGN KEY (CarID) REFERENCES cars(CarID),
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);
'''

# Execute the schema creation query
cursor.executescript(create_tables_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

# Define functions for car shop operations
def add_car(make, model, year, price):
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cars (Make, Model, Year, Price) VALUES (?, ?, ?, ?)', (make, model, year, price))
    conn.commit()
    conn.close()

def add_customer(first_name, last_name, email):
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    
    # Check if the email already exists
    cursor.execute('SELECT * FROM customers WHERE Email = ?', (email,))
    existing_customer = cursor.fetchone()
    if existing_customer:
        print("Error: Customer with this email already exists.")
        return
    
    # Insert the new customer
    cursor.execute('INSERT INTO customers (FirstName, LastName, Email) VALUES (?, ?, ?)', (first_name, last_name, email))
    conn.commit()
    conn.close()

def make_sale(car_id, customer_id):
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    sale_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO sales (CarID, CustomerID, SaleDate) VALUES (?, ?, ?)', (car_id, customer_id, sale_date))
    conn.commit()
    conn.close()

def get_all_cars():
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    conn.close()
    return cars

def get_all_customers():
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()
    return customers

def get_all_sales():
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    conn.close()
    return sales

def get_customer_by_email(email):
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers WHERE Email = ?', (email,))
    customer = cursor.fetchone()
    conn.close()
    return customer

def delete_car(car_id):
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM cars WHERE CarID = ?', (car_id,))
    conn.commit()
    conn.close()

def delete_customer(customer_id):
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM customers WHERE CustomerID = ?', (customer_id,))
    conn.commit()
    conn.close()

def delete_sale(sale_id):
    conn = sqlite3.connect('car_shop.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM sales WHERE SaleID = ?', (sale_id,))
    conn.commit()
    conn.close()

# Example usage
add_car('Toyota', 'Corolla', 2022, 25000)
add_customer('John', 'Doe', 'jjohndoe@example.com')
add_customer('alina', 'freeman', 'asa@example.com' )
make_sale(1, 1)

print(get_all_cars())
print(get_all_customers())
print(get_all_sales())
print(get_customer_by_email('john@example.com'))
