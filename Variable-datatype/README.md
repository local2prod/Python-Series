# Variables and Data Types

Variables in Python are names that store data. Think of a variable as a label attached to a value.

- **No declaration needed.** A variable comes into existence the moment you first assign to it.
- **Dynamically typed.** The same variable can hold values of different types over its lifetime.
- **Case-sensitive.** `name` and `Name` are distinct identifiers.

You can assign values with the `=` operator:

```python
x = 42            # integer
name = "Alice"   # string
pi = 3.14159      # float
x = "now a text" # reassignment to a different type
```

## Common Data Types

| Category      | Types                             | Examples                  |
|---------------|-----------------------------------|---------------------------|
| Text          | `str`                             | `'hello'`, `"world"`    |
| Numeric       | `int`, `float`, `complex`         | `10`, `2.5`, `3+4j`       |
| Sequence      | `list`, `tuple`, `range`          | `[1, 2]`, `(3,4)`, `range(5)` |
| Mapping       | `dict`                            | `{'a': 1}`                |
| Set           | `set`, `frozenset`                | `{1,2}`, `frozenset({3})` |
| Boolean       | `bool`                            | `True`, `False`           |
| Binary        | `bytes`, `bytearray`, `memoryview`| `b'bytes'`                |
| None          | `NoneType`                        | `None`                    |

### Numeric type details

- **`int`** – whole numbers of arbitrary precision (e.g. `42`, `-3`).
- **`float`** – double-precision floating-point numbers used for real values; values include a decimal
  point (`3.14`) or exponential notation (`2e-5`). Floating arithmetic is approximate, so
  `0.1 + 0.2` will not exactly equal `0.3` due to binary representation.
- **`complex`** – numbers with real and imaginary parts, written `a+bj` (e.g. `1+2j`).

## Naming Rules

- Must start with a letter (a–z, A–Z) or underscore (`_`).
- Cannot start with a digit.
- May contain letters, digits and underscores only.
- Cannot be a reserved keyword (`import`, `for`, `if`, etc.).

### Common Naming Conventions

- **camelCase** – first word lower, subsequent words capitalised (`myVariable`).
- **PascalCase** – every word capitalised (`MyClass`).
- **snake_case** – words separated by underscores (`my_function`). This is the PEP 8 recommended style for variables and functions.

## Inspecting and Casting Types

Use `type()` to check the type of a value or variable:

```python
>>> a = 5
>>> type(a)
<class 'int'>
>>> a = "five"
>>> type(a)
<class 'str'>
```

To convert between types (casting):

```python
int('123')     # -> 123
str(3.14)      # -> '3.14'
float('2.0')   # -> 2.0
bool(0)        # -> False
```

> 📝 Casting will raise `ValueError` if the conversion is not possible.

## Strings and Quotes

Python strings may be enclosed in single (`'`) or double (`"`) quotes interchangeably. Triple quotes (`'''` or `"""`) allow multi-line literals:

```python
msg = 'hello'
msg2 = "hello"
poem = """Roses are red
Violets are blue"""
```

## Example: Interactive Exploration

```sh
$ python3       # start REPL
>>> x = 10
>>> type(x)
<class 'int'>
>>> x = x + 5
>>> x
15
>>> quit()
```

## Examples

Several simple example scripts live alongside this README.  A good one to experiment with is `calculator.py`, which prompts for two numbers and an operation using variables for storage and displays the result.  You can run it via:

```bash
python3 calculator.py
```

## Summary

Python’s variable system is simple and flexible, making it ideal for beginners. Use clear names, follow snake_case for readability, and rely on built-in functions like `type()` to understand the data you’re working with.

