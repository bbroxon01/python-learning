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
