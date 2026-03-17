#week 9 exercises
#beginner
#scenario 1
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for month in months:
    print(month)
#scenario 2
import random
roll = random.randint(1, 6)
count = 0
while roll != 6:
    print(f"You rolled a {roll}")
    roll = random.randint(1, 6)
    count += 1
print("You rolled a 6!")
print(f"It took you {count} rolls to get a 6.")
   
#scenario 3
square = 1**2
while square < 10:
    print(square)
    square = (square + 1)**2
print("No more squares less than 10!")
#scenario 4
response = (input(""))
while response != "quit":
    response = (input(""))
#intermediate
num= 1
while num <= 5:
    print(num)
    num += 1
print("Done!")

#advanced
#for i in range(5):
#print(i)
i = 0
while i < 5:
    print(i)
    i += 1
#unit 2
#beginner
#1
#score = 0
#while score < 100:
#2
#answer = "no"
#while answer != "yes":

#intermediate
num = 2
while num <= 10:
    print(num)
    num += 2
#the original output would not have printed 10 because the condition did not say <= 10

#advanced
count = 1
num = 1
while num <= 1000:
    print(num)
    num *= 2
    count += 1
print(f"You can double 1 {count} times before you exceed 1000.")

#unit 3
#beginner 1
word = "education"
for vowel in word:
    if vowel in "aeiou":
        print(f"{vowel}", end=" " + "\n")
    
#beginner 2
num = int(input("Enter a number: "))
while num != 0:
    print(num)
    num = int(input("Enter a number: "))
print("Goodbye!")

#intermediate 1
#for i in range(10, -1, -1):
    #print(i)
# i = (10, 0, -1)
# while i == i:
    #print(i)
#using while in this way causes an infinite loop

#intermediate 2
#convert while loop to for loop
#value = 1
#while value < 1000:
#    value *= 2
#    print(value)
for value in range(1, 1000):
    value *= 2
    print(value)
#value is multiplied times 2 and does not stop at 1000

#advanced
running = True
menu = "Menu:\n1. Add\n2. Subtract\n3. Exit"
print(f"{menu}")
while running:
    choice = int(input())
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The sum is: {num1 + num2}\n")
        print(f"{menu}")
        running = True
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"The difference is: {num1 - num2}\n")
        print(f"{menu}")
        running = True
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        print(f"{menu}")
        running = True