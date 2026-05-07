#1.1
# What will each line print?
message = "Hello, Python!"
print(message)
print(type(message))
number = 42
print(type(number))

#1.2
# These lines have errors. Fix them to be valid AND follow PEP 8:
# 1st_name = "Taylor"
first_name = "Taylor"
# user-age = 21
student_age = 21
# class = "Computer Science"
course__name = "Computer Science"
# My Score = 100
my_score = 100

#1.3
# Run this code and explain what you observe:
a = 256
b = 256
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")
print(f"Same object? {id(a) == id(b)}")
print()
c = 10000
d = 10000
print(f"c = {c}, id(c) = {id(c)}")
print(f"d = {d}, id(d) = {id(d)}")
print(f"Same object? {id(c) == id(d)}")

#1.4
# AFTER: Messy code
email = "johnsmith@email.com"
diff_year = 2026 - 2004
adult = diff_year>=18
welcome_message = "Welcome" if adult else "Sorry, too young"
print(welcome_message)

# Answer: "Variables are names or labels that refer to an object, not its contents. A variable x=10 is not a box containing 10, the box represents 10 as a label.

#2.1
x = 5
y = 10
# x = object with value 5
# y = object with value 10
y = x
# Now y points to the same object as x
x = 20
# x = object with value 20
# y still points to the object with value 5

#2.2
# Predict the output of each print statement:
a, b, c = 1, 2, 3
print(a, b, c) # 1 2 3
x = y = z = 100
print(x, y, z) # 100 100 100
p, q = q, p = 10, 20
print(p, q) # 20 10

#2.3
a = 1000
b = 1000
c = a

print(id(a)) # e.g., 140703263123888
print(id(b)) # e.g., 140703263123920
print(id(c)) # e.g., 140703263123888

print(a is b)
print(a is c)
print(a == b)
# Explanation: a and b are different objects with the same value, so 'a is b' is False but 'a == b' is True. c points to the same object as a, so 'a is c' is True.
# what is the difference between 'is' and '=='?
# 'is' checks for object identity (same memory location), while '==' checks for value equality.

#2.4
x = "first"
y = "second"
x, y = y, x
print(x, y)

#2.5
x = 10
print(f"Initial: x = {x}, id = {id(x)}")
# x and 10 refer to the same object
x += 5
print(f"After x += 5: x = {x}, id = {id(x)}")
# x and x += 5 create new objects because integers are immutable
x = x + 5
print(f"After x = x + 5: x = {x}, id = {id(x)}")
# x and x = x + 5 create new objects again

#2.6
# Draw a memory diagram (namespace and heap) after each statement:
name = "Python"
print(f"name = {name}, id = {id(name)}")
# value = Python, id = e.g., 140703263124112
language = name
print(f"language = {language}, id = {id(language)}")
# value = Python, id = e.g., 140703263124112
name = "Java"
print(f"name = {name}, id = {id(name)}")
# value = Java, id = e.g., 140703263124144
version = 3
print(f"version = {version}, id = {id(version)}")
# value = 3, id = e.g., 140703263123888
version = version + 1
print(f"version = {version}, id = {id(version)}")
# value = 4, id = e.g., 140703263123920
# Explanation: Strings and integers are immutable, so reassigning them creates new objects in memory.
# End of week2lecture2.py