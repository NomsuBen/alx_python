#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print(number)
if number > 0:
    print("if the number is greater than 0: is positive")
elif number == 0:
    print("if the number is 0: is zero")
else:
    print("if the number is less than 0: is negative")
