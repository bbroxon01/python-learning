#1.1
# Given the string text = "Programming", write the code to print:
text = "Programming"
# the first character
print(text[0])  # "P"
# the last character (using negative indexing)
print(text[-1])  # "g"
# the fifth character (index 4)
print(text[4])  # "r"
# the length of the string
print(len(text))  # 11

#1.2
print("*" * 20)
print('*' + 'Welcome' .center(18) + '*')
print('*' * 20)

#1.3
word = 'CAT'
print(f"{word[0]}: index 0, index -3")
print(f"{word[1]}: index 1, index -2")
print(f"{word[2]}: index 2, index -1")

#2.1
text = "Computer Science"
print(text[:8])      # "Computer"
print(text[-7:])     # "Science"
print(text[3:6])     # "put"

#2.2
# Extract first 4 characters
date = "2026-02-05"
# Extract year
year = date[:4]
# Extract month
month = date[6:8]
# Extract day
day = date[-2:]
print(f"Year: {year}, Month: {month}, Day: {day}")

#2.3
#reverse text
text1 = "Python"
reversed1 = text1[::-1]
print(reversed1)  # "nohtyP"
# every other character
text2 = "programming"
every_other = text2[::2]
print(every_other)  # "pormig"
#last 3 characters of Hello World reversed
text3 = "Hello, World!"
last_three_reversed = text3[-3:][::-1]
print(last_three_reversed)  # "!dl"

#3.1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name.upper() + " " + last_name.upper()
birth_year = input("What year were you born? ")
hobby = input("Enter your favorite hobby: ")
age = 2026 - int(birth_year)
print("=" * 25)
print("   USER PROFILE CARD   ")
print("=" * 25)
print(f"Name:\t{full_name}")
print(f"Age:\t{age}")
print(f"Hobby:\t{hobby}")
print("-" * 25)
print("Thank you for creating your profile!")
print("=" * 25)
