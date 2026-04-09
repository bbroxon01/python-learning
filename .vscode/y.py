#exercises 1 by 1
taken = ["admin", "root", "user", "test"]
errors = []
under_score = "_"
user_name = input("Enter a username ")
if not user_name.strip(" "):
    errors.append("Username cannot be empty")
elif not 4 <= len(user_name) <= 16:
    errors.append("Username must be 4-16 characters")
elif not user_name[0].isalpha():
    errors.append("Username must begin with a letter")
elif not user_name.isalnum() and not under_score in user_name:
    errors.append(f"Username must only contain:\nLetters, numbers, and underscores")
elif user_name in taken:
    errors.append("Invalid username")
else:
    print("Valid username")
if not errors == []:
    print(errors)