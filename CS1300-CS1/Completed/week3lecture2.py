# Week 3 Lecture 2
#3.1
a = 42 # integer
print(type(a))
b = 42.0 # float
print(type(b))
c = "42" # string
print(type(c))
d = True # boolean
print(type(d))
e = 3 + 4 # expression
print(type(e))
f = 3 / 4 # expression - true division - always float division
print(type(f))
g = 3 // 4 # expression - floor divison - results in integer - rounds towards minus infinity
print(type(g))

# 3.2
first = "Computer"
second = "Science"
full_course = first + " " + second
separator = "-" * 10
length = len(full_course)
print(full_course)
print(separator)
print(length)

# 3.3
# This code has type-related errors. Fix them!
quantity = int(input("How many items? ")) # User enters: 3
price = 9.99
subtotal = quantity * float(price)
tax_rate = (f"{0.07:.2f}")
tax = subtotal * float(tax_rate)
total = subtotal + tax
print("Total: $" + f"{total:.2f}")

#3.4
x = 10
y = 5
name = "Python"
empty = ""
# Predict these:
a = x > y and y > 0 # True
b = x < y or y == 5 # True
c = not (x == 10) # False
d = bool(name) # True
e = bool(empty) # False
f = x == 10 and name == "Python" # True
g = (x + y) > 20 or len(name) == 6 # True

# 3.5
print(10 / 3) # 3.3333333333333335 # true division
print(10 // 3) # 3 # floor division
print(-10 // 3) # -4 (not -3!) # rounds towards minus infinity
print(10 % 3) # 1 # remainder
print(-10 % 3) # 2 because -10 = (-4 * 3) + 2
print(2 ** 10) # 1024 # exponentiation
print(10 ** -2) # 0.01 # exponentiation with negative exponent

#3.6
customer_name = "Alice"
items = 3
price = 12.99
subtotal = items * float(price)
tax_rate = (f"{0.07:.2f}")
tax = subtotal * float(tax_rate)
total = subtotal + tax
print("Total: $" + f"{total:.2f}")
print("======== RECEIPT ========")
print("Customer: " + customer_name)
print("Items: " + str(items) + " x $" + f"{price:.2f}")
print("Subtotal: $" + f"{subtotal:.2f}")
print("Tax (7%): $" +f"{tax:.2f}")
print("Total: $" +f"{total:.2f}")
print("=========================")