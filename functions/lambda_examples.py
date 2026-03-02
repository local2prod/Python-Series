"""lambda_examples.py
Showcases lambda functions and their use with `map`, `filter`, and `sorted`.
"""

nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))

pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
# sort by second element
sorted_pairs = sorted(pairs, key=lambda t: t[1])

if __name__ == '__main__':
    print('squares ->', squares)
    print('evens ->', evens)
    print('sorted_pairs ->', sorted_pairs)
