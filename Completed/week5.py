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

#unit 2 exercises
#beginner
#print(True or False and False)
#True
#print(not True or True)
#True
#print(5 > 3 and 2 < 1 or 4 == 4)
#True    

#intermediate
#result = (x >= 0 and x <= 100) or (x == -1 and not error)

#advanced
gpa = 3.6
full_time = True
service_hours = 150
if gpa >= 3.7 and full_time or gpa >= 3.5 and full_time and service_hours >= 100:
    print("qualified")
#yes

#unit 3
#beginner
#false and (10 / 0 > 1) - false
#true or (10 / 0 > 1) - true
#true and (5 > 3) - true

#intermediate
my_list = []
#if my_list[0] > 10:
    #print("First element is large")
if len(my_list) > 0 and int(my_list[0]) > 10:
    print("First element is large")
elif int(my_list[0]) <= 10:
    print("First element not large")
else:
    print("Empty list")

#advanced
result1 = "" or "default" or "backup"
#false or true or true - stops after first or true because true or anything never evaluates because it is not necessary
print(result1)
result2 = "hello" and "" and "world"
#the same evaluation as the first result which = false
print(result2)
#prints false because once "True or" is evaluated, it is always true 
result3 = 0 or [] or "found" or None
print(result3)
#end of week 5 lecture 1 exercises

#week 5 lecture 2 exercises

#unit 1
#beginner
#write in order of execution
x = 10 #execution 1 
y = 20 #execution 2
z = x + y #execution 3
print(z) #execution 4

#intermediate
step1 = "Mix ingredients"
step2 = "Bake for 30 minutes"
step3 = "Let it cool"
step4 = "Serve and enjoy"
recipe = [step1, step2, step3, step4]
#you would not want to do step 4 before step 3 because the food may be too hot to eat and the ingredients may not have settled properly.

#advanced 
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

#unit 2 
#beginner
age = 20
if age >= 18:
    print("You are an adult.")
    print("You can vote.")

#intermediate
x = 7
if x > 5:
    print("A")
    if x > 10:
        print("B")
        print("C")
        print("D")    
        
#advanced
score = 100
if score == 100:
    print("Perfect score!")
    print("Congratulations!")
    if score < 100:
        print("Keep trying!")

#unit 3
#beginner
#write if-else statement that checks if a number is even or odd and prints an appropriate message
number = 10
if number % 2 == 0:
    print("The number is even.")
else:    print("The number is odd.")

#intermediate
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

#advanced
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