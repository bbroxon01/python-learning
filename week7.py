list_a = [1, 2, 3]
list_b = list_a
list_b[0] = 99
print(list_a)  # Output: [99, 2, 3]

# unit 1 beginner exercise
colors = ["red", "green", "blue"]
numbers = [10, 20, 30]
print(f'Colors: {colors}')
print(f'Numbers: {numbers}\n Colors: {colors}')

# unit 1 intermediate exercise
list_temp = [72, 75, 78]
list_temp[0] = 70
print(list_temp)  # Output: [70, 75, 78]

word = "Hello"
#word[0] = "J"  # This will raise an error because strings are immutable

# unit 1 advanced exercise
original = [10, 20, 30]
alias = original
alias[1] = 200
print(original)  # Output: [10, 200, 30]
#make an independent copy of the list

# unit 2 beginner exercise
#create a list called animals with: "cat", "dog", "bird", "fish", and "hamster"

animals = ["cat", "dog", "bird", "fish", "hamster"]
print(animals[0]) #cat
print(animals[-1]) #hamster
print(len(animals)) #5

# unit 2 intermediate exercise
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
months[1] = "February"
middle_index = len(months) // 2
print(len(months)) #6
print(months[middle_index]) #Apr
print(months[-1]) #Jun
print(len(months)-1) #5

# unit 2 advanced exercise
data = [100, 200, 300]
empty = []
if not empty:
    print(data[0])  # Output: 100
else:
    print("The list is empty")
data[0], data[-1] = data[-1], data[0]
print(data)

# unit 3 beginner exercise
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#print first three numbers
#print last three numbers
#print middle three numbers
#create a complete copy of list
print(numbers[:3])
print(numbers[-3:])
middle_index = len(numbers) // 2
print(numbers[middle_index-1:middle_index+2])
print(numbers[:])

# unit 3 intermediate exercise
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#use slicing to:
#1. get every other letter starting from "a"
#2. get every other letter starting from "b"
#3. reverse the list
#4. get every third letter starting from reversed list
print(alphabet[::2])  # Output: ['a', 'c', 'e', 'g', 'i']
print(alphabet[1::2])  # Output: ['b', 'd', 'f', 'h', 'j']
print(alphabet[::-1])  # Output: ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
print(alphabet[::-3])  # Output: ['j', 'g', 'd', 'a']

# unit 3 advanced exercise
course = "CS1300"
course = list(course)
course[3], course[4] = course[4], course[3]
course = "".join(course)
print(course)

csv_row = "Alice,92,88,95"
csv_row = list(csv_row.split(","))
print(csv_row[0])
print(csv_row[1:])

normal_list = [1, 2, 3, 4, 5]
reversed_list = normal_list[::-1]
print(normal_list) # Output: [1, 2, 3, 4, 5]
print(reversed_list) # Output: [5, 4, 3, 2, 1]

#Lecture 2

#Unit 1 Exercises 
# Exercise 1
groceries = []
groceries.append("Milk")
print(groceries)
groceries.append("Eggs")
print(groceries)
groceries.append("Bread")
print(groceries)

# Exercise 2
numbers = [10, 30, 40]
numbers.insert(1, 20) 
numbers.insert(0, 5)
numbers.append(50)
numbers.extend([60, 70, 80])
print(numbers)

# Exercise 3
a = [1,2]
a.append([3,4])
print(a)

b = [1,2]
b.extend([3,4])
print(b)

c = [1,2]
c.append("hi")
print(c)
d = [1,2]
d.extend("hi")
print(d)

# Unit 2 exercises
# Exercise 1
animals = ["cat", "dog", "bird", "dog", "fish"]
animals.remove("bird")
print(animals)
last = animals.pop()
print(last)
print(animals)
del animals[0]
print(animals)

# Exercise 2
queue = ["Alice", "Bob", "Charlie", "David", "Eve"]
queue.remove("David")
served = queue.pop(0)
print(f"{served} was served.")
left = queue.pop()
print(left)
print(queue)

# Exercise 3
score = 100
scores = [85, 92, 78, 64, 95, 88]
if score in scores:
    scores.remove(score)
else: 
    print(f"{score} not found.")

index = 10
if index < len(scores):
    scores.pop(index)
else:
    print(f"{index} out of range.")
    
del scores[len(scores) // 2 - 1: len(scores) // 2 + 1]
print(scores)

# Unit 3 exercises
# Exercise 1
colors = ["red", "blue", "green", "yellow", "blue"]
if "blue" in colors:
    print("Blue is in the list.")
else:
    print("Blue is not in the list.")
if "purple" not in colors:
    print("Purple is not in the list.")
else:
    print("Purple is in the list.")

print(f"Index of green: {colors.index('green')}")
print(f"Blue occurs {colors.count('blue')} times")

# Exercise 2
students = ["Alice", "Bob", "Charlie", "David", "Alice"]
student_name = input("Enter a student name: ")
if student_name in students:
    print(f"Index of {student_name}: {students.index(student_name)}")
    print(f"{student_name} appears {students.count(student_name)} time.")
else:
    print(f"{student_name} is not enrolled.")

# Exercise 3   
inventory = ["hammer", "nails", "screwdriver", "nails", "wrench", "nails"]
print(f"Nails are in inventory {inventory.count('nails')} times.")
print(f"The first entry of nails is at index: {inventory.index('nails')}")
inventory.remove('nails')
print(f"The first entry of nails is now at index: {inventory.index('nails')}")
inventory.remove('nails')
print(f"Nails are now in inventory {inventory.count('nails')} time.")
print(inventory)