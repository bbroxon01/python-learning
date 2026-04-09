# Coding problem 1
age = int(input("How old are you? "))
matinee = str(input("Is this a matinee showing? yes/no: "))
if age < 13:         
    age_group = "Child"
    if matinee == "yes":
        price = "$6.00"
    else:
        price = "$8.00"
elif 13 <= age <= 17:
    age_group = "Teen"
    if matinee == "yes":
        price = "$7.00"
    else:
        price = "$10.00"
elif age >= 18:
    age_group = "Adult"
    if matinee == "yes":
        price = "$8.00"
    else:
        price = "$13.00"
elif age >= 65:
    age_group = "Senior"
    if matinee == "yes":
        price = "$6.00"
    else:
        price = "$7.00"
print(f"Age group: {age_group}")
print(f"Ticket price: {price}")

# Coding problem 2
errors = []
student_id = str(input("Enter student ID: "))
full_name = str(input("Enter full name: "))
age = int(input("How old are you? "))
major = str(input("What is your major? "))

if not student_id[0].isalpha():
    errors.extend("Student ID must start with a letter")
elif not student_id[1:].isdigit():
    errors.extend("Student ID must contain only digits after the first character")
elif not len(student_id) == 8:
    errors.extend("Student ID must be exactly 8 characters long")
else:
    correct_id = str(student_id)
    
if not full_name.replace(" ", "").isalpha():
    errors.extend("Name must contain only letters and spaces")
if not len(full_name.split(" ")) >= 2:
    errors.extend("Full name must contain first and last name")
if not full_name.strip():
    errors.extend("Full name cannot be empty")
else:
    correct_name = str(full_name.istitle())

try:
    valid_age = float(age)
except ValueError:
    errors.extend("Age must be a number")

if valid_age and 16 <= age <= 99:
    correct_age = str(age)
else:
    errors.extend("Age must be between 16 and 99")

major_list = {"CS", "IT", "CE", "DS"}
if major.upper() not in major_list:
    errors.extend("Major must be one of the following: CS, IT, CE, or DS")
else:
    correct_major = str(major.upper())

if errors == []:
    all_errors = errors
    print({all_errors})
else:
    print("Profile created successfully!")
    print("Student ID:", correct_id)    
    print("Name:", correct_name)
    print("Age:", correct_age)
    print("Major:", correct_major)

#Coding problem 3
#Order of operations

#menu list
#selection variables
#create coffee variables
#add cheese to sandwich?
#salad dressing?
#combo variables
#name validation 
#item quantity
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
            cheese_sandwich = "Sandwich with Cheese"
            sandwich_price = sandwich + cheese
            combo_price = sandwich_price + coffee_price - 1.50
        else:
            cheese_sandwich = "Sandwich with No Cheese"
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
print("Customer: " + f"{name}")
print("Item: " + f"{item}")
print("Quantity: " + f"{str(quantity)}")
print("Unit Price: " + f"{str(unit_price):.2f}")
print("Subtotal: " + f"{unit_price * quantity:.2f}")
print("Tax (7%): " + f"{unit_price * quantity * 0.07:.2f}")
print("Total: " + f"{unit_price * quantity * 1.07:.2f}")
print(("=" * width) + "\n" + "Thank you for your order!".center(width) + "\n" + "Have a great day!".center(width) + "\n" + ("=" * width))
