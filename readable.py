def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error" if b == 0 else a / b

while True:
    op = input("\nChoose (+, -, *, /) or q to quit: ")
    if op == 'q':
        print("Goodbye!")
        break

    a = float(input("First number: "))
    b = float(input("Second number: "))

    if op == '+':
        print("Result:", add(a, b))
    elif op == '-':
        print("Result:", subtract(a, b))
    elif op == '*':
        print("Result:", multiply(a, b))
    elif op == '/':
        print("Result:", divide(a, b))
    else:
        print("Invalid choice.")