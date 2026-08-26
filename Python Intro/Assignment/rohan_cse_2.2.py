"""
Assignment: Simple Calculator

Name: Rohan Rahim
Department: CSE
Semester: 2.2

Instructions:
- Complete each function below. Do not change function names or parameters.
- Do not delete the comments — they explain what each part should do.
- Test your program by running this file before submitting.
- Note: 'pass' is a placeholder that does nothing — replace it with your
  own code inside each function.
"""


import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    # TODO: implement this function
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    # TODO: implement this function
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    # TODO: implement this function
    return a*b


def divide(a: float, b: float) -> float:
    """
    Return a divided by b.
    Handle division by zero (b == 0) instead of letting the program crash.
    """
    # TODO: implement this function
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

def main():
    """
    Build a simple calculator here. Follow these steps in order:

    1. Ask the user to enter the first number.
    2. Ask the user to choose an operation: +, -, *, /
    3. Ask the user to enter the second number.
    4. Use if / elif / else to check which operation was chosen.
    5. Call the matching function above (add/subtract/multiply/divide)
       and store the result in a variable.
    6. Print the result using an f-string.

    Bonus (optional): wrap everything in a while loop so the user can
    keep calculating until they type 'quit'.
    """
    # TODO: implement the steps above
    
    print("------------ Basic Calculator ------------\n\n")

    while True:
        op = input("Choose an operation(+, -, *, / or quit): ")

        if op.lower() == "quit":
            print("\nExiting program. Thanks for using....")
            break
        elif op not in ["+", "-", "*", "/"]:
            print("\nPlease enter a valid operation\n")
            continue

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("\nPlease enter valid numerical numbers as input.\n")
            continue

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        else:
            result = divide(a, b)


        if result is not None:
            print(f"The result is: {result}\n")



if __name__ == "__main__":
    # This line runs main() only when this file is executed directly.
    main()
