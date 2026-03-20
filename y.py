#Coding problem 3
#create menu
coffee = float(3.50)
sandwich = float(6.00)
salad = float(5.50)
combo = float(8.00)
width = 30
menu = f"{"=" * 30}\n{("CAMPUS CAFE").center(30)}\n{"=" * 30}\n{("1. Coffee") + (f"${coffee:.2f}").rjust(width - len("1. Coffee"))}\n{("2. Sandwich") + (f"${sandwich:.2f}").rjust(width - len("2. Sandwich"))}\n{("3. Salad") + (f"${salad:.2f}").rjust(width - len("3. Salad"))}\n{("4. Combo") + (f"${combo:.2f}").rjust(width - len("4. Combo"))}\n{("5. Exit")}\n{"=" * 30}"
print(menu)
name = str(input("Enter your name: "))
for char in name:
    if  char.isalnum: