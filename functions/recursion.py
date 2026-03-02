"""recursion.py
Recursive functions: factorial and Fibonacci (simple implementations).
"""

def factorial(n):
    """Return n! for n >= 0. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError('n must be >= 0')
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def fib(n):
    """Return the n-th Fibonacci number (0-based). Uses simple recursion."""
    if n < 0:
        raise ValueError('n must be >= 0')
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print('5! =', factorial(5))
    print('fib(7) =', fib(7))
