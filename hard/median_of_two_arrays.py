from typing import List


# Number: 4
# Level: Hard
# Name: Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of
# size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).

# Example
# 1:
#
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Explanation: merged
# array = [1, 2, 3] and median is 2.
# Example
# 2:
#
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.50000
# Explanation: merged
# array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
#
# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

def run():
    nums1 = [1,3]
    nums2 = [2]
    median = __find_median_sorted_arrays(nums1, nums2)
    print(median)


def __find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    merge = nums1 + nums2
    merge.sort()

    size = len(merge)

    if size == 1:
        return merge[0]

    if size % 2 > 0:
        median = (size // 2) + 1
        return merge[median-1]

    mid_idx = size // 2
    left = merge[mid_idx - 1]
    right = merge[mid_idx]

    median = (left + right) / 2

    return median
