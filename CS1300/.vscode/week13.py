#beginning of week 13 lecture 1
#no unit 1 exercises
#unit 2 exercises

#beginner
grades = [78, 92, 85, 91, 88]
reversed_grades = sorted(grades, reverse=True)
for index, grade in enumerate(reversed_grades, 1):
    print(f"{index}. {grade}")

#intermediate


#advanced
products = ["Apple", "Banana", "Orange"]
prices = [0.50, 0.30, 0.60]
quantities = [10, 15, 8]
for product, price, quantity in zip(products, prices, quantities):
    print(f"{product}: ${price * quantity} ({quantity} * ${price})")
#unit 3

#beginner
value1 = 42
value2 = "42"
is_int = isinstance(value1, int)
print(f"value1 is integer: {is_int}")

value2_type = type(value2)
print(f"value2 type: {value2_type.strip()}")

#intermediate
inputs = [5, 10, 15, 20]
all_positive = [input >0 for input in inputs]
print(all(all_positive))
any_large = [input for input in inputs if input >15]
print(any_large)
print(f"Any >15 {any_large}")