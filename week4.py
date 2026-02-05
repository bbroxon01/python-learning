# week4lecture1.py
# 1.1
# Produce the following output using print statements:
print("Welcome to Python Programming")
print("Course: CS 1300")
print("Instructor: Xin Wang")
#1.2
# print 2026-01-27 using a single print statement and sep parameter
year = 2026
month = "01"
day = 27
print(year, month, day, sep="-")
#1.3
# Print "Python is awesome!" using multiple print statements and end parameter
print("Python", end=" ")
print("is", end=" ")
print("awesome!")
#2.1
Line1 = "Python says:"
Line2 = "\"Hello, World!\""
Line3 = "\'Welcome to Programming\'"
print(Line1 + "\n" + "\t" + Line2 + "\n" + "\t" + Line3)
#2.2
# Student Report
#--------------
#Name: Alice Smith
#GPA: 3.85
#Status: Dean's List
#first_name = "Alice"
#last_name = "Smith"
#gpa = 3.8537
#on_deans_list = True

first_name = "alice"
last_name = "smith"
gpa = 3.8537
on_deans_list = True
student_name = "Name:" + " " + (f"{first_name.capitalize()} {last_name.capitalize()}")
deans_list = gpa >= 3.5
if deans_list:
    status = "Status:" + " " + "Dean's List"
else: 
    status = "Status:" + " " + "Get your grades up!"
print("Student Report")
print("--------------")
print(student_name)
print(f"GPA:\t{gpa:.2f}\n{status}")
#2.3

#Item: Widget
#Price: $19.99
#Quantity: 3
#-----------
#Subtotal: $ 59.97
#Tax (7%): $ 4.20
#Total: $ 64.17

item = "Widget"
price = 19.99
quantity = 3
tax_rate = 0.07
subtotal = price * quantity
tax = subtotal * tax_rate
total = subtotal + tax
print("Item:" + " " + item)
print("Price:" + " " + f"${price:.2f}")
print("Quantity:" + " "+ str(quantity))
print("-----------")
print(f"Subtotal: $ {subtotal:.2f}")
print(f"Tax (7%): $ {tax:.2f}")
print(f"Total: $ {total:.2f}")
# End of week4lecture1.py

# Beginning of week4lecture2.py
# 3.1

# write a program that asks for the user's favorite color and food, then prints a message using both
favorite_food = input("Enter your favorite food: ")
favorite_color = input("Enter your favorite color: ")
print(f"Your favorite food is {favorite_food}")
print(f"Your favorite color is {favorite_color}")
#3.2

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
sum = float(num1) + float(num2)
difference = float(num1) - float(num2)
product = float(num1) * float(num2)
print(f"The sum of these two numbers is: {int(sum)}, The difference is: {int(difference)}, The product is: {int(product)}")
#3.3

