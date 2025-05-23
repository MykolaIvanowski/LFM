# given an array,
# if you can made a two subset, then sum values ana they are equal
#  sum(subset1) == sum(subset2) , return true another false
#
# Input: nums = [1,2,3,4]
# Output: true
#
# Input: nums = [1,2,3,4,5]
# Output: false
#
from typing import List

# algorithm does not care if nums have odd or even length
class SolutionTopDown:
    def can_partition(self, nums: List[int])-> bool:
        total = sum(nums)

        # we check base case: sum for nums is not even numbers it mean that we can not  find equal sum for subsets
        # so if sum is odd numbers we should return False
        if total %2!=0:
            return False
        # why use target, target help to split nums to two subset
        # target represent max sum for one subset!!!
        target = total//2
        n = len(nums)

        # we use 2d array like [i+1][target+1]
        # i - represent index in nums
        memo = [[-1]* (target+1) for _ in range(n+1)]

        def dfs(i, target):

            if target==0: # valid subset is founded, target is sum for subset we try to achieve
                return True
            # if target < 0 then sum for subset is not what we want
            # if n achieve n it mean that we go through all elements, max depth
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1: # we already calculate this so return result
                return memo[i][target]
            # run dfs for every numer, target subtract with number and in next recursive call check
            # if it achieve target==0
            # - By skipping nums[i], you keep the target unchanged.
            # This path checks if a valid subset can be formed without the current number.
            # Often, the right combination might come entirely from the later elements.
            #
            # - When you include nums[i], you subtract its value from target.
            # This path checks if including the current element helps in forming the subset sum.
            memo[i][target] = (dfs(i+1, target) or dfs(i+ 1,target-nums[i]))
            return memo[i][target]

        return dfs(0,target)

obj = SolutionTopDown()
print(obj.can_partition([2,3,5,7,3,2]))
#
#   dfs(i+1, target) - skip(ignoring) nums[i];    dfs(i+ 1,target-nums[i]) - including nums[i]
#
#   example  nums = [3,7,5], target = 10
#                             dfs(0, 10)
#                           /             \
#           [Skip nums[0]=3]             [Include nums[0]=3]
#                 /                                     \
#           dfs(1, 10)                                dfs(1, 7)
#          /          \                               /         \
# [Skip nums[1]=5]  [Include nums[1]=5]       [Skip nums[1]=5] [Include nums[1]=5]
#          |                   |                      |                   |
#    dfs(2, 10)           dfs(2, 5)             dfs(2, 7)             dfs(2, 2)
#       /     \             /     \               /     \                /     \
# [Skip]   [Include]    [Skip]   [Include]    [Skip]   [Include]     [Skip]   [Include]
#    |          |          |         |          |          |            |         |
# dfs(3,10)  dfs(3,3)  dfs(3,5)  dfs(3,-2)    dfs(3,7)  dfs(3,0)      dfs(3,2)  dfs(3,-5)
#


# 0-1 knapsack problem solution
class SolutionBottomUp:
    def can_partition(self, nums:List[int])-> bool:
        total = sum(nums)
        if total %2!=0: # base case if sum of nums is odd return False,i even the it need to check
            return False

        # turget is the half from sun of nums
        target = total//2
        n = len(nums)
        # 2d array row is index+1, columns is target+1
        dp = [[False]* (target+1) for _ in range(n+1)]

        # filed first column with True value
        # columns or target sum 0 always True
        # because sum zero for subsets is True
        for i in range(n+1):
            dp[i][0] = True

        # rum though every index , go through rows
        for i in range(1, n +1):
            # run for every columns, columns represent numbers from 1 to target+1
            for j in range(1, target+1): # j represent targeted sum for subset
                # if current number from nums is less or equale to sum we trying to check we have option to include
                # it in our subset
                if nums[i-1]<= j:
                    # set up solution from previous or
                    # from previous row and column current target - previous nums value (numa[i-1)
                    # we have two choices ignor or include nums[i-1]
                    dp[i][j] = (
                        dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    )
                else:
                    # set value from previous row
                    dp[i][j] = dp[i-1][j]

        return dp[n][target]

obj = SolutionBottomUp()
print(obj.can_partition([2,3,5,7,3,2]))


class SolutionSpaceOptimized:
    def can_partition(self, nums: List[int])-> bool:
        # sum for nums is even number the is possible solution if odd number no solution
        if sum(nums)%2!=0:
            return False

        target = sum(nums)//2 # sums of subsets can achieve this number
        dp  = [False] * (target+1) # represent weather a subset sum of j can be formed using the numbers processed so far
        next_dp = [False]* (target+1) # temporary array to holds update for next iterations

        dp[0] = True

        # iterate through each number in array
        for i in range(len(nums)):
            # iterate though each value fro 1 till targeted sum (target+1)
            for j in range(1, target+1):

                # can we include number under index from muns
                # for that it should be less or equal to current targeted sum
                if j  >= nums[i]:
                    # include or ignore current number
                    next_dp[j] =  dp[j] or dp[j-nums[i]]
                else:
                    # current nums[i] can not be included
                    # so carry forward previous value
                    next_dp[j] = dp[i]

            #- Instead of maintaining a full 2D table, we swap dp with nextDp,
            # keeping only the latest computations.
            dp, next_dp = next_dp, dp

        return dp[target]