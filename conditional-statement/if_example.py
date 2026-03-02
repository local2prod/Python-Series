# Demonstration of conditional statements in Python

try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("That's not an integer.")
    exit(1)

if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

# additional condition
if n % 2 == 0:
    print("even")
else:
    print("odd")
