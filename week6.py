# unit 1 beginner exercise
a = 5 
b = 12

if a > 3:
    if b > 10:
        print("X")
    else:
        print("Y")
else: 
    print("Z")
# exercise prints "X"

# unit 1 intermediate exercise
# movie age rating system

age = int(input("Enter your age: "))
rating = input("Enter the movie rating (G, PG-13, or R): ")
if age >= 13:
    if rating == "G".lower():
        print("Access granted".capitalize())
elif 13 <= age < 18:
    if rating == "PG-13".lower() or rating == "G".lower():
        print("Access granted".capitalize())
    else:
        print("Access denied".capitalize())
else:
    print("Access granted".capitalize())
    
# unit 1 advanced exercise
age = int(input("Enter your age: "))
rating = input("Enter the movie rating (G, PG-13, or R): ")
if age <= 13 and rating == "G".lower():
    print("Access granted")
elif  13 <= age < 18 and rating != "R".lower():
    print("Access granted")
elif age >= 18:
    print("Access granted")
else:
    print("Access denied")
    
# unit 2 beginner exercise
if points >=100:
    
level = "gold" if points >= 100 else "silver"

# unit 2 intermediate exercise
# write a single line that assigns 'result' to "pass" if score is >= 60 and "fail" otherwise
# then print f-string: "status: pass" or "Status: fail"

result = "Pass" if score >= 60 else "Fail"
print(f"status: {result}")

# unit 2 advanced exercise
x = 5
y = 10
result = "yes" if x > 3 else "no" if y > 20 else "maybe"
# ("no" if y > 20 else "maybe") is evaluated first, then "yes" if x > 3 else the result of the previous evaluation

# unit 3 beginner exercise
# find and fix the bug:

age = 18

if age >= 18:
    print("Can vote")
else:
    print("Cannot vote")

# unit 3 intermediate exercise
# this code is supposed to classify a numnber as positive, negative, or zero. Find ALL the bugs:
num = 0

if num > 0:
    category = "positive"
if num < 0:
    category = "negative"
else:
    category = "zero"

print(f"{num} is {category}")
 
#missing else statement for num = 0
# unit 3 advanced exercise

amount = 75
is_member = True

if amount > 100 and is_member:
    discount = 0.20
elif 50 < amount <= 100 and is_member:
    discount = 0.10
elif amount < 50 and is_member:
    discount = 0.05
else:
    discount = 0.0
total = amount * (1 - discount)
print(f"Total amount after discount: ${total:.2f}")
# end of week6lecture1 exercises

#beginning of week6lecture2 exercises
# unit 1 beginner exercise

age = int(input("Enter your age: "))
if 0 <= age < 120:
    print("Valid age")
else:
    print("Invalid age")    

# unit 1 intermediate exercise
phone_number = input("Enter your phone number: ")
if len(phone_number.replace("(", "").replace(")", "").replace("-", "")) == 10 and phone_number.replace("(", "").replace(")", "").replace("-", "").isdigit():
    print("Valid phone number")
elif len(phone_number.replace("(", "").replace(")", "").replace("-", "")) != 10 and phone_number.replace("(", "").replace(")", "").replace("-", "").isdigit():
    print("Invalid phone number - incorrect length")
elif not phone_number.replace("(", "").replace(")", "").replace("-", "").isdigit():
    print("Invalid phone number - contains non-numeric characters")
    
# unit 1 advanced exercise
password = input("Create a password: ")
if len(password) < 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password) and password.lower() != "password":
    print("Password too short")
elif len(password) >= 8 and not any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password) and password.lower() != "password":
    print("Password missing digit")
elif len(password) >= 8 and any(c.isdigit() for c in password) and not any(c.isupper() for c in password) and any(c.islower() for c in password) and password.lower() != "password":
    print("Password missing uppercase letter")
elif len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and not any(c.islower() for c in password) and password.lower() != "password":
    print("Password missing lowercase letter")
elif len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c.islower() for c in password) and password.lower() == "password":
    print("Password cannot be 'password'")
else:
    print("Strong password")
    
# unit 2 beginner exercise
favorite_color = input("Enter your favorite color:" +"\n" + "Your options are: red, blue, green, yellow, orange, and purple: ")
if favorite_color.lower() in ["red", "blue", "green", "yellow", "orange", "purple"]:
    print(f"Your favorite color is {favorite_color}")
else:
    print("Invalid color choice")
    
# unit 2 intermediate exercise
email = input("Enter your email address: ")
if not email:
    print("Email address cannot be empty")
elif not email.count('@') == 1:
    print("Invalid email address - must contain exactly one '@' symbol")
elif not email.endswith((".com", ".net", ".org")):
    print("Invalid email address")

#unit 2 advanced exercise

#unit 3 beginner exercise

#unit 3 intermediate exercise

#unit 3 advanced exercise
