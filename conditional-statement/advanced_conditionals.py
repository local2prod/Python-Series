# More conditional examples demonstrating logical, membership, and nested tests

value = input("Type something: ")

# membership test
if value in ('yes', 'y', 'Y'):
    print("You agreed!")
elif value in ('no', 'n', 'N'):
    print("You disagreed.")
else:
    print("Unclear response.")

# nested conditionals
try:
    number = int(input("Enter a number between 1 and 100: "))
except ValueError:
    print("That's not a number.")
    number = None

if number is not None:
    if 1 <= number <= 100:
        print("Good range")
        if number % 10 == 0:
            print("It's a multiple of 10")
    else:
        print("Number out of range")

# identity test
x = []
y = []
if x is y:
    print("x and y refer to the same object")
else:
    print("x and y are different objects (even if equal)")

# logical combination
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
