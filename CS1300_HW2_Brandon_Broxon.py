#coding problem 1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name.capitalize() + " " + last_name.capitalize()
birth_year = input("What year were you born? ")
hobby = input("Enter your favorite hobby: ")
age = str(2026 - int(birth_year))
width = 36
fillchar =  len(" ")

print("=" * width)
print("   USER PROFILE CARD   ".center(width))
print("=" * width)
print("Name:" , full_name.rjust(width-len("Name:")-1))
print("Age:" , age.rjust(width-len("Age:")-1))
print("Hobby: " , hobby.rjust(width-len("Hobby: ")-1))
print("-" * width)
print("Thank you for creating your profile!")
print("=" * width + "\n")

# coding problem 2
sentence = input("Enter a short sentence: ")
total_length = len(sentence)
short_length = len(sentence.replace(" ", ""))
word_count = len(sentence.split())
vowel_count = sum(1 for char in sentence.lower() if char in 'aeiou')
upper_sentence = sentence.upper()
lower_sentence = sentence.lower()
reversed_sentence = sentence[::-1]
capital_start = sentence[0].isupper()
punctuation = sentence.endswith(('.', '!', '?'))
longer_width = 40

print("\n" + ("=" * longer_width))
print("Sentence Analysis".center(longer_width))
print("-" * longer_width + "\n")
print("Entered Sentence:" , sentence.rjust(longer_width-len("Entered Sentence:")-1))
print("\n" + ("-" * longer_width))
print("\n" + "Analysis Results".center(longer_width))
print("=" * longer_width)
print(f"Sentence Length (with spaces):" , str(total_length).rjust(longer_width-len("Sentence Length (with spaces):")-1))
print(f"Sentence Length (without spaces):" , str(short_length).rjust(longer_width-len("Sentence Length (without spaces):")-1))
print(f"Word Count:" , str(word_count).rjust(longer_width-len("Word Count:")-1))
print(f"Vowel Count:" , str(vowel_count).rjust(longer_width-len("Vowel Count:")-1))
print("Uppercase:" , upper_sentence.rjust(longer_width-len("Uppercase:")-1))
print("Lowercase:" , lower_sentence.rjust(longer_width-len("Lowercase:")-1))
print("Reversed:" , reversed_sentence.rjust(longer_width-len("Reversed:")-1))
print(f"Starts with capital letter:" , str(capital_start).rjust(longer_width-len("Starts with capital letter:")-1))
print(f"Ends with punctuation:" , str(punctuation).rjust(longer_width-len("Ends with punctuation:")-1))
print("=" * longer_width)
#I took extra time on both coding problems 1 and 2 to make the output look nice and organized. I hope it is clear and easy to read.

#coding problem 3 (extra credit)
word = input("Enter a word or phrase: ")
is_palindrome = word.replace(" ", "").lower() == word.replace(" ", "")[::-1].lower()
if is_palindrome:
    print(f"{word} is a palindrome.")
else:    
    print(f"{word} is NOT a palindrome.")
