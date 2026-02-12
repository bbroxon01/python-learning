#Beginner
x = 15
print(10 <= x <= 20)
print(1 < 2 < 3 < 4)
print(1 < 2 > 3)

#Intermediate
temperature = 75
humidity = 40

if temperature < 90 and humidity < 80:
    print("Pleasant weather")

#advanced
height = input("Enter your height in inches: ")
age = input("Enter your age: ")
supervision = input("Do you have adult supervision? (yes/no): ")
ride_height = int(height)
age = int(age)
adult_supervision = supervision.lower() == 'yes'
ride_requirement = ride_height >= 48 and age >= 8 or (ride_height >= 48 and adult_supervision)
ride_access = bool(ride_requirement or adult_supervision) == True
fun_none = bool(ride_requirement) == False
if ride_access:
    print("You can go on the ride!")
elif adult_supervision:
    print("You can go on the ride with adult supervision.")
else:  
    print("You are too young for the ride.")
    
#week5lecture2 exercises
#unit 1 exercise beginner
#write in order of execution

x = 10 #execution 1 
y = 20 #execution 2
z = x + y #execution 3
print(z) #execution 4

#unit 1 exercise intermediate
step1 = "Mix ingredients"
step2 = "Bake for 30 minutes"
step3 = "Let it cool"
step4 = "Serve and enjoy"
recipe = [step1, step2, step3, step4]
#you would not want to do step 4 before step 3 because the food may be too hot to eat and the ingredients may not have settled properly.

#unit 1 exercise advanced 
#For example, in a game where the player has to navigate through a maze, a GOTO statement could be used to jump back to a previous point in the maze if the player gets lost. However, this can be achieved using a loop and conditional statements without the need for a GOTO statement.
#sketch this situation
player = "Player1"
maze = ["Start", "Path1", "Path2", "Path3", "End"]
current_position = 0
while current_position < len(maze):
    print(f"{player} is at {maze[current_position]}")
    if maze[current_position] == "Path2":
        print("You got lost! Going back to Path1.")
        current_position = 1  # Jump back to Path1
    else:
        current_position += 1  # Move to the next position

#unit 2 exercise beginner
age = 20
if age >= 18:
    print("You are an adult.")
    print("You can vote.")

#unit 2 exercise intermediate
x = 7
if x > 5:
    print("A")
    if x > 10:
        print("B")
        print("C")
        print("D")    
        
#unit 2 exercise advanced
score = 100
if score == 100:
    print("Perfect score!")
    print("Congratulations!")
    if score < 100:
        print("Keep trying!")

#unit 3 exercise beginner
#write if-else statement that checks if a number is even or odd and prints an appropriate message
number = 10
if number % 2 == 0:
    print("The number is even.")
else:    print("The number is odd.")

#unit 3 exercise intermediate
#write an if-elif-else chain that converts numerical grades into letter grades (A, B, C, D, F)
grade = 84
if grade >= 90:
    print("A")
elif grade >= 87 and grade <= 89:
    print("A-")
elif grade >= 83 and grade <= 86:
    print("B+")
elif grade >= 80 and grade <= 82:
    print("B")
else:
    print("C or below")

weight = int(input("Enter the weight of the package in pounds: "))
region = input("Enter the region (domestic/international): ")

if weight <= 2:
    if region == "domestic":
        cost = 5
    else:
        cost = 15
elif weight > 2 and weight <= 10:
    if region == "domestic":
        cost = 10
    else:
        cost = 25
elif weight > 10:
    print("Contact us for a quote.")