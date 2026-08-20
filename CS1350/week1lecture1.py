# unit 1.1
#demo
contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Pizza Place": "555-9999"
}

print(contacts)
print(type(contacts))

# creating with dict()
prices = dict(burger=8.99, fries=3.49, soda=1.99)
print(prices)

# empty dictionary
my_grades = {}
print(my_grades) 

#beginner
my_info = {
    "Name": "Brandon",
    "Age": "33",
    "Major": "Information Systems"
}
print(my_info)
#intermediate
menu = {
    "burger": 8.99,
    "hotdog": 5.99,
    "fries": 3.49,
    "soda": 1.99
}
course_credits = {
    "CS1300": 3,
    "CS1350": 3,
    "IS1150": 3,
    "ACC1010": 3
}
#advanced
weekly_temps = dict(Monday=75, Tuesday=80, Wednesday=78, Thursday=82, Friday=85, Saturday=88, Sunday=90)

# unit 1.2
# demo
grades = {"Alice": 85, "Bob": 92, "Charlie": 55}
print(grades.get("Gerald", 0))

#beginner
pet = {"name": "Buddy", "type": "dog", "age": 3}
print(pet["name"] + ":", pet["type"], pet["age"])

#intermediate
print(pet.get("color", "Unknown"))

grades = {"Alice": 85, "Bob": 92, "Charlie": 55}
for student in grades:
    grade = grades.get(student)
    if grade >= 60:
        print(student, "passed with a grade of", grade)
    else:
        print(student, "failed with a grade of", grade)

#advanced
products = {"laptop": "$999.99", "mouse": "$29.99", "keyboard": "$79.99"}

for product in products:
    search = input("Search for a product: ")
    if search == "exit":
        import sys
        sys.exit()
    if search not in products:
        print(search.capitalize() + ": not available")    
    else:
        print(products[product])
        