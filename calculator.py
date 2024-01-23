import math
import re

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def exponentiate(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def modulus(x, y):
    return x % y

def calculate_percentage(x, percentage):
    return (percentage / 100) * x

def parse_input(user_input):
    try:
        return float(user_input)
    except ValueError:
        return user_input.lower()

def calculator():
    print("Advanced Calculator")
    print("Type 'exit' to end the calculator.")

    while True:
        user_input = input("Enter expression: ")

        if user_input.lower() == 'exit':
            break

        # Split the input into individual components (numbers and operators)
        components = re.findall(r"[-+]?\d*\.\d+|\d+|[-+*/%\(\)\[\]\{\}]", user_input)

        # Initialize variables
        result = None
        numbers = []
        operators = []

        for component in components:
            parsed_component = parse_input(component)

            if isinstance(parsed_component, float):
                numbers.append(parsed_component)
            elif parsed_component in ('+', '-', '*', '/', '**', 'sqrt', '%', '(', ')', '[', ']', '{', '}'):
                operators.append(parsed_component)

        # Evaluate the expression with multiple operators
        i = 0
        while i < len(operators):
            operator = operators[i]

            if operator == '%':
                if i < len(numbers) - 1:
                    percentage_of = numbers.pop(i + 1)
                    base_number = numbers.pop(i)
                    result = calculate_percentage(base_number, percentage_of)
                    numbers.insert(i, result)
                    operators.pop(i)
                else:
                    print("Invalid input. Percentage operator should be used with a preceding number.")
                    break
            else:
                i += 1

        expression = ''
        for i in range(len(numbers)):
            expression += str(numbers[i])
            if i < len(operators):
                expression += operators[i]

        try:
            result = eval(expression)
            print(f"Result: {result}")
        except (SyntaxError, ZeroDivisionError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
