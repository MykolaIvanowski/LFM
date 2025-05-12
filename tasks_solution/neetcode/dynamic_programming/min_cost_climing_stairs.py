# give array it represent stair, every value in array represent cast for step
# you can use two types of steps i+1 or i+2  , you can start from index 0 or  index 1
# moving pointer it is a cost declared in each array value
# find less cast way to get reach the end of array (roof)
#
# arr = [2,3,4,5] - move from 0 index to index 1 or 2 (step 1) cost 2
#     move from index 1 to index 2 or 3 cost 3
#
# Input: cost = [1,2,3]
# Output: 2
#
# Input: cost = [1,2,1,2,1,1,1]
# Output: 4
#
#
from typing import List


class SolutionTopDown:
    def min_cost_climbing_stairs(self, cost: List[int])-> int:
        min_cost_result = [-1] * len(cost) # store min result fo specific index, -1 means not counted

        def dfs(i):
            if i >= len(cost): # achieved the end of depth
                return 0
            if min_cost_result[i] != -1: # prevent redundant calculation, so just return stored value
                return min_cost_result[i]
            # calculate result  for path i+1 and pass i+2 and store lowest  to array
            min_cost_result[i] = cost[i] + min(dfs(i+1), dfs(i+2)) # go to every possible variety of tree

            # return current result for future recursive calculation
            return min_cost_result[i]

        # return lowest result stored in result array
        return min(dfs(0), dfs(1))

class SolutionBottomUp:
    def min_cost_climbing_stairs(self, cost: List[int])-> int:
        min_pass = [0] * len(cost+1) # why cost+1, because we will have value 0  under index 0 and 1  (allways)

        for  i in range(2,len(cost+1)):

            # we use i-1 and i-2 because result_memo is always for two elements greater then cost array
            # example:  cost      [ 2, 5, 6, 8]                               i-1      i-2
            #     min_pass  [ 0, 0, 2, 0, 0,] - index[2] calculation -> min((0 + 5), (0 + 2)) set 2
            #
            # calculate both ways for going to the 'roof', lowest possible way to reach the last ladder step
            min_pass[i] = min(min_pass[i-1] + cost[i-1], min_pass[i-2] + cost[i-2])

        # each step in iteration we decided what is smaller i-1 or i-2
        # we use calculation that give result to min_pass the last element always be the lowest pass
        return min_pass[len(cost)]


class SolutionSpaseOptimized:
    def min_cost_climbing_stairs(self, cost:List[int])->int:
        # cost =  [3,7,2,7,9,1]
        # price for step is in current cell for next step
        # price for step in reverse order is previous step for current cell
        # if use space optimisation for normal order  need  use two variables to track calculation

        #run in revers way, with -1 spep (because reverse), and from third value from end
        for i in range(len(cost) - 3, -1,-1):
            # calculate lowest way to reach the ladder, from up to bottom
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])