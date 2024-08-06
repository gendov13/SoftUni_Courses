orders = {}
while True:
    products = input()
    if products == "buy":
        break
    name, price, quantity = products.split()
    price = float(price)
    quantity = int(quantity)
    if name not in orders:
        orders[name] = {"quantity": quantity, 'price': price}
    else:
        orders[name]['quantity'] += quantity
        if orders[name]['price'] != price:
            orders[name]['price'] = 0
            orders[name]['price'] = price


for product_name, details in orders.items():
    total_price = details['quantity'] * details['price']
    print(f"{product_name} -> {total_price:.2f}")

