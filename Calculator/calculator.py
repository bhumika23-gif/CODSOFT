def calculator():
    print("Welcome to the simple calculator!\n")

    while True:
        print("Choose an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Modulus (%)")
        print("6. Exit\n")

        choice = input("Enter your choice (1–6): ")

        if choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please enter a number between 1 and 6.\n")
            continue

        # Take input numbers from the user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")
            continue

        # Perform the selected operation
        if choice == "1":
            result = num1 + num2
            op = "+"
        elif choice == "2":
            result = num1 - num2
            op = "-"
        elif choice == "3":
            result = num1 * num2
            op = "*"
        elif choice == "4":
            if num2 == 0:
                print("Error: Division by zero is not allowed.\n")
                continue
            result = num1 / num2
            op = "/"
        elif choice == "5":
            if num2 == 0:
                print("Error: Modulus by zero is not allowed.\n")
                continue
            result = num1 % num2
            op = "%"

        print(f"\nResult: {num1} {op} {num2} = {result}\n")

if __name__ == "__main__":
    calculator()
