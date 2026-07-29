# List of Tuples

delivery_orders = [
    ("Laptop", 2, 350),
    ("Mouse", 5, 20),
    ("Monitor", 3, 220),
]

def add_delivery_order(item: str, quantity: int, price: float):
    delivery_orders.append((item, quantity, price))

add_delivery_order("Keyboard", 5, 1000)
add_delivery_order("Fan", 2, 30)

print(delivery_orders)

def display_high_value_items(threshold_value: int): # Adds orders above 500 to list and prints with order_cost
    high_value_items = []

    for order in delivery_orders:
        order_cost = order[1] * order[2]
        if (order_cost) > threshold_value:
            high_value_items.append(order[0])
            print(high_value_items, ": ", order_cost)

display_high_value_items(500)
