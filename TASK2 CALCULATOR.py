def add(p, q):
    return p + q

def subtract(p, q):
    return p - q

def multiply(p, q):
    return p * q

def divide(p, q):
    if q == 0:
         ValueError("Cannot divide by zero.")
    return p / q

def calculator():
    while True:
        print("\nSimpleCalculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))

                if choice == '1':
                    print(add(num1, num2))
                elif choice == '2':
                    print(subtract(num1, num2))
                elif choice == '3':
                    print(multiply(num1, num2))
                elif choice == '4':
                    print(divide(num1, num2))

            except  ValueError:
                print("Invalid input. Please enter valid numbers.")
            except  ZeroDivisionError as e:
                print("Error: {e}")

        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator()
