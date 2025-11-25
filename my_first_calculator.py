def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide (n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    first_number = float(input("Enter first number: \n"))
    pick_operation = input("Enter operation ('+','-','*','/'): \n")
    second_number = float(input("Enter second number: \n"))

    result = operations[pick_operation](first_number,second_number)


    while input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation.\n") == "y":
        first_number = result
        pick_operation = input("Enter operation ('+','-','*','/'): \n")
        second_number = float(input("Enter second number: \n"))

        result = operations[pick_operation](first_number, second_number)







