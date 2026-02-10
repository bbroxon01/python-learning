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