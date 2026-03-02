# Week 8 lecture
#Unit 1
# Exercise 1
print("Student 1: Present")
print("Student 2: Present")
print("Student 3: Present")
print("Student 4: Present")
print("Student 5: Present")
# Attendance
# What is the repeated action? Print the name of the student and "Present"
# What varies? The name of the student
# How many times do we need to repeat this action? 5 times

# Exercise 2
# If you count down from 1000 with manual code, it would take a long time to write.
print(5)
print(4)
print(3)
print(2)
print(1)
print("Blastoff!")
#writing a loop removes the need to write out each print statement, and allows us to easily change the starting number if we want to.

# Exercise 3
#print hello 5 times
for i in range(5):
    print("Hello")
#print Hello if user's age is over 18

#read three exam scores, compute the average, and print pass if the average is >= 70, otherwise print "Fail"
#ask the user for numbers until they type -1, then print the sum of all numbers entered

# Unit 2
# Exercise 1
for hello in [1, 2, 3, 4, 5]:
    print("Hello")
    
colors = ["red", "blue", "green"]
for color in colors:
    print(color)

# Exercise 2
for day in ["Mon", "Tue", "Wed"]:
    print(f"{day} is a weekday")
print("Weekend is coming!")
#it prints 1 time

# Exercise 3
for multiplier in [3, 7,2,9,1]:
    print(multiplier * 2)
print()

words = ["cat", "elephant", "dog", "rhinoceros"]
total_chars = 0
for word in words:
    total_chars += len(word)
    print(total_chars)

# Unit 3
# Exercise 1
for number in range(1, 11):
    print(number)

for number in range(0,5):
    print(number)

word = "CODE"
for letter in word:
    print(letter)

# Exercise 2
for number in range(1, 20, 2):
    print(number)

for multiples_of_5 in range(0, 51, 5):
    print(multiples_of_5)

pets = ["dog", "cat", "fish", "hamster"]
for pet in range(len(pets)):
    print(f"{pet + 1}. {pets[pet]}")

# Exercise 3
text = "Hello World"
vowel_count = 0
for letter in text:
    if letter in "aeiouAEIOU":
        vowel_count += 1
print(vowel_count)

for countdown in range(10, 0, -1):
    print(countdown)
print("Blastoff!")

#print a multiplication table for 7
for number in range(1, 11):
    print(f"7 x {number + 1} = {7*number}")
    