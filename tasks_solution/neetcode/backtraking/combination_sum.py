# given array of numbers and int target value.
# find how many sets uniq numbers equal to target
# #
# Input:  nums = [2,5,6,9]    # as you see one numer can be used many times
#         target = 9
# Output: [[2,2,5],[9]]
##
# Input:  nums = [3,4,5]
#         target = 16
# Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
from typing import List


class Solution:
    def combination_sum(self, nums: List[int], target: int)-> List[List[int]]:
        res =[]

        def dfs(i , cursor, total):
            if total == target:
                res.append(cursor.copy())
                return
            if i>=len(nums) or total> target:
                return

            cursor.append(nums[i])
            dfs(i, cursor, total+ nums[i])
            cursor.pop()
            dfs(i + 1, cursor, total)

        dfs(0,[],0)
        return res


obj = Solution()
r =obj.combination_sum([2,3,5,7],7)
print(r)