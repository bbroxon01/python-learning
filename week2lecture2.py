# What will each line print?
message = "Hello, Python!"
print(message)
print(type(message))
number = 42
print(type(number))

# These lines have errors. Fix them to be valid AND follow PEP 8:
# 1st_name = "Taylor"
first_name = "Taylor"
# user-age = 21
student_age = 21
# class = "Computer Science"
course__name = "Computer Science"
# My Score = 100
my_score = 100

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

# AFTER: Messy code
email = "johnsmith@email.com"
diff_year = 2026 - 2004
adult = diff_year>=18
welcome_message = "Welcome" if adult else "Sorry, too young"
print(welcome_message)

# Answer: "Variables are names or labels that refer to an object, not its contents. A variable x=10 is not a box containing 10, the box represents 10 as a label.