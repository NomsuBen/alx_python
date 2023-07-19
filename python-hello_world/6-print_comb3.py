for tens_digit in range(10):
    for units_digit in range(tens_digit+1, 10):
        print("{:02d}".format(tens_digit * 10 + units_digit), end=", " if tens_digit < 8 else "\n")