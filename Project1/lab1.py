import pandas as pd

# Creating a list of products with additional characteristics
data = [
    {'Name': 'Apples', 'Price': 12.5, 'Product Type': 'Fruits', 'Quantity': 10, 'Expiration Date': '2024-04-01'},
    {'Name': 'Bananas', 'Price': 48.70, 'Product Type': 'Fruits', 'Quantity': 15, 'Expiration Date': '2024-03-15'},
    {'Name': 'Tomatoes', 'Price': 26.10, 'Product Type': 'Vegetables', 'Quantity': 8, 'Expiration Date': '2024-03-20'},
    {'Name': 'Milk', 'Price': 22.15, 'Product Type': 'Dairy Products', 'Quantity': 2, 'Expiration Date': '2024-03-10'},
    {'Name': 'Bread', 'Price': 10.99, 'Product Type': 'Bakery Products', 'Quantity': 5, 'Expiration Date': '2024-03-12'},
    {'Name': 'Pears', 'Price': 31.52, 'Product Type': 'Fruits', 'Quantity': 12, 'Expiration Date': '2024-04-05'},
    {'Name': 'Butter', 'Price': 48.95, 'Product Type': 'Dairy Products', 'Quantity': 3, 'Expiration Date': '2024-03-18'},
    {'Name': 'Potatoes', 'Price': 10.99, 'Product Type': 'Vegetables', 'Quantity': 10, 'Expiration Date': '2024-03-25'},
    {'Name': 'Cheese', 'Price': 45.97, 'Product Type': 'Dairy Products', 'Quantity': 4, 'Expiration Date': '2024-03-14'},
    {'Name': 'Coffee', 'Price': 100.5, 'Product Type': 'Beverages', 'Quantity': 5, 'Expiration Date': '2024-04-02'},
    {'Name': 'Tea', 'Price': 27.35, 'Product Type': 'Beverages', 'Quantity': 8, 'Expiration Date': '2024-03-22'},
    {'Name': 'Juice', 'Price': 12.8, 'Product Type': 'Beverages', 'Quantity': 6, 'Expiration Date': '2024-03-28'},
    {'Name': 'Eggs', 'Price': 14.3, 'Product Type': 'Dairy Products', 'Quantity': 12, 'Expiration Date': '2024-03-15'},
    {'Name': 'Rice', 'Price': 23.8, 'Product Type': 'Grains', 'Quantity': 5, 'Expiration Date': '2024-03-31'},
    {'Name': 'Honey', 'Price': 154.89, 'Product Type': 'Sweets', 'Quantity': 7, 'Expiration Date': '2024-03-25'},
    {'Name': 'Chicken', 'Price': 45.6, 'Product Type': 'Meat', 'Quantity': 3, 'Expiration Date': '2024-03-20'},
    {'Name': 'Cucumbers', 'Price': 21.15, 'Product Type': 'Vegetables', 'Quantity': 6, 'Expiration Date': '2024-03-28'},
    {'Name': 'Cookies', 'Price': 9.5, 'Product Type': 'Sweets', 'Quantity': 8, 'Expiration Date': '2024-04-05'},
    {'Name': 'Cola', 'Price': 15.9, 'Product Type': 'Beverages', 'Quantity': 10, 'Expiration Date': '2024-03-10'},
    {'Name': 'Oranges', 'Price': 37.5, 'Product Type': 'Fruits', 'Quantity': 14, 'Expiration Date': '2024-03-18'},
]

def spacing():
    print()
    print('*********')
    

# Creating a DataFrame
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

# Read data from the CSV file
df_read = pd.read_csv('data.csv')

# Displaying the read DataFrame
print("Read DataFrame from CSV:")
print(df_read)

# Sorting functions
def sort_by_price(dataframe):
    return dataframe.sort_values(by='Price')

spacing()

def sort_by_quantity(dataframe):
    return dataframe.sort_values(by='Quantity')

spacing()

# Displaying the first 5 elements
print("\nFirst 5 elements:")
print(df.head())
spacing()

# Displaying the last 5 elements
print("\nLast 5 elements:")
print(df.tail())
spacing()

# Selecting products more expensive than 49,25
expensive_over_3 = df[df['Price'] > 49.25]
print("\nProducts more expensive than 49.25:")
print(expensive_over_3)
spacing()

# Minimum price
min_price = df['Price'].min()
print("\nMinimum price:", min_price)
spacing()

# Maximum price
max_price = df['Price'].max()
print("Maximum price:", max_price)
spacing()

# Average price
average_price = df['Price'].mean()
print("Average price:", average_price)
spacing()

# Median
median = df['Price'].median()
print("Median:", median)
spacing()

# Sorting products that are fruits
fruits_df = df[df['Product Type'] == 'Fruits'].sort_values(by='Name')
spacing()

#Sorting products by expiry date
print("Products sorted by date: \n", df.sort_values(by = 'Expiration Date'))
spacing()

# Displaying the sorted DataFrame for fruits
print("\nSorted Fruits:")
print(fruits_df)
spacing()

# Save the sorted DataFrame to a CSV file
fruits_df.to_csv('products_info.csv', index=False)
print("\nSorted Fruits saved to 'products_info.csv'.")
spacing()

print("Sorting by price: ")
print(sort_by_price(df_read))
spacing()

print("Sorting by quantity: ")
print(sort_by_quantity(df_read))
spacing()

# Grouping by the first letter
grouped_products = df.groupby(df['Name'].str[0])
print("\nGrouping by the first letter:")
for group, data in grouped_products:
    print(f"\nLetter: {group}")
    print(data)
