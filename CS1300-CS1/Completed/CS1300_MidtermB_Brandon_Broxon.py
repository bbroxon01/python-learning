#Coding Problem 1
weight = float(input("Enter your weight in lbs or kgs: "))
unit = input("Enter unit (imperial/metric): ")
height = float(input("Enter your height: "))
if unit == 'imperial':
    BMI = (weight * 703) / (height ** 2)
elif unit == 'metric':
    BMI = (weight / (height ** 2))
else:   
    print("Invalid unit system. Please enter imperial or metric.")

if BMI < 18.5:
    BMI_category = "Underweight"
elif BMI >= 18.5 and BMI < 25:
    BMI_category = "Normal weight"
elif BMI >= 25 and BMI < 30:
    BMI_category = "Overweight"
else:
    BMI_category = "Obese"
    
if unit == 'imperial':
    print(f"Weight: {weight} lbs")
    print(f"Height: {height} inches")
    print(f"BMI: {BMI:.1f}")
    print(f"BMI Category: {BMI_category}")
elif unit == 'metric':
    print(f"Weight: {weight} kgs")
    print(f"Height: {height} meters")
    print(f"BMI: {BMI:.1f}")
    print(f"BMI Category: {BMI_category}")

#Coding Problem 2
password = input("Enter a password: ")
num_uppercase = 0
num_lowercase = 0
num_digits = 0
num_special = 0
    
for c in password:
   if c.isupper():
       num_uppercase += 1 
   elif c.islower():
       num_lowercase += 1
   elif c.isdigit():
        num_digits += 1
   elif not c.isalnum():
        num_special += 1
criteria_met = 0
if len(password) >= 8:
    criteria_met += 1
    print("Length:\tPASS")
else:
    print("Length:\tFAIL")
if num_uppercase > 0:
    criteria_met += 1
    print("Uppercase:\tPASS")
else:
    print("Uppercase:\tFAIL")
if num_lowercase > 0:
    criteria_met += 1
    print("Lowercase:\tPASS")
else:
    print("Lowercase:\tFAIL")
if num_digits > 0:
    criteria_met += 1
    print("Digits:\tPASS")
else:
    print("Digits:\tFAIL")
if num_special > 0:
    criteria_met += 1
    print("Special char:\tPASS")
else:
    print("Special:\tFAIL")
if criteria_met == 5:
    rating = "Strong"
elif criteria_met >= 3:
    rating = "Moderate"
elif criteria_met >= 1:
    rating = "Weak"
else:
    print("No password criteria met.")
print(f"Criteria met: {criteria_met} / 5")
print((f"Strength: {rating}"))

        
#Coding Problem 3
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset"]
quantities = [12, 45, 30, 8, 22]

print("=== Inventory ===")
for i in range(len(products)):
    print(f"{products[i]}:\t{quantities[i]}")
print("=================")

max_index = None
min_index = None
max_quantity = 0
min_quantity = 1000
for index in range(len(quantities)):
    print(index, quantities[index], products[index])
    if quantities[index] > max_quantity:
        max_quantity = quantities[index]
        max_index = index
    
    if quantities[index] < min_quantity:
        min_quantity = quantities[index]
        min_index = index
        
print(f"Highest: {products[max_index]} {quantities[max_index]}")
print(f"Lowest: {products[min_index]} {quantities[min_index]}")
print(f"Total quantity: {sum(quantities)}")
print(f"Average quantity: {sum(quantities) / len(quantities):.2f}")

products.append("Webcam")
quantities.append(15)
products.insert(2, "USB Hub")
quantities.insert(2, 50)
products.remove("Headset")
quantities.remove(22)
removed_product = products.pop(5)
removed_quantity = quantities.pop(5)
print(removed_product, removed_quantity)
print("= Updated Inventory =")
for i in range(len(products)):
    print(f"{products[i]}:\t{quantities[i]}")
print("=================")
