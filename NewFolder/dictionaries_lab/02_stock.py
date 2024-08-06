data = input().split()

stock_products = {}

for i in range(0, len(data), 2):
    product = data[i]
    quantities = data[i + 1]
    stock_products[product] = quantities

items_to_search = input().split()

for item in items_to_search:
    if item in stock_products:
        print(f"We have {stock_products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")