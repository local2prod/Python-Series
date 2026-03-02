"""basic_functions.py
Simple functions and usage examples.
"""

def greet(name):
    """Return a greeting for `name`."""
    return f"Hello, {name}!"


def add(a, b):
    return a + b


if __name__ == '__main__':
    print(greet('Alice'))
    print('2 + 3 =', add(2, 3))
