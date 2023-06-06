# Palindrome Number
# Level: Easy
import math


# Given an integer x, return true if x is a
# palindrome, and false otherwise.

def run():
    r = __polindrome_number(1)
    print(r)


def __polindrome_number(number: int) -> bool:
    if number == 0 or (0 < number < 10):
        return True
    elif number < 0 or number == 10:
        return False
    digs = math.ceil(math.log(abs(number), 10))

    r = 0
    for i in range(0, digs):
        r += (number % math.pow(10, i + 1) // math.pow(10, i)) * math.pow(10, digs - i - 1)

    if r == number or number == 0:
        return True

    return False
