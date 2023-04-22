from typing import Optional


# Number: 2
# Level: Medium

# You are given two non-empty linked
# lists representing two non-negative integers.
# The digits are stored in reverse order,
# and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain
# any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Constraints:
#
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def run():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    r = __add_two_numbers(l1, l2)

    while r is not None:
        print(r.val)
        r = r.next


def __add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    a1 = []
    a2 = []

    while l1 is not None:
        a1.append(l1.val)
        l1 = l1.next

    while l2 is not None:
        a2.append(l2.val)
        l2 = l2.next

    a1.reverse()
    a2.reverse()

    v1 = int("".join(str(i) for i in a1))
    v2 = int("".join(str(i) for i in a2))

    v3 = str(v1 + v2)

    a3 = [int(x) for x in v3]

    r = None
    for v in a3:
        r = ListNode(v, next=r)

    return r

# [9,9,9,9,9,9,9]
# [9,9,9,9]
#
# 8,9,9,9,0,0,0,1
# 8,9,9,9,0,0,0,1
