def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

while True:
    print("\nSelect operation:")
    print(" +  for Addition")
    print(" -  for Subtraction")
    print(" *  for Multiplication")
    print(" /  for Division")
    print(" q  to Quit")
    
    op = input("Operation: ")

    if op == 'q':
        print("Calculator exited.")
        break

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if op == "+":
        print("Result:", add(x, y))
    elif op == "-":
        print("Result:", subtract(x, y))
    elif op == "*":
        print("Result:", multiply(x, y))
    elif op == "/":
        print("Result:", divide(x, y))
    else:
        print("Invalid operation.")