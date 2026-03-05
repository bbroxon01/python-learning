# Coding Problem 1: Temperature Converter
temp = float(input("Enter temperature: "))
scale = input("Enter scale (C/F): ")
print("Entered temperature:", temp)
print("Entered scale:", scale)
if scale == "f" or scale == "F":
    celsius = (temp - 32) * 5 / 9
    print(f"{temp:.1f}°F = {celsius:.1f}°C")
elif scale == "c" or scale == "C":
    fahrenheit = (temp * 9 / 5) + 32
    print(f"{temp:.1f}°C = {fahrenheit:.1f}°F")
else:    
    print("Invalid scale. Please enter C or F.")
    
# Coding Problem 4:
    