#coding problem 1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name.capitalize() + " " + last_name.capitalize()
birth_year = input("What year were you born? ")
hobby = input("Enter your favorite hobby: ")
age = str(2026 - int(birth_year))
width = 36
print("=" * width)
print("   USER PROFILE CARD   ".center(width))
print("=" * width)
print(f"Name:" + full_name.rjust(width-(len("Name:")*len(fillchar))))
print(f"Age:" + age.rjust(width-(len("Age:")*len(fillchar))))
print(f"Hobby:" + hobby.rjust(width-(len("Hobby:")*len(fillchar))))
print("-" * width)
print("Thank you for creating your profile!")
print("=" * width)

# coding problem 2
sentence = input("Enter a sentence: ")
total_length = len(sentence)
short_length = len(sentence.replace(" ", ""))
word_count = len(sentence.split())
vowel_count = sum(1 for char in sentence.lower() if char in 'aeiou')
upper_sentence = sentence.upper()
lower_sentence = sentence.lower()
reversed_sentence = sentence[::-1]
capital_start = sentence[0].isupper()
punctuation = {sentence.endswith('.', '!', '?')}
print("\n" + ("=" * 8) + 'Sentence Analysis'.center(40) + ("=" * 8) + "\n")
print(f"Entered Sentence: {sentence.rjust(40)}" + "\n")
print("----- Analysis Results -----".center(40))
print(f"Sentence Length (with spaces): {str(total_length).rjust(40)}")
print(f"Sentence Length (without spaces): {str(short_length).rjust(40)}") 
print(f"Word Count: {str(word_count).rjust(40)}")
print(f"Vowel Count: {str(vowel_count).rjust(40)}")
print(f"Uppercase: {upper_sentence.rjust(40)}")
print(f"Lowercase: {lower_sentence.rjust(40)}")
print(f"Reversed: {reversed_sentence.rjust(40)}")
print(f"Starts with capital letter: {str(capital_start).rjust(40, fillchar=' ')}")
print(f"Ends with punctuation: {str(punctuation).rjust(40, fillchar=' ')}")


