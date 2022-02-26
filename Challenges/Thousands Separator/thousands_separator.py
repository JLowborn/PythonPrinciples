"""
Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".
"""

# DIY solution
def format_number(n):
    number = str(n)[::-1]
    number = ",".join(number[i : i + 3] for i in range(0, len(number), 3))
    return number[::-1]


# Smart solution
def format_number(n):
    return "{:,}".format(n)
