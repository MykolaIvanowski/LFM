# given array of numbers and int target value.
# find how many uniq sets in sum is equal to target
# each numbers in array can be used multiple times
# #
# Input:  nums = [2,5,6,9]    # as you see one numer can be used many times
#         target = 9
# Output: [[2,2,5],[9]]
##
# Input:  nums = [3,4,5]
#         target = 16
# Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
from typing import List

# how many branches have this solution?
# the number of branches in this solution depends on len(nums) and target
#
# this solution avoid redundant subset because
# index control
class Solution:
    def combination_sum(self, nums: List[int], target: int)-> List[List[int]]:
        res =[]

        def dfs(index, possible_sets, sum_possible_sets):
            if sum_possible_sets == target:
                # copy reference to result array if sets is match to target
                res.append(possible_sets.copy())
                return
                # this if means that we achieve the end of tree
            if index>=len(nums) or sum_possible_sets> target:
                return
            # add numbers, it possible add to result if feet the condition in future calls
            possible_sets.append(nums[index])
            # go to left subtree
            dfs(index, possible_sets, sum_possible_sets + nums[index])

            # when left subtree, (leaf) is finished
            # then we clear last element and go to right subtree (leaf)
            possible_sets.pop()

            # go to right subtree, to check right variety fo subtree we need index+1
            # we go to next number in array for adding it in next recursive call
            dfs(index + 1, possible_sets, sum_possible_sets)

        dfs(0,[],0)
        return res


obj = Solution()
r =obj.combination_sum([2,3,5,7],7)
print(r)