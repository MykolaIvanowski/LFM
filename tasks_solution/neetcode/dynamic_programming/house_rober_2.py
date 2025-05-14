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
        # one element  return this element
        if len(nums)== 1:
            return nums[0]

        price_flag = [[-1]* 2 for _ in range(len(nums))]
        def dfs(i, flag):
            # reach the end of depth,
            # if flag is true the first house is robbed and last is not robbed
            # if flag is false the first  house is not robed and last is can be robbed
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0
            # not visited skip if visited return visited element
            # False == 0, True == 1, help return firs or second element in matrix
            if price_flag[i][flag]!= -1:
                return price_flag[i][flag]
            # calculate which cell is bettor to
            # flag or (i==0) if house 0 robbed update flag to true, if flag alredy true last house an not be robbed
            price_flag[i][flag] = max(dfs(i+1, flag),nums[i]+ dfs(i+ 2, flag or (i==0)))

            return price_flag[i][flag]

        return max(dfs(0,True), dfs(1,False))


o = SolutionTopDown()
print(o.house_robber([2,3,4,5,1]))


class SolutionBottomUp:
    def house_robber(self, nums: List[int])->int:
        if len(nums) == 1: # one element in array
            return nums[0]
        # calculate which is grater with count last or first cell in sequence
        return max(self._dp(nums[1:]), self._dp(nums[:-1]))

    def _dp(self, nums: List[int])-> int:
        if not nums: # empty array
            return 0
        if len(nums) == 1: # need second check for one element in array
            return nums[0] # because we slise the array in call _dp method

        # initialise aray for saving
        house_calculation = [0]* len(nums)
        # use base case for first two element
        house_calculation[0] = nums[0]
        house_calculation[1] = max(nums[0], nums[1])

        # calculate bath path for cell calculation
        for i in range(2, len(nums)):
            house_calculation[i] = max(house_calculation[i-1], house_calculation[i-2] + nums[i])

        return house_calculation[-1]