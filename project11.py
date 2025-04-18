menu = {
    'Pizza': 100,
    'Pasta': 80,
    'Burger': 150,
    'Salad': 200,
    'Cofee': 100,
    'Panipuri': 90,
    'Coketail': 200
}
print("Welcome to Cafe House")
print("Pizza: Rs100\nPasta: Rs80\nBurger: Rs150\nSalad: Rs200\nCofee: Rs100\nPani pure: Rs90\nCoketail: Rs200\n")

order_total = 0

# Convert the menu keys to lowercase for case-insensitive comparison
menu_lower = {key.lower(): value for key, value in menu.items()}

item_1 = input("Enter the item that you want: ").lower()  # Convert user input to lowercase
if item_1 in menu_lower:
    order_total += menu_lower[item_1]  #0+90
    print(f"Your item {item_1} has been added to your order.")
else:
    print("Please order something else that we can serve you, this item is not available.")

another_order = input("Do you want to add another item? (Yes/No): ").lower()  # Convert input to lowercase
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()  # Convert user input to lowercase
    if item_2 in menu_lower:
        order_total += menu_lower[item_2]#0+90
        print(f"{item_2} has been added to your order.")
    else:
        print(f"{item_2} is not available.")

print(f"The total amount of items is Rs {order_total}")
