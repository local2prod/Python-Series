"""docstring_example.py
Shows how to write and view docstrings and use `help()`.
"""

def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the product.

    Parameters
    ----------
    a : int
        First factor.
    b : int
        Second factor.

    Returns
    -------
    int
        Product of `a` and `b`.
    """
    return a * b


if __name__ == '__main__':
    print('multiply(3,4)=', multiply(3, 4))
    # show the docstring via help()
    print('\nDocstring for multiply:')
    help(multiply)
