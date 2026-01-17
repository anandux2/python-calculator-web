import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def main():
    while True:
        print("\n" + "="*30)
        print("   PREMIUM CLI CALCULATOR   ")
        print("="*30)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Modulus (%)")
        print("7. Exit")
        print("-" * 30)

        choice = input("Choose an operation (1-7): ").strip()

        if choice == '7':
            print("\nExiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            try:
                if choice == '1':
                    result = add(num1, num2)
                    op = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    op = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    op = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    op = "/"
                elif choice == '5':
                    result = power(num1, num2)
                    op = "^"
                elif choice == '6':
                    result = modulus(num1, num2)
                    op = "%"

                print(f"\nResult: {num1} {op} {num2} = {result}")
            except ValueError as e:
                print(f"\nError: {e}")
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}")
        else:
            print("\nInvalid choice! Please select a number between 1 and 7.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
