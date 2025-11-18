# Calculator Program

def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Return the difference of two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Return the quotient of two numbers."""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print("🧮 Welcome to the Calculator!")

    num1 = float(input("What's the first number?: "))

    should_continue = True

    while should_continue:
        # Show the available operations
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, "
            "or type 'n' to start a new calculation, or 'q' to quit: "
        ).lower()

        if choice == "y":
            num1 = answer
        elif choice == "n":
            calculator()  # restart calculator
            should_continue = False
        else:
            should_continue = False
            print("Goodbye! 👋")


calculator()
