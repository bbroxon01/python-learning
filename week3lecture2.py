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
separator = "----------"
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
