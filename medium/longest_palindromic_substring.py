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
    s = "cccc"

    sub = __longest_palindrome(s)
    print(sub)


def __longest_palindrome(s: str) -> str:
    if len(s) < 2:
        return s

    subs = []

    for i in range(0, len(s)):
        p = s[i]
        for j in range(i + 1, len(s)):
            p = p + s[j]
            r = p[::-1]
            if p == r:
                subs.append(p)

    palindromic = max(subs, key=len)

    return palindromic
