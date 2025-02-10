# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2],
# such that they add up to a given target number target and index1 < index2.
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
from typing import List


class Solution:
    def two_sum(self, numbers: List[int],  target:int)->List[int]:
        left, right =  0, len(numbers) -1

        while left < right:
            current_sum= numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left +=1
            else:
                return [left+1, right+1]

        return []

# current_sum is calculated by adding the numbers at the left and right indices.

# first if statement means the sum is too large,
# so the right pointer (r) is decremented to try a smaller number.

# second elif statement means the sum is too small, so the left pointer (left)
# is incremented to try a larger number.

# else solution is found, and the function returns
# the 1-based indices of the two numbers (left + 1 and right + 1).