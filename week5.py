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

ride_access = input("Enter your height in inches: " +"\n" + "Enter your age: " + "\n" + "Do you have adult supervision? (yes/no): ")

if ride_height >= 48 and age >= 8:
    print("You can go on the ride!")
elif ride_height >= 48 and adult_supervision:
    print("You can go on the ride with adult supervision.")
else:  
    print("You are too young for the ride.")