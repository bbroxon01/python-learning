# 1.1
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

# 1.2
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
        
# 1.3
# beginner
inventory = {}
inventory['apples'] = 5
inventory['oranges'] = 3
inventory['bananas'] = 2
print(inventory)

# intermediate
scores = {'Team A': 45, 'Team B': 38}
scores['Team B'] = 52
scores['Team C'] = 41
print(scores.pop('Team A'))

# advanced
# shopping cart system
shopping_cart = {}
shopping_cart['shoes']= "23.99"
shopping_cart['socks']= "3.99"
shopping_cart['shirt']= "12.99"
print(shopping_cart.pop('socks'))
print(shopping_cart)
shopping_cart_total = float(shopping_cart['shoes']) + float(shopping_cart['shirt'])
print(shopping_cart_total)

# 2.1
# beginner
# which of these are valid dictionary keys?

#a) "student_name" # valid (reason: string)
#b) [1, 2, 3] # invalid (reason: list)
#c) 100 # valid (reason: number)
#d) ("x", "y") # valid (reason: tuple)
#e) {"a": 1} # invalid (reason: dictionary)
#f) frozenset({1,2}) # valid (reason: frozenset)

# 2.2


#2.3
#beginner 1
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
    print(f"{fruit} is {color}")

#beginner 2
#2. Without running the code, predict what list(colors.items()) returns.

#it should return a list of tuples for each fruit with it's associated color