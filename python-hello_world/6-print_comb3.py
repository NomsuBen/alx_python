for tens_digit in range(1, 10):
    for units_digit in range(0, tens_digit):
        print("{:02d}".format(units_digit * 10 + tens_digit), end=", " if tens_digit > 2 else "\n")