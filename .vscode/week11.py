#week11 exercises
#lecture 1
#unit 1
#beginner
def say_hi():
    print("Hi there!")
say_hi()

#intermediate
#code is repeated twice
def print_my_name():
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    print(first_name, end= " ")
    print(last_name)
print_my_name()

#advanced
#calculated twice
#fix bugs in one place and/or make changes
#runs the same code instead of repeating it each time
#easier to read
def draw_box():
    print("+-----+")
    print("|     |")
    print("+-----+")
draw_box() 
#unit 2
#beginner
def print_star():
    print("*")
print_star()
print_star()
#intermediate
#define a function Compliment() that prints "You are great!"
def compliment():
    print("You are great!")
compliment()
#advanced
#why does this fail?
#say_hello()
#def say_hello():
#   print("Hello!")
#fails because the call is made before the function is defined

#unit 3
#beginner
def add_five(n):
    answer = n + 5
    return answer

result = add_five(10)
print(result)
#intermediate

#advanced

#lecture 2
#unit 1 
#beginner
def add(a,b):
    return a + b
result = add(5,3)
print(result)

def welcome(name="Student"):
    print(f"Welcome, {name}!")

welcome("Brandon")
welcome()

#intermediate
#write a function multiply(x,y,z) that returns the product of 3 numbers, then add a default exponent of 2 to this power function
def multiply(x, y, z):
    print((f"{x}")+"*"+(f"{y}")+(f"{z}"))

#advanced

#unit 2
#beginner

def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(f"x = {x}, y = {y}")

#intermediate

#advanced

