# Conditional Statements

Conditionals allow your program to execute different code paths depending on
boolean expressions. Python supports `if`, `elif`, and `else` clauses.

## Syntax

```python
if condition:
    # executed when condition evaluates to True
    do_something()
elif other_condition:
    # executed when first condition was False but this one is True
    do_something_else()
else:
    # executed when all previous conditions are False
    fallback()
```

- The `elif` and `else` blocks are optional.
- Conditions are any expressions that evaluate to `True` or `False`.
- Python uses indentation to delimit blocks; there are no braces.

## Boolean Expressions

Common operators:

- comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- membership: `in`, `not in`
- identity: `is`, `is not`
- logical: `and`, `or`, `not`

Example: `if x > 0 and x < 10:`

## Example Code

The following script prompts the user for a number and reports whether it's
positive, negative, or zero; it also checks whether the value is even or odd.

```python
# conditional-statement/if_example.py

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
```
