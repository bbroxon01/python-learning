#for loop to print all lists without "'[]'"
width = 36
pizza_sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
base_prices = ["6.99", "9.99", "12.99", "16.99"]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 
order_descriptions = []
order_prices = []

menu = ("="*width) + "\n" + "PIZZA SIZES".center(width) + "\n" + ("="*width)
print(menu)
for size_choice in range(len(pizza_sizes)):
    print(f"{size_choice + 1}. ", f"{pizza_sizes[size_choice]}", "\t" f"${base_prices[size_choice]}")
print("=" * width)

choice = input("Choose a size (1-4): ")
print("")
while choice not in ["1", "2", "3", "4"]:
    print("Invalid choice")
    if choice in ["1", "2", "3", "4"]:
        choice = input("Choose a size (1-4):")
        print("Order Stored")
#appended description and price        
order_descriptions.append(pizza_sizes[size_choice])
order_prices.append(float(base_prices[size_choice]))

for topping in range(len(topping_names)):
    print(f"{topping + 1}. ",  f"{topping_names[topping]}")
selection = "Bad"
all_toppings = []
while not selection == "done":
    selection = input("Choose a topping/s\nType \"done\" when finished ")
    if selection == "done":
        for topping in all_toppings:
            print(f"Added {topping}")
        break
    if not selection.isdigit():
        print("Invalid Selection")
        continue
    if int(selection) not in range(len(topping_names)):
        print("Invalid selection")
        continue
    topping_name = topping_names[int(selection)+1] 
    if topping_name not in all_toppings:
        all_toppings.append(topping_name)
        
        price += topping_price
        print(f"Added {topping_name}")
    else:
        print("Duplicate Selection")
        
for description in order_descriptions:
    print(description)
for price in order_prices:
    print(f"${price}")