def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

a = 1
b = 2
__import__("0-add")
result = add(a, b)
print("{} + {} = {}".format(a, b, result))