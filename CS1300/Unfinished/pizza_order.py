# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
prices = [6.99, 9.99, 12.99, 16.99]
width = 36
border = "=" * width
menu = border + "\n" + 'Pizza Sizes'.center(36) + "\n" + border 
#A List of the content on the menu 
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99
#Store the chosen index in a variable called size_choice (0-based) and the base price in base_price
order_size_descriptions= []
order_descriptions= []
user_size= 0
# EXERCISE 5 — Wrap everything in a multi-pizza loop
while True:
# (Exercise 1 — display menu)
    print(menu)
    for i in range(len(sizes)):
        print(f"{i + 1}. {sizes[i]}   \t${prices[i]}")
# (Exercise 2 — choose size)
    user_size = int(input("Pick a pizza size (1-4): "))
    if 1 <= user_size <= 4:
        size_choice = sizes[user_size - 1]
        order_size_descriptions.append(size_choice)
        user_size_index = user_size - 1  
        user_size_price = prices[user_size_index]  
        order_size_prices=[]
        order_size_prices.append(user_size_price)
# (Exercise 3 — add toppings)
        topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions","Sausage", "Bacon", "Extra Cheese", "Pineapple"]
        print(border)
        print("Here's our avaliable toppings!") 
        print(border)
        print("Available toppings ($1.50 each):")
        print(border)
        for i, topping in enumerate(topping_names, start=1):
            print(f"{i}. {topping}") 
        print(border)

        user_toppings = []
        order_toppings_descriptions = []
        topping_price = 1.50
        total_toppings = 0
        while True:
            user_toppings = input("Add topping or print \"done\": ")
            if user_toppings == "done":
                total_toppings == total_toppings
                break
            user_toppings = int(user_toppings)
            if 1 <= user_toppings <= len(topping_names):
                chosen = topping_names[user_toppings - 1]
                if chosen in order_toppings_descriptions:
                    print("Already added " + chosen + "!")
                else:
                    print("✓ Added " + chosen)
                    order_toppings_descriptions.append(chosen)
                    total_toppings +=1
                    break
            
                total_toppings = len(order_toppings_descriptions)
                toppings_str = ", ".join(order_toppings_descriptions) if order_toppings_descriptions else "No toppings"
                pizza_description = f"[{sizes[user_size_index]}]", f"[{toppings_str}]"
                total = user_size_price + (total_toppings * topping_price)
                order_descriptions.append(pizza_description)
                order_prices.append(total)
#EXERCISE 4 — Calculate price and store the pizza
                subtotal = 0
                for price in order_prices:
                    subtotal += price
                    tax= subtotal * 0.07
                    total_1= subtotal + tax
                    continue
#Before printing the final total, ask the customer if they have a discount code. 
#Valid codes: "STUDENT10" → 10% off, "HALFOFF" → 50% off.
                attempt= 0
                while attempt < 3:
                    user_discount= input("Type discount code (type 'none' to skip): ").upper()
                    if not user_discount == "none" or "None":
                        attempt += 1
                        print(f"amount of attempts: {attempt} out of 3".center(width))
                    if user_discount == "STUDENT10":
                        print("10 percent discount applied!")
                        discount= (total_1) * .10
                        break
                    if user_discount == "HALFOFF":
                        print("50 percent discount applied!")
                        discount= (total_1) * .50
                        break
                    if user_discount == "NONE":
                        discount = 0
                        break
                    if attempt == 3:
                        print("Discount code NOT applied.")
                        discount= 0
                        break
                    else:
                        print("Invalid code")
                        user_discount= input("Type discount code (type 'none' to skip): ").upper()
                    final_total = total_1 - discount    
# (Exercise 6 — print receipt)
                    print("=" * width)
                    print("YOUR ORDER RECEIPT".center(width))
                    print("=" * width)
                    for i in range(len(order_descriptions)):
                        print(f"{i + 1}. {order_descriptions[i]}")
                        print(f"\t\t\t${order_prices[i]:.2f}")
                        print("-" * width)
        subtotal = 0
        for sum in order_prices:
            subtotal += sum
        print(f"{'Subtotal:':<23}\t${subtotal:.2f}")
        tax = subtotal * 0.07
        print(f"{'Tax(7%):':<23}\t${tax:.2f}")
        print(f"{'Total:':<23}\t${final_total:.2f}")
    # EXERCISE 7 — Find most expensive pizza
    #write loop to find the most expensive pizza and print it out with its price
    max_expensive_price = 0
    max_expensive_index = 0
    for i in range(len(order_prices)):
        if order_prices[i] > max_expensive_price:
            max_expensive_price = order_prices[i]
            max_expensive_index = i
    print("The most expensive pizza is: ")
    for max_expensive_index in order_descriptions:
        print(f"{max_expensive_index} at\t{max_expensive_price:.2f}")
    # EXERCISE 9 — Count pizzas by size
    # Print a summary showing how many pizzas of each size were ordered.
    size_counts = {size: 0 for size in sizes}
    for description in order_descriptions:
        for size in sizes:
            if size in description:
                size_counts[size] += 1
                print("-"*width)
                print("Pizza Size Summary: ")
                print(f"{size_counts[size]} {size} pizza(s)")
                print("-=" * 16)
                print("\n")
                print("***********THANK YOU***********")
                break
                while True:        
                    order_another= input("Order another pizza? (yes/no): ")
                    if order_another == "yes".lower() or order_another == "y".lower():
                        print("Ordering next pizza")
                        continue
                    elif order_another == "no".lower() or order_another == "n".lower():
                        print("Thank you for your order!")
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        order_another = input("Order another pizza? (yes/no): ")
                
            else:
                print(("Invalid topping"))
                user_toppings = input("Add topping or print \"done\": ")
    else:
        print("Invalid choice")
#Exercise 10 — Code a post reciept that prints "No pizza ordered" and skips the rest if the user doesn't order any pizzas.
    #if len(order_descriptions) == 0:
    #    print("No pizza ordered.")
    #    break


    #Exercise 8 — Discount code with attempt limit

    