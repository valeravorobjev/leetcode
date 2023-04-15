from typing import List

# Number: 946
# Level: medium

# Given two integer arrays pushed and popped each
# with distinct values, return true if this could
# have been the result of a sequence of push and
# pop operations on an initially empty stack, or false otherwise.

# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

[1, 2, 3, 4, 5, 6]
[3, 4, 6, 5, 2, 1]


# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

# Constraints:
#
# 1 <= pushed.length <= 1000
# 0 <= pushed[i] <= 1000
# All the elements of pushed are unique.
# popped.length == pushed.length
# popped is a permutation of pushed.

def __validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
    stack = []

    popped.reverse()

    for pu in pushed:
        stack.append(pu)

        while stack and popped and stack[-1] == popped[-1]:
            stack.pop()
            popped.pop()

    r = not stack and not popped
    return r


def run():
    result = __validate_stack_sequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
    print(f'Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1] result = {result}')

    result = __validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2])
    print(f'Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2] result = {result}')
