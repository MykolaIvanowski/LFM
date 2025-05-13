# given array, cell - house, value is gold in the house
# white a solution to find the most highest sum, you can not sum from neighbors cell
# first and last cell are connected as if they create a circle (cycle graph)
# it is mean that you can chose add to calculation only first or last cell
#
# Input: nums = [3,4,3]
# Output: 4
#
# Input: nums = [2,9,8,3,6]
# Output: 15
#
from typing import List

class SolutionSpaseOptimizated:
    def house_robber(self, nums: List[int])-> int:
        # case if nums have only one element
        # and case where we calculate with first element from array but without last element
        # and where we calculate without first element  but with last element
        return max(nums[0], self._dp(nums[:-1]), self._dp(nums[1:]))

    def _dp(self, nums):
        position1, position2 = 0,0


        for n in nums:
            # calculate with cell in have greater values
            # index-2 + n or index-1
            # on each step made decision where greater calculation
            temp = max(position1+n, position2)
            # update calculated values
            position1=position2
            position2=temp


class SolutionTopDown:
    def house_robber(self, nums: List[int])-> int:
        if len(nums)== 1:
            return nums[0]
