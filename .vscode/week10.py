#week 10 exercises
#Unit 1
#exercise 1

colors = ["red", "blue"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(color, size)

#exercise 2
#print all the numbers from 1 to 16 in a 4x4 grid
#THINK ABOUT ROWS AND COLUMNS
rows = 4
columns = 4
counter = 0
for i in range(4):
    for j in range(4):
        counter += 1
        print(f"{counter}", end=" ")
    print()
    
#exercise 3
numbers = [2, 7, 3, 8, 5]
pair = 10
group = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == pair:
            print(f"{numbers[i]} + {numbers[j]} = 10")
print()
#unit 2
#Exercise 1
scores = [85, 92, 78, 95, 88]
total = 0
count = 0
for score in scores:
    total += score
    count += 1
average = total / count
print(f"The average score is: {average}")

#exercise 2
text = "Hello World 2026!"
uppercase_only = ""
for char in text:
    if char.isupper():
        uppercase_only += char
print(uppercase_only)

#exercise 3
numbers = [2, 3, 4, 5, 6]
even_sum = 0
odd_product = 1
for digit in numbers:
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_product *= digit
print(even_sum, odd_product)   

#unit 3
#exercise 1
data = [45, 67, 23, 89, 51, 44, 78]
count = 0
for big_number in data:
     if big_number > 50:
         count += 1
print(count)
#exercise 2
prices = [5.99, 12.50, 3.25, 0, 9.99]
total = 0
item_count = 0
for price in prices:
    if price == 0:
        break
    if price != 0:
        total += price
        item_count +=1
print(f"Items: {item_count}, Total: ${total:.2f}")
#exercise 3
# given a list of words, find
#1 the total number of characters across all words (accumulator)
#2 how many words have more than 4 characters (counter)
#3 stop processing if you encounter the word "stop" (sentinel)
words = ["cat", "elephant", "dog", "python", "STOP", "rhinoceros", "bat"]
total_chars = 0
long_count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == pair:
            print(f"{numbers[i]} + {numbers[j]} = 10")

for word in words:
    if word:
        total_chars += len(word)
    if word == "STOP":
        break
    if total_chars > 4:
        long_count += 1
print(f"Total characters: {total_chars}")
print(f"Words longer than 4 chars: {long_count}")