# unit 1 
#beginner
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

#intermediate
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
    
#advanced
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
    
# unit 2
#beginner
#if points >=100:
#level = "gold" if points >= 100 else "silver"
points = input("How many points did you get? ")
level = "gold" if points >= 100 else level = "silver"

#intermediate
# write a single line that assigns 'result' to "pass" if score is >= 60 and "fail" otherwise
# then print f-string: "status: pass" or "Status: fail"
score = input("What is your score? ")
result = "Pass" if score >= 60 else "Fail"
print(f"status: {result}")

#advanced
x = 5
y = 10
result = "yes" if x > 3 else "no" if y > 20 else "maybe"
# ("no" if y > 20 else "maybe") is evaluated first
#then "yes" if x > 3 
#else the result of the previous evaluation

# unit 3
#beginner
# find and fix the bug:
age = 18
if age >= 18:
    print("Can vote")
else:
    print("Cannot vote")

#intermediate
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
#advanced
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
# end of week 6 lecture 1

#beginning of week 6 lecture 2
# unit 1
#beginner
age = int(input("Enter your age: "))
if 0 <= age < 120:
    print("Valid age")
else:
    print("Invalid age")    

#intermediate
phone_number = input("Enter your phone number: ")
if len(phone_number.replace("(", "").replace(")", "").replace("-", "")) == 10 and phone_number.replace("(", "").replace(")", "").replace("-", "").isdigit():
    print("Valid phone number")
elif len(phone_number.replace("(", "").replace(")", "").replace("-", "")) != 10 and phone_number.replace("(", "").replace(")", "").replace("-", "").isdigit():
    print("Invalid phone number - incorrect length")
elif not phone_number.replace("(", "").replace(")", "").replace("-", "").isdigit():
    print("Invalid phone number - contains non-numeric characters")
    
#advanced
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
    
#unit 2 
#beginner
favorite_color = input("Enter your favorite color:" +"\n" + "Your options are: red, blue, green, yellow, orange, and purple: ")
if favorite_color.lower() in ["red", "blue", "green", "yellow", "orange", "purple"]:
    print(f"Your favorite color is {favorite_color}")
else:
    print("Invalid color choice")
    
#intermediate
email = input("Enter your email address: ")
if not email:
    print("Email address cannot be empty")
elif not email.count('@') == 1:
    print("Invalid email address - must contain exactly one '@' symbol")
elif not email.endswith((".com", ".net", ".org")):
    print("Invalid email address")

#advanced

    
#unit 3
#beginner

#intermediate

#advanced

#end of week 6 lecture 2