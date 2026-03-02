"""defaults_and_kwargs.py
Demonstrates default parameters, *args, and **kwargs.
"""

def power(base, exponent=2):
    """Return base ** exponent. Default exponent is 2."""
    return base ** exponent


def summarize(*args):
    """Return a list of provided positional arguments."""
    return list(args)


def describe(**kwargs):
    """Return the keyword args as a dict."""
    return kwargs


if __name__ == '__main__':
    print('power(3)=', power(3))
    print('power(2,3)=', power(2, 3))
    print('summarize ->', summarize(1, 2, 3))
    print('describe ->', describe(name='Bob', age=30))
