import decimal

def pow(a, b):
    decimal_a = decimal.Decimal(str(a))
    decimal_b = decimal.Decimal(str(b))
    result = decimal_a ** decimal_b
    return float(result)
