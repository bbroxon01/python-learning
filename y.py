#Coding problem 3
#order of operations
#menu list
#selection variables
#name validation 
#item size variables
#add cheese to sandwich
#add salad dressing
#add combo
#calculate total price
#print receipt

#create menu list
import sys
sandwich = float(6.00)
cheese = float(0.75)
coffee = float(3.50)
combo = float(8.00)
width = 36
menu = f"{"=" * width}\n{("CAMPUS CAFE MENU").center(36)}\n{"=" * width}\n{("1. Coffee") + ("$3.50").rjust(width - len("1. Coffee"))}\n{("2. Sandwich") + ("$6.00").rjust(width - len("2. Sandwich"))}\n{("3. Salad") + ("$5.50").rjust(width - len("3. Salad"))}\n{("4. Combo (Sandwich + Coffee)") + ("$8.00").rjust(width - len("4. Combo (Sandwich + Coffee)"))}\n{("5. Exit")}\n{"=" * 36}"
print(menu)
#make selection variables
selection = int(input("Enter your selection (1-5): "))
if selection == 1:
#create coffee variables
    coffee = float(3.50)
    coffee_size = str(input("What size coffee would you like? (Small, Medium, Large) "))
    if coffee_size.lower() == "small" or coffee_size.lower() == "s":
        coffee_price = coffee
    elif coffee_size.lower() == "medium" or coffee_size.lower() == "m":
        coffee_price = coffee + 1.00
    elif coffee_size.lower() == "large" or coffee_size.lower() == "l":
        coffee_price = coffee + 2.00
    else:
        coffee_price = coffee
        print("Invalid coffee size, defaulting to Small")    
elif selection == 2:
#add cheese to sandwich?
    sandwich = float(6.00)
    cheese = float(0.75)
    add_cheese = str(input("Add cheese? (yes or no) "))
    if add_cheese.lower() == "yes" or add_cheese.lower() == "y":
        cheese_sandwich = "Sandwich with cheese"
        sandwich_price = sandwich + cheese
    else:
        cheese_sandwich = "Sandwich with no cheese"
        sandwich_price = sandwich
elif selection == 3:
#salad dressing?
    salad = float(5.50)
    salad_dressing = str(input("What kind of salad dressing" + "\nRanch, Italian, Vinaigrette, None) "))
    if salad_dressing.lower() == "ranch":
        salad_dressing = "Ranch"
    elif salad_dressing.lower() == "italian":
        salad_dressing = "Italian"
    elif salad_dressing.lower() == "vinaigrette":
        salad_dressing = "Vinaigrette"
    elif salad_dressing.lower() == "none" or salad_dressing.lower() == "n":
        salad_dressing = "no"
    else:
        salad_dressing == "" or not salad_dressing == salad_dressing.alnum()
        salad_dressing = "no"
        print("Invalid salad dressing, defaulting to no dressing")

elif selection == 4:
#combo variables
    if combo:
        coffee_size = str(input("What size coffee would you like? (Small, Medium, Large) "))
        if coffee_size.lower() == "small" or coffee_size.lower() == "s":
            coffee_price = coffee
        elif coffee_size.lower() == "medium" or coffee_size.lower() == "m":
            coffee_price = coffee + 1.00
        elif coffee_size.lower() == "large" or coffee_size.lower() == "l":
            coffee_price = coffee + 2.00
        else:
            coffee_price = coffee
            print("Invalid coffee size, defaulting to Small")
    
        add_cheese = str(input("Add cheese to sandwich? (yes or no) "))
        if add_cheese.lower() == "yes" or add_cheese.lower() == "y":
            cheese_sandwich = "Sandwich with cheese"
            sandwich_price = sandwich + cheese
            combo_price = sandwich_price + coffee_price - 1.50
        else:
            cheese_sandwich = "Sandwich with no cheese"
            sandwich_price = sandwich
        
        combo_price = sandwich_price + coffee_price - 1.50
elif selection == 5:
    print("Thank you for visiting the Campus Cafe!")
    sys.exit()
else:
    1 > selection or selection > 5 or selection == ""
    print("Invalid selection")
    selection = int(input("Enter your selection (1-5): "))
    
#name validation
name = str(input("What is your name? "))
if not name.strip():
    print("Name cannot be empty:")
    name = str(input("What is your name? "))
else:
    good_name = name.istitle()
#quantity
quantity = int(input("How many items would you like to order? "))
#format selection for receipt   
if selection == 1:
    item = f"{coffee_size.capitalize()} Coffee"
    unit_price = coffee_price
elif selection == 2:
    item = f"{cheese_sandwich}"
    unit_price = sandwich_price
elif selection == 3:
    item = f"Salad with {salad_dressing} Dressing"
    unit_price = salad
elif selection == 4:
    item = f"Combo ({cheese_sandwich} + {coffee_size.capitalize()} Coffee)"
    unit_price = combo_price
else:
    item = "No items ordered"
#print formatted receipt
print("\n" + ("=" * width + "\n") + "CAMPUS CAFE RECEIPT".center(width) + "\n" + ("=" * width))
print("Customer: " + f"{name.rjust(7)}")
print("Item: " + f"{item.rjust(12)}")
print("Quantity: " + f"{str(quantity).rjust(7)}")
print("Unit Price: " + f"{str(unit_price).rjust(4)}")
print("Subtotal: " + f"{unit_price * quantity:.2f}".rjust(6))
print("Tax (7%): " + f"{unit_price * quantity * 0.07:.2f}".rjust(6))
print("Total: " + f"{unit_price * quantity * 1.07:.2f}".rjust(6))
print("=" * width)
print("\n" + "Thank you for your order!".center(width) + "\n" + "Have a great day!".center(width) + "\n" + ("=" * width))