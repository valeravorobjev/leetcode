# Name: 7. Reverse Integer
# Level: medium

# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit
# integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
#
# Input: x = 123
# Output: 321

# Example 2:
#
# Input: x = -123
# Output: -321

# Example 3:
#
# Input: x = 120
# Output: 21

def run():
    # 1534236469
    # 1463847412
    # -2147483648
    result = __reverse(-123)
    print(result)


def __reverse(x: int) -> int:
    arr = list(str(x))

    m = 1
    if arr[0] == "-":
        arr.pop(0)
        m = -1

    arr.reverse()

    r = int("".join(arr)) * m

    if r <= -2 ** 31 or r >= 2 ** 31 - 1:
        r = 0

    return r
