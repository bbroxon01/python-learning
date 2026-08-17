#Problem 1
for number in range(1,31):
    if number % 3==0 and number % 5==0:
        print("FizzBuzz")
    elif number % 3==0:
        print("Fizz")
    elif number % 5==0:
        print("Buzz")
    else:
        print(number)

#Problem 2
n=6
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end="\t")
    print()
      
#Problem 3
#write a function that returns a new list containing only the first occurance of each element, preserving the original list
def unique_preserve_order(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return print(unique_list)
unique_preserve_order([1, 2, 3, 2, 4, 1, 5])

#Problem 4
def fibonacci(n):
    if n < 0:
        return "Input must be a non-negative integer."
    fibonacci_sequence = [0, 1]
    if n == 0:
        return print("[]")
    elif n == 1:
        return print(fibonacci_sequence[:1])
    elif n == 2:
        return print(fibonacci_sequence)
    elif n > 2:
        for i in range(2, n):
            value = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.extend([value])
        return print(fibonacci_sequence)
fibonacci(1)
fibonacci(2)
fibonacci(7)
fibonacci(10)
fibonacci(0)

#Problem 5
balance = 1000.00
transaction_history = []

while True:
    print("-" * 30)
    print("Bank of Brandon".center(30))
    print("-" * 30)
    print("Main Menu".center(30))
    print("-" * 30)
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show Transaction History")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        print(f"Current Balance: ${balance:.2f}")
        
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"Deposited ${amount:.2f}. New Balance: ${balance:.2f}")
        else:
            print("Deposit amount must be positive.")
            amount = float(input("Enter deposit amount: "))
    
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdrew: ${amount:.2f}")
            print(f"Withdrew ${amount:.2f}. New Balance: ${balance:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to current balance.")
            amount = float(input("Enter withdrawal amount: "))
    
    elif choice == "4":
        if not transaction_history == []:
            print("\nTransaction History:")
            for transaction in transaction_history:
                print(transaction)
        else:
            print("No transactions yet")
            print(f"Balance: ${balance:.2f}")
            break
            
    elif choice == "5":
        print(f"Balance: ${balance:.2f}")
        break
        
    else:
        print("Invalid option. Please choose a number between 1 and 5.")