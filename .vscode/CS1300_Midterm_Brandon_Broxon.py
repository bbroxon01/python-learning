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

# Coding Problem 2
sentence = input("Enter a sentence: ")
total_characters = len(sentence)
print("String Analyzer")
print("Total characters:", total_characters)
uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0
reversed_sentence = sentence[::-1]
for char in sentence:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Number of digits:", digit_count)
print("Number of spaces:", space_count)
print("Reversed sentence:", reversed_sentence)

# Coding Problem 3
numbers = [15, 8, 23, 42, 4, 16, 31, 7, 19, 11]
print("Original list:", numbers)
print(numbers[0] and numbers[-1])
print(numbers[(len(numbers)//2)-2:(len(numbers)//2)+2])
numbers.extend([99])
numbers.insert(0, 0)
numbers.remove(42)
removed_number = numbers.pop()
print("Removed number:", removed_number)
if 23 in numbers:
    print("True")
else:
    print("False")
print(numbers.index(16))
print("Final list:", numbers)
print("Length of final list:", len(numbers))