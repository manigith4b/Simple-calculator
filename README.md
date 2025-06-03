# Simple-calculator
A simple Python calculator built using functions
# Simple Calculator

A simple terminal-based calculator built with Python that supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features
- Add (+), subtract (-), multiply (*), and divide (/)
- Handles division by zero gracefully
- User-friendly terminal interface
- Runs continuously until the user chooses to quit

## How to Run
1. Clone or download this repository.
2. Run the `calculator.py` script using Python 3:
   ```bash

  
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
