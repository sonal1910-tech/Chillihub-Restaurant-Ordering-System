# Define the menu of the restaurant
menu = {
    'Pizza': 79,
    'Burger': 49,
    'Fried': 49,
    'Salad': 29,
    'Noodles': 70,
    'Sushi': 99,
    'Pasta': 80,
    'Coffee': 90,
}

# Greet the customer
print("Welcome to Chillihub Restaurant!")
print("\nMenu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")

order_total = 0
ordered_items = []

# Ordering Loop
while True:
    item = input("\nEnter the name of the item you want to order: ").title()
    
    if item in menu:
        order_total += menu[item]
        ordered_items.append(item)
        print(f"✅ {item} has been added to your order.")
    else:
        print(f"❌ {item} is not available on the menu.")

    another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_order != 'yes':
        break

# Display final bill
print("\nYour Order Summary:")
for ordered_item in ordered_items:
    print(f"- {ordered_item}: Rs {menu[ordered_item]}")
print(f"Total Amount to Pay: Rs {order_total}")
print("Thank you for visiting Chillihub Restaurant! 😊")
