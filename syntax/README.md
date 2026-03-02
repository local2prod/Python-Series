# Python Syntax

This document collects basic syntax rules and short examples to help a beginner start writing Python code.

## Comments

- A hash sign (`#`) begins a comment; everything after it on the same line is ignored.
- Multiline comments are typically written as consecutive `#` lines or in a
  string literal that isn’t assigned (docstring style). Only `#` comments are
  recognised by the interpreter.

```python
# This is a single-line comment
x = 5  # comment after code
```

## Variables and Assignment

- Python has no variable declaration keyword; assignment creates a variable.
- Variables are dynamically typed; the interpreter infers the type from the value.

```python
count = 10          # integer
name = "Alice"     # string
count = count + 1   # reuse variable with new value
```

## Indentation and Blocks

- Indentation (spaces or tabs) is **significant** and defines block structure.
- The recommended convention is four spaces per level (PEP 8).

```python
if x > 0:
    print("positive")
    x -= 1
else:
    print("non-positive")
```

## Statements and Line Continuation

- A statement typically ends at the newline. Use a backslash (`\`) for explicit
  continuation, or wrap expressions in parentheses/brackets.

```python
total = (a + b + c +
         d + e)
```

## Control Flow

### Conditional (`if`/`elif`/`else`)

```python
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
```

### Loops

- `for` iterates over items of a sequence.
- `while` repeats until a condition becomes false.

```python
for i in range(5):
    print(i)

n = 0
while n < 5:
    print(n)
    n += 1
```

Use `break` and `continue` for loop control.

## Functions

Define functions using `def`. Use docstrings to describe behaviour.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

result = add(2, 3)
```

Functions can have default arguments and keyword-only parameters (using `*`).

## Imports

Bring modules or names into scope using `import` or `from ... import ...`.

```python
import math
from datetime import date
```

## Data Structures

- **Lists**: mutable sequences (`[1, 2, 3]`)
- **Tuples**: immutable sequences (`(1, 2, 3)`)
- **Dictionaries**: key-value mappings (`{'a': 1}`)
- **Sets**: unique, unordered collections (`{1, 2, 3}`)

## Strings

- Single (`'`), double (`"`), and triple quotes for multi-line
- Prefix `r` for raw strings, `f` for f-strings

```python
s = 'hello'
fmsg = f"value is {x}"
```

## Type Conversion / Casting

Python provides built-in functions to convert between basic types. These are
also called *casting* functions. Common ones include:

```python
int('123')      # -> 123
float('3.14')   # -> 3.14
str(10)         # -> '10'
bool(0)         # -> False
list((1,2,3))   # -> [1, 2, 3]

# converting between sequences
tuple([1,2])    # -> (1, 2)
set('abc')      # -> {'a', 'b', 'c'}
```

If a conversion is not possible, a `ValueError` is raised:

```python
int('abc')      # ValueError
```

### Implicit Conversion

In some expressions, Python will implicitly convert types (known as *coercion*):

```python
3 + 4.5     # -> 7.5  (int converted to float)
```

It's best to cast explicitly when mixing types to avoid surprises.

## Exceptions and Error Handling

Use `try`/`except` to catch exceptions.

```python
try:
    value = int(user_input)
except ValueError:
    print("not a number")
```

## Example Script

Below is a small script demonstrating many syntax elements:

```python
# greet the user and count down
name = input("What is your name? ")
print(f"Hello, {name}!")

for i in range(3, 0, -1):
    print(i)

print("Lift off!")
```

## Further Reading

Refer to the official tutorial at https://docs.python.org/3/tutorial/ for
in-depth coverage.

