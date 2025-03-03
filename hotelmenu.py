#Define the menu of restaurant
menu = {
    'Pizza':79,
    'Burger':49,
    'Fried':49,
    'Salad':29,
    'Noddles':70,
    'Sushi':99,
    'Pasta':80,
    'Coffee':90,
}
#Greet
print("welcome to Chillihub Restaurant")
print("Pizza: Rs79\nBurger:Rs49\nFried:Rs49\nSalad:Rs29\nNoddles:Rs70\nSushi:Rs99\nPasta:Rs80\nCoffee:90")

order_total = 0
#80+70=150

item_1 = input("enter the name of items you want to order =" )
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input ("Do you want to add another item? (Yes/No)")
if another_order =="Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is  {order_total}")   
