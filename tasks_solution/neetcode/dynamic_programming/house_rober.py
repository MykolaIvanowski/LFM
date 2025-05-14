# given array, cell - house, value is gold in the house
# white a solution to find the most highest sum, you can not sum from neighbors cell
##
# Input: nums = [1,1,3,3]
# Output: 4
#
# Input: nums = [2,9,8,3,6]
# Output: 16
#
from typing import List


class SolutionTopDown:
    def house_robber(self, nums: List[int])-> int:
        current_state = [-1] * len(nums) #array for  saving state in current calculation

        def dfs(i):
            # reach the end of array
            if i>= len(nums):
                # we go hire three times
                #
                return 0
            # prevent redundant calculation, and return calculated value
            if current_state[i] != -1:
                return current_state[i]

            # find
            # this idea base on sub task
            # calculation start from end of depth (tree) and on each step try to get max value for possibilities
            # is better leaved the same value or calculate next:
            #
            # input [3,4,5,6,70,1,70,1]
            # [-1,  -1,  -1,  -1,  -1,  -1, -1, 1]     0  or 1     max(dfs(i+1), dfs(i+2 )+ nums[i])
            # [-1,  -1,  -1,  -1,  -1,  -1, 70, 1]     1  or 70
            # [-1,  -1,  -1,  -1,  -1,  70, 70, 1]     70 or 2
            # [-1,  -1,  -1,  -1,  140, 70, 70, 1]     70 or 140
            # [-1,  -1,  -1,  140, 140, 70, 70, 1]    140 or 76
            # [-1,  -1,  145, 140, 140, 70, 70, 1]    140 or 145
            # [-1,  145, 145, 140, 140, 70, 70, 1]    145 or 144
            # [148, 145, 145, 140, 140, 70, 70, 1]    145 or 148

            # why we use dfs(i+1), dfs(i+2 )+ nums[i] not dfs(i+1)+ nums[i], dfs(i+2 )+ nums[i]
            # because we should skip some cells though one cell, and not try find best way through each cell
            # 1. Skip the current house and move to the next one (dfs(i + 1)).
            # 2. Rob the current house and then move to the one after the next (nums[i] + dfs(i + 2))
            current_state[i] = max(dfs(i+1), dfs(i+2 )+ nums[i])

            return current_state[i]

        return dfs(0)

o = SolutionTopDown()
r = o.house_robber([3,4,5,6,70,1,70, 1])
print(r)


class SolutionBottomUp:
    def house_robber(self, nums:List[int])-> int:
        # base case when array not have elements or have only one element
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        best_option = [0] * len(nums)
        # base case first two elements have 0 end max value from first two cells
        best_option[0] = nums[0]
        best_option[1] = max(nums[0], nums[1])

        # run loop from index 2 for array becouse they are initialized
        for i in range(2, len(nums)):
            # calculate  max value based on previous cell or leave it as it is
            # on each step calculation deside calculate it or leave it
            best_option[i] = max(best_option[i-1], nums[i]+ best_option[i-2])

        # return last element
        return best_option[-1]

o = SolutionBottomUp()
r = o.house_robber([3,4,5,6,70,1,40,70, 1])
print(r)


class SolutionSpaceOptimized:
    def house_robber(self, nums: List[int])-> int:
        position1, position2 = 0,0,

        # use tem value to store additional element value
        for n in nums:
            # calculate calculate or leave it depend on what is greater
            # you have three cells (state), cell with index -1, cell with index -2 , cell with index i
            # and compere is better  current + index-2 or index-1, calculation is through one cell, calculated cell
            # on each iteration you can diside what is better, current version or calculation
            temp = max(position1 + n, position2)

            # update position values for next calculation
            position1 = position2
            position2 = temp

        return  position2

o = SolutionSpaceOptimized()
r = o.house_robber([3,4,5,6,70,1,40,70, 1])
print(r)
