# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    else:
        return x / y

# Main function
def main():
    print("Welcome to Simple Calculator")
    while True:
        try:
            # Prompt user for input
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Select operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            choice = input("Enter choice (1/2/3/4): ")

            # Perform calculation based on user choice
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except Exception as e:
            print("An error occurred:", str(e))

        # Ask if the user wants to continue or exit
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
