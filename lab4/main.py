import tkinter as tk
from tkinter import ttk
from db import get_all_cars, get_all_customers, get_all_sales, add_car, add_customer, make_sale, delete_car, delete_customer, delete_sale

def refresh_cars_table():
    for row in car_tree.get_children():
        car_tree.delete(row)
    for car in get_all_cars():
        car_tree.insert("", "end", values=(car[0], car[1], car[2], car[3], car[4]))
        
def refresh_customers_table():
    for row in customer_tree.get_children():
        customer_tree.delete(row)
    for customer in get_all_customers():
        customer_tree.insert("", "end", values=(customer[0], customer[1], customer[2], customer[3]))
 
def refresh_sales_table():
    for row in sales_tree.get_children():
        sales_tree.delete(row)
    for sale in get_all_sales():
        sales_tree.insert("", "end", values=(sale[0], sale[1], sale[2], sale[3]))
 
root = tk.Tk()
root.title("Car Shop Management System")

# Frame for all tables
table_frame = ttk.LabelFrame(root, text="Tables")
table_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

# Cars table
car_frame = ttk.LabelFrame(table_frame, text="Cars")
car_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
car_tree = ttk.Treeview(car_frame, columns=("ID", "Make", "Model", "Year", "Price"), show="headings")
car_tree.heading("ID", text="ID")
car_tree.heading("Make", text="Make")
car_tree.heading("Model", text="Model")
car_tree.heading("Year", text="Year")
car_tree.heading("Price", text="Price")
car_tree.grid(row=0, column=0, sticky="nsew")

refresh_cars_table()

# Insert car frame
insert_car_frame = ttk.LabelFrame(car_frame, text="Insert Car")
insert_car_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
make_label = ttk.Label(insert_car_frame, text="Make:")
make_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
make_entry = ttk.Entry(insert_car_frame)
make_entry.grid(row=0, column=1, padx=5, pady=5)

model_label = ttk.Label(insert_car_frame, text="Model:")
model_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
model_entry = ttk.Entry(insert_car_frame)
model_entry.grid(row=1, column=1, padx=5, pady=5)

year_label = ttk.Label(insert_car_frame, text="Year:")
year_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
year_entry = ttk.Entry(insert_car_frame)
year_entry.grid(row=2, column=1, padx=5, pady=5)

price_label = ttk.Label(insert_car_frame, text="Price:")
price_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
price_entry = ttk.Entry(insert_car_frame)
price_entry.grid(row=3, column=1, padx=5, pady=5)

def insert_car_button_clicked():
    add_car(make_entry.get(), model_entry.get(), int(year_entry.get()), float(price_entry.get()))

refresh_cars_table()

insert_car_button = ttk.Button(insert_car_frame, text="Insert Car", command=insert_car_button_clicked)
insert_car_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


delete_car_frame = ttk.LabelFrame(car_frame, text="Delete Car")
delete_car_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
delete_car_id_label = ttk.Label(delete_car_frame, text="Enter Car ID to delete:")
delete_car_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
delete_car_id_entry = ttk.Entry(delete_car_frame)
delete_car_id_entry.grid(row=0, column=1, padx=5, pady=5)

def delete_car_button_clicked():
    car_id = delete_car_id_entry.get()
    if car_id:
        delete_car(int(car_id))
        
refresh_cars_table()

delete_car_button = ttk.Button(delete_car_frame, text="Delete Car", command=delete_car_button_clicked)
delete_car_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


customer_frame = ttk.LabelFrame(table_frame, text="Customers")
customer_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
customer_tree = ttk.Treeview(customer_frame, columns=("ID", "First Name", "Last Name", "Email"), show="headings")
customer_tree.heading("ID", text="ID")
customer_tree.heading("First Name", text="First Name")
customer_tree.heading("Last Name", text="Last Name")
customer_tree.heading("Email", text="Email")
customer_tree.grid(row=0, column=0, sticky="nsew")

refresh_customers_table()

insert_customer_frame = ttk.LabelFrame(customer_frame, text="Insert Customer")
insert_customer_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
first_name_label = ttk.Label(insert_customer_frame, text="First Name:")
first_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
first_name_entry = ttk.Entry(insert_customer_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

last_name_label = ttk.Label(insert_customer_frame, text="Last Name:")
last_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
last_name_entry = ttk.Entry(insert_customer_frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = ttk.Label(insert_customer_frame, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
email_entry = ttk.Entry(insert_customer_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

def insert_customer_button_clicked():
    add_customer(first_name_entry.get(), last_name_entry.get(), email_entry.get())
    
refresh_customers_table()

insert_customer_button = ttk.Button(insert_customer_frame, text="Insert Customer", command=insert_customer_button_clicked)
insert_customer_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


delete_customer_frame = ttk.LabelFrame(customer_frame, text="Delete Customer")
delete_customer_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
delete_customer_id_label = ttk.Label(delete_customer_frame, text="Enter Customer ID to delete:")
delete_customer_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
delete_customer_id_entry = ttk.Entry(delete_customer_frame)
delete_customer_id_entry.grid(row=0, column=1, padx=5, pady=5)

def delete_customer_button_clicked():
    customer_id = delete_customer_id_entry.get()
    if customer_id:
        delete_customer(int(customer_id))

refresh_customers_table()

delete_customer_button = ttk.Button(delete_customer_frame, text="Delete Customer", command=delete_customer_button_clicked)
delete_customer_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

sales_frame = ttk.LabelFrame(table_frame, text="Sales")
sales_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
sales_tree = ttk.Treeview(sales_frame, columns=("ID", "Car ID", "Customer ID", "Sale Date"), show="headings")
sales_tree.heading("ID", text="ID")
sales_tree.heading("Car ID", text="Car ID")
sales_tree.heading("Customer ID", text="Customer ID")
sales_tree.heading("Sale Date", text="Sale Date")
sales_tree.grid(row=0, column=0, sticky="nsew")

refresh_sales_table()

insert_sale_frame = ttk.LabelFrame(sales_frame, text="Insert Sale")
insert_sale_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
car_id_label = ttk.Label(insert_sale_frame, text="Car ID:")
car_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
car_id_entry = ttk.Entry(insert_sale_frame)
car_id_entry.grid(row=0, column=1, padx=5, pady=5)

customer_id_label = ttk.Label(insert_sale_frame, text="Customer ID:")
customer_id_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
customer_id_entry = ttk.Entry(insert_sale_frame)
customer_id_entry.grid(row=1, column=1, padx=5, pady=5)

def insert_sale_button_clicked():
    make_sale(int(car_id_entry.get()), int(customer_id_entry.get()))
    
refresh_sales_table()

insert_sale_button = ttk.Button(insert_sale_frame, text="Insert Sale", command=insert_sale_button_clicked)
insert_sale_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

delete_sale_frame = ttk.LabelFrame(sales_frame, text="Delete Sale")
delete_sale_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
delete_sale_id_label = ttk.Label(delete_sale_frame, text="Enter Sale ID to delete:")
delete_sale_id_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
delete_sale_id_entry = ttk.Entry(delete_sale_frame)
delete_sale_id_entry.grid(row=0, column=1, padx=5, pady=5)

def delete_sale_button_clicked():
    sale_id = delete_sale_id_entry.get()
    if sale_id:
        delete_sale(int(sale_id))
        
refresh_sales_table()

delete_sale_button = ttk.Button(delete_sale_frame, text="Delete Sale", command=delete_sale_button_clicked)
delete_sale_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.mainloop()
