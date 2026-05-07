#beginning of week 4 lecture 1
#print

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
print("Item: " + item)
print("Price: " + f"${price:.2f}")
print("Quantity: " + str(quantity))
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
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
sum = float(num1) + float(num2)
difference = float(num1) - float(num2)
product = float(num1) * float(num2)
print(f"The sum of these two numbers is: {int(sum)}, The difference is: {int(difference)}, The product is: {int(product)}")

#3.3
#Create tip calculator
bill_amount = float(input("Enter the bill amount: "))
tip_percentage = int(input("Enter the tip percentage as an integer: "))
tip_amount = (float(f"{bill_amount:.2f}") * (1 * tip_percentage / 100))
total_amount = bill_amount + (float(f"{tip_amount:.2f}"))
print("=== Tip Calculator ===")
print(f"Bill Amount: ${bill_amount:.2f}")
print(f"Tip Percentage: {tip_percentage}%")
print(" ")
print(f"Tip Amount: ${tip_amount:.2f}")
print(f"Total Amount: ${total_amount:.2f}")
# End of week4lecture1.py

#Beginning of week 4 lecture 2
#String
#1.1
# Given the string text = "Programming", write the code to print:
text = "Programming"
# the first character
print(text[0])  # "P"
# the last character (using negative indexing)
print(text[-1])  # "g"
# the fifth character (index 4)
print(text[4])  # "r"
# the length of the string
print(len(text))  # 11

#1.2
print("*" * 20)
print('*' + 'Welcome' .center(18) + '*')
print('*' * 20)

#1.3
word = 'CAT'
print(f"{word[0]}: index 0, index -3")
print(f"{word[1]}: index 1, index -2")
print(f"{word[2]}: index 2, index -1")

#2.1
text = "Computer Science"
print(text[:8])      # "Computer"
print(text[-7:])     # "Science"
print(text[3:6])     # "put"

#2.2
# Extract first 4 characters
date = "2026-02-05"
# Extract year
year = date[:4]
# Extract month
month = date[6:8]
# Extract day
day = date[-2:]
print(f"Year: {year}, Month: {month}, Day: {day}")

#2.3
#reverse text
text1 = "Python"
reversed1 = text1[::-1]
print(reversed1)  # "nohtyP"
# every other character
text2 = "programming"
every_other = text2[::2]
print(every_other)  # "pormig"
#last 3 characters of Hello World reversed
text3 = "Hello, World!"
last_three_reversed = text3[-3:][::-1]
print(last_three_reversed)  # "!dl"

#3.1
text = "hello world, welcome to PYTHON"
# Convert to uppercase
upper_text = text.upper()
print(upper_text)  # "HELLO WORLD, WELCOME TO PYTHON"
# Convert to lowercase
lower_text = text.lower()
print(lower_text)  # "hello world, welcome to python"
# Convert to title case
title_text = text.title()
print(title_text)  # "Hello World, Welcome To Python"

#3.2
sentence = input("Enter a sentence: ")
length = len(sentence)
a_count = sentence.count('a')
hello_sentence = sentence.startswith("Hello")
end_sentence = sentence.endswith(". ! ?")
print(f"Length of the sentence: {length}")
print(f"Number of 'a' characters: {a_count}")
print(f"Sentence starts with Hello: {bool(hello_sentence)}")
print(f"Sentence ends with punctuation: {bool(end_sentence)}")

#3.3
# Messy user input
name = "  JOHN DOE   "
email = "   John.Doe@Email.COM   "
phone = "   (555) 123-4567   "

clean_name = name.strip().title()
clean_email = email.strip().lower()
clean_phone = phone.strip().replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(f"Clean Name: {clean_name}")
print(f"Clean Email: {clean_email}")
print(f"Clean Phone: {clean_phone}")

# End of week 4 exercises