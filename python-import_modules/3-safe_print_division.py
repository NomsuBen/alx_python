def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both inputs should be integers!")
        return None
    else:
        print("Inside result: {}".format(result))
        return result
    finally:
        print("Finally: Division operation completed.")

# Test the function
a = 10
b = 2
safe_print_division(a, b)

c = 5
d = 0
safe_print_division(c, d)

e = "invalid"
f = 2
safe_print_division(e, f)
