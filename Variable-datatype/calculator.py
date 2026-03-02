"""Simple calculator demonstrating variables and basic operations.

Usage: run the script and follow prompts to perform arithmetic on two numbers.
"""

# read two numbers from the user
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
except ValueError:
    print("Please enter valid numeric values.")
    exit(1)

# prompt for operation
op = input("Choose operation (+, -, *, /): ")

result = None
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("Error: division by zero")
        exit(1)
    result = a / b
else:
    print("Unsupported operation")
    exit(1)

print(f"{a} {op} {b} = {result}")
