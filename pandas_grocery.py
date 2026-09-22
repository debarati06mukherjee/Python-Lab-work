import pandas as pd

# Create a Series of 10 grocery products with their prices
products = pd.Series({
    "Rice": 60,
    "Sugar": 45,
    "Milk": 55,
    "Bread": 40,
    "Oil": 120,
    "Salt": 25,
    "Tea": 80,
    "Biscuits": 30,
    "Dal": 90,
    "Flour": 50
})

# i) Print the products with name and price
print("Products and Prices:")
print(products)

# ii) Find the average price
average = products.mean()
print("\nAverage price:", average)

# iii) Print the products whose price is more than average price
print("\nProducts with price more than average:")
print(products[products > average])

# iv) List the products whose price is less than 50
print("\nProducts with price less than 50:")
print(products[products < 50])