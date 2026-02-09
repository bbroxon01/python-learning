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
text = "hello world, welcome to PYTHON"
# Convert to uppercase
upper_text = text.upper()
print(upper_text)  # "HELLO WORLD, WELCOME TO PYTHON"
# Convert to lowercase
lower_text = text.lower()
print(lower_text)  # "hello world, welcome to python"
# Convert to title case
title_text = text.title()
print(title_text)  # "Hello World, Welcome To Python"

#3.2
sentence = input("Enter a sentence: ")
length = len(sentence)
a_count = sentence.count('a')
hello_sentence = sentence.startswith("Hello")
end_sentence = sentence.endswith(". ! ?")
print(f"Length of the sentence: {length}")
print(f"Number of 'a' characters: {a_count}")
print(f"Sentence starts with Hello: {bool(hello_sentence)}")
print(f"Sentence ends with punctuation: {bool(end_sentence)}")

#3.3
# Messy user input
name = "  JOHN DOE   "
email = "   John.Doe@Email.COM   "
phone = "   (555) 123-4567   "

clean_name = name.strip().title()
clean_email = email.strip().lower()
clean_phone = phone.strip().replace(" ", "").replace("(", "").replace(")", "").replace("-", "")
print(f"Clean Name: {clean_name}")
print(f"Clean Email: {clean_email}")
print(f"Clean Phone: {clean_phone}")

# End of week 4 exercises