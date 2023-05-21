# Zigzag Conversion

#  6. Zigzag Conversion
# Level: medium

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

def run():
    result = __convert('AYPALISHIRING', 4)
    print(result)


def __convert(s: str, num_rows: int) -> str:
    if num_rows == 1:
        return s

    rows = [""] * num_rows
    index = 1
    going_up = True

    for ch in s:
        rows[index - 1] += ch
        if index == num_rows:
            going_up = False
        elif index == 1:
            going_up = True

        if going_up:
            index += 1
        else:
            index -= 1

    return "".join(rows)
