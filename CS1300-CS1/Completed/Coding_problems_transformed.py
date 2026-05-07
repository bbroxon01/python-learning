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

word = "education"
for vowel in word:
    if vowel in "aeiou":
        print(f"{vowel}", end=" ")