options = ["New Game", "Load Game", "Settings", "Quit"]
for index, option in enumerate(options, 1):
    print(f"{index}. {option}")
option_number= int(input("Select an option: "))
if option_number not in range(1, len(options)+1):
    print("Wrong Choice")
    option_number= input("Select an a option ")
else:
    if option_number in range(len(options)+1):
        for i in str(options):
            selection = str(option_number)
            print(f"Option selected {i}")