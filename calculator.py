# Create a basic calculator
# that can perform addition, subtraction, multiplication, and division.
# The calculator should handle invalid inputs gracefully and provide appropriate error messages.
# The calculator should also allow the user to perform multiple calculations until they choose to exit.
# The calculator should be able to handle floating-point numbers.
# The calculator should be able to handle division by zero gracefully.
# The calculator should be able to handle invalid operations gracefully.
# The calculator should be able to handle invalid inputs gracefully.
# Write unit test cases for the calculator functions in a separate file.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in operations:
            return op
        print("Invalid operation. Please choose from +, -, *, /.")

def main():
    print("Welcome to the basic calculator!")
    while True:
        x = get_number("Enter first number: ")
        op = get_operation()
        y = get_number("Enter second number: ")

        if op == '+':
            result = add(x, y)
        elif op == '-':
            result = subtract(x, y)
        elif op == '*':
            result = multiply(x, y)
        elif op == '/':
            result = divide(x, y)
        else:
            result = "Error: Unknown operation."

        print("Result:", result)

        cont = input("Do you want to perform another calculation? (y/n): ").strip().lower()
        if cont != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()