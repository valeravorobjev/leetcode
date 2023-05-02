# Name: 5. Longest Palindromic Substring
# Number: 5
# Level: medium

# Given a string s, return the longest
# palindromic substring in s.

# Example
# 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example
# 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
#
# 1 <= s.length <= 1000 s consist of only digits and English letters.

def run():
    s = "a"

    sub = __longest_palindrome(s)
    print(sub)


def __longest_palindrome(s: str) -> str:

    size = len(s)
    subs = []
    for i in range(0, size):
        for j in range(0, size):
            p = s[i:j+1]
            r = p[::-1]
            if p == r:
                subs.append(p)

    return max(subs, key=len)
