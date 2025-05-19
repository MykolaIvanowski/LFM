# given array, find subarray that has the largest product
# it is only for contiguous subarray
#
# Input: nums = [1,2,-3,4]
# Output: 4
#
# Input: nums = [-2,-1]
# Output: 2
#
from typing import List

# Kadane's Algorithm
class Solution:
    def subarray(self, nums:List[int])->int:
        result = nums[0]                    # first element possibly can be the largest subarray
        current_min, current_max = 1,1      # track minimum/maximum for sub array
        # why track minimum: because array can have negative numbers and if we multiplying negative numbers
        # it can turn into large positive number, so in case not miss it we track minimum

        # example: Input: nums = [-1, -3, -10, 0, 60]
        # Without tracking current_min, we might miss the fact that -3 × -10 = 30,
        # which could contribute to the final max product

        # run loop for every number in array
        for num in nums:
            # we use temporary variable, because want to use unmodified current_max on this step
            # in calculating current_min (it is effect in case negative numbers)
            tmp = current_max * num

            # current_max is product previous subarray numbers multiply with current number, or current number
            # or current number multiply with current_min
            current_max = max(num * current_max, num* current_min,num)
            # current_min is current number or previous current max multiply on current number or
            # current number multiply on current_min
            current_min = min(tmp, num * current_min, num)

            # chose best result
            result = (result,current_max)
        return result

obj = Solution()
print(obj.subarray([1,4,6,3,-3,-6]))
