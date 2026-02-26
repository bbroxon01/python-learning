# Coding Problem 1
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
comparison = a < b < c
de_morgan = not (a > b or a > c)
equivalent_de_morgan = a <= b and a <= c
width = 24

print("a < b < c", ": ".rjust(width-len("a < b < c:")) + str(comparison))
print("not (a > b or a > c)", ": ".rjust(width-len("not (a > b or a > c):")) + str(de_morgan))
print("a <= b and a <= c", ": ".rjust(width-len("a <= b and a <= c:")) + str(equivalent_de_morgan) + "\n")
if de_morgan == equivalent_de_morgan:
    print("De Morgan's Law confirmed: Expressions 2 and 3 match!")

# Coding Problem 2
temp = int(input("Enter the current temperature in Fahrenheit: "))
is_raining = input("Is it currently raining? (yes/no): ").strip().lower() == "yes"
