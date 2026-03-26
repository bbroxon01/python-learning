width = 36
pizza_size = ['Personal (8")', 'Medium (12")', 'Large (16")', 'Party (20")']
base_prices = ["6.99", "9.99", "12.99", "16.99"]
    
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
topping_price = 1.50 

order_descriptions = []
order_prices = []


menu = print(("="*width) + "\n" + "PIZZA SIZES".center(width) + "\n" + ("="*width) + "\n")
for size in range(len(pizza_size)):
    print(f"{size + 1}."), end=""
    print({pizza_size[size]})
    print(f"${base_prices[size]:.>5}")
print("=" * width)

choice = input("Choose a size (1-4) ")
while choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please choose a size (1-4).")
    choice = input("Choose a size (1-4)")
size_choice = int(choice) - 1
order_descriptions.append(pizza_size[size_choice])
order_prices.append(float(base_prices[size_choice]))