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
    errors.append("Student ID must start with a letter")
if not student_id[1:].isdigit():
    errors.append("Student ID must contain only digits after the first character")
if not len(student_id) == 8:
    errors.append("Student ID must be exactly 8 characters long")
else:
    correct_id = str(student_id)
    
if not full_name.replace(" ", "").isalpha():
    errors.append("Name must contain only letters and spaces")
if not full_name.count(" ") < 1:
    errors.append("Full name must contain first and last name")
if len(full_name) == 0:
    errors.append("Full name cannot be empty")
else:
    correct_name = str(full_name.istitle())

try:
    valid_age = float(age)
except ValueError:
    errors.append("Age must be a number")

if valid_age and 16 <= age <= 99:
    correct_age = str(age)
else:
    errors.append("Age must be between 16 and 99")

major_list = {"CS" or "IT" or "CE" or "DS"}
if major.upper() not in major_list:
    errors.append("Major must be one of the following: CS, IT, CE, or DS")
else:
    correct_major = str(major.upper())

if errors == []:
    print({errors}.strip("'"), end ="\n")
else:
    print("Profile created successfully!")
    print("Student ID:", correct_id)    
    print("Name:", correct_name)
    print("Age:", correct_age)
    print("Major:", correct_major)