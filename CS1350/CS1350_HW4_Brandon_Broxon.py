#3.1
#beginner
inventory = {"apples": 50, "bananas": 30, "oranges": 25}
for item in inventory:
    print(item)
total_items = sum(inventory.values())
for item, value in inventory.items():
    print(f"{item}: {value}")


#3.1 intermediate
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

for item in sorted(prices):
    print(f"{item.capitalize()}: ${prices[item]}")
for price in sorted(prices, key=prices.get):
    print(f"{price.capitalize()}: ${prices[price]}")
print(max(prices.items()))
#3.1 advanced
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}
temp_list = list(temps.values())
average= sum(temp_list) / len(temp_list)
print(f"The average temp for the weekdays is {average:.1f}")

coldest_day=100
warmest_day=0
above_average=0
for temp in sorted(temps, key=temps.get):
    if temps[temp] < coldest_day:
        coldest_day = temps[temp]
    if temps[temp] > warmest_day:
        warmest_day = temps[temp]

for temp in sorted(temps, key=temps.get):
    if temps[temp] > average:
        above_average += 1
print(f"The coldest day was {list(temps.keys())[list(temps.values()).index(coldest_day)]} with a temperature of: {coldest_day}")
print(f"The warmest day was {list(temps.keys())[list(temps.values()).index(warmest_day)]} with a temperature of: {warmest_day}")        
print(f"The number of days with above average temperature was: {above_average}")

#3.2
#beginner & intermediate
products = {
"laptop": {"price": 999, "stock": 15},
"phone": {"price": 699, "stock": 50}
}
for key, value in products.items():
    if key== "laptop":
        print(f"{key}: {value}")

products["tablet"] = {"price": 449, "stock": 30}
for key, value in list(products.items()):
    if value["stock"] < 20:
        del products[key]
        print(products)
 
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
locations= {}
for country, capital in zip(countries, capitals):
    locations[country] = capital

#advanced
company = {
"Engineering": {"Alice": 95000, "Bob": 85000},
"Marketing": {"Carol": 75000, "Dave": 70000}
}
all_employees = {}
average_salary = {}
for department, info in company.items():
    for name, salary in info.items():
        all_employees[name] = salary
        if department == "Engineering":
            average_salary["Engineering"] = sum(info.values()) / len(info)
        if department == "Marketing":
            average_salary["Marketing"] = sum(info.values()) / len(info)

highest_paid = max(all_employees, key=all_employees.get)
print(all_employees)
for department, avg_salary in average_salary.items():
    print(f"Average salary in {department}: ${int(avg_salary)}")
print(f"Highest paid employee: {highest_paid}")

#3.3
#beginner
cubes = {x: x**3 for x in range(1,6)}
print(cubes)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}
celsius = {day: (temp-32)* 5/9 for day, temp in temps.items()}
print(celsius)
#intermediate
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
passing = {name: grade for name, grade in scores.items() if grade >= 70}

def to_letter(s):
    if s >= 90: return "A"
    if s >= 80: return "B"
    if s >= 70: return "C"
    if s >= 60: return "D"
    return "F"
    
scores_in_letters = {n: to_letter(g) for n, g in scores.items()}
print(scores_in_letters)

student_ids = {"Alice": 101, "Bob": 102}
by_id = {v: k for k, v in student_ids.items()}
print(by_id)
#advanced
sales = [
("North", "Alice", 5000), ("South", "Bob", 4500),
("North", "Carol", 6000), ("South", "Alice", 3500)
]
total_sales= {}
by_salesperson = {}
by_region = {}
for region, name, amount in sales:
    total_sales[region] = total_sales.get(region, 0) + amount
    
    if name not in by_salesperson:
        by_salesperson[name] = []
    by_salesperson[name].append((region, amount))

    if region not in by_region:
        by_region[region] = []
    by_region[region].append((name, amount))

print(total_sales)
print(by_salesperson)
print(by_region)

# SET Unit 1
#beginner
vowels = {"a", "e", "i", "o", "u"}
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
compact_numbers = set(numbers)

empty = {}
#it is a dictionary, not a set
#the proper way to build an empty set is:
empty = set()

#intermediate
text = "mississippi"
unique_letters = set(text)      
#there are 4 unique letters

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = set(emails) 
smaller_emails = list(unique_emails)

#Why does this fail? s = {[1, 2], [3, 4]}
#because a set can not contain a list, let alone two. lists are mutable and sets only contain immutable elements

#advanced
import timeit

list_time = timeit.timeit("999999 in list(range(1000000))", number=1000)
set_time = timeit.timeit("999999 in set(range(1000000))", number=1000)
print(f"List time: {list_time}")
print(f"Set time: {set_time}")

frozen = frozenset([1, 2, 3])
graph = {frozen: [(1, 2), (2, 3)]}
print(f"Graph with frozenset key: {graph}")

edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
unique_edges = set(edges)
print(f"Unique edges: {unique_edges}")

#unit 2
#beginner
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
all = a | b
both = a & b
diff = a - b
print(all, both, diff, sep="\n")

#intermediate
morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

all_employees = morning_shift | evening_shift | weekend_shift
any_shift = morning_shift & evening_shift & weekend_shift
morning_only = morning_shift - evening_shift - weekend_shift
one_shift = (morning_shift ^ evening_shift ^ weekend_shift)

#unit 2
#advanced
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}
eligible_students = prereqs_met & has_space & paid_tuition
unpaid_prereqs = prereqs_met - paid_tuition
unmet_prereqs_and_unpaid = (prereqs_met - paid_tuition) & (paid_tuition - prereqs_met)

#unit 3
#beginner
numbers = {1, 2, 3}
numbers.add(4)
numbers.discard(4)
#numbers.remove(5) 
#raises a KeyError because 5 is not in the set

evens = {x for x in range(20) if x % 2 == 0}
print(evens)

