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
#beginner
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(f"There are {len(temps.keys())} days")

#intermediate
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(max(temps.values()))
print(min(temps.values()))
if "Friday" not in temps.items():
    print("Day not in temps")
else:
    print(temps.items("Friday"))

temps.setdefault("Thursday", 70)
print(temps.items())
print(temps.keys())
temps.setdefault("Friday", 69)
print(temps.items())

#advanced
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
print(sum(prices.values()))
print(f"{sum(prices.values()) / len(prices):.1f}")
for item, price in prices.items():
    min_value = min(prices.items())
    max_value = max(prices.items())
print(min_value)
print(max_value)

import sys
view = prices.keys()
as_list = list(prices.keys())
print(f"View: {sys.getsizeof(view)} bytes")
print(f"List: {sys.getsizeof(as_list)} bytes")

prices.update({"tv": 1299, "desktop": 1599, "refrigerator": 2199})
print(prices)

#2.3
#beginner 1
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
    print(f"{fruit} is {color}")

#beginner 2
#2. Without running the code, predict what list(colors.items()) returns.
#it should return a list of tuples for each fruit with it's associated 

#intermediate
prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
count = 0
for item, price in prices.items():
    taxed_price = price * 1.10
    print(f"{item}:" + f" ${price:.2f}"+ " + tax = " + f"${taxed_price:.2f}")
    if price > 4.00:
        count += 1
        print(f"There are {count} items that cost more than $4.00")        

x=10
y=20
x, y = y, x

first, *rest, last = [1, 2, 3, 4, 5]
print(f"first= {first}, last= {last}, rest = {rest}")

#advanced
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
best_name, best_grade = max(scores.items(), key=lambda x: x[1])
print(f"The student with the highest grade is {best_name} with a grade of {best_grade}.")
passed = []
failed = []
for student, grade in scores.items():
    if grade >= 70:
        passed.append(student)
    else:
        failed.append(student)
        
print(f"These students passed: {passed}")
print(f"These students failed: {failed}")

average = sum(scores.values()) / len(scores)
print(f"The class' average is {average}")
deviation = []
for student, grade in scores.items():
    deviation = grade - average
    print(f"{student}" +"'s grade is " + f"{abs(deviation):.1f}" + " from the average.")

#advanced 4
print("Items() Vs Keys() + Lookup")
print("-" * 26)
import time
big_dict = {i: i*2 for i in range(50000)}
start = time.time()
for k, v in big_dict.items():
    _ = k + v
items_time = time.time() - start
start = time.time()
for k in big_dict.keys():
    v = big_dict[k]
    _ = k + v
keys_time = time.time() - start
print(f"items(): {items_time:.4f}s")
print(f"keys() + lookup: {keys_time:.4f}s")
print(f"items() is {keys_time/items_time:.1f}x faster")