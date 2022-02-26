"""
All equal
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""

def all_equal(numbers):
    return all([x == y for x, y in zip(numbers, numbers[1:])])

print(all_equal([1, 1, 1]))