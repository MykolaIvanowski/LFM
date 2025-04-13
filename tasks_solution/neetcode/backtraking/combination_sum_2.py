# given array and target, array can have not unic values
# subset in sum should be equal to target
# each number in array can be use only once
# if array have [1,1] - then 1 can use two times, if [1,1,1] then three times
#
# Input: candidates = [9,2,2,4,6,1,5], target = 8
#
# Output: [
#   [1,2,5],
#   [2,2,4],
#   [2,6]
# ]

from typing import List


class Solution:
    def cambination_sum_2(self, candidates: List[int], target: int )->List[List[int]]:
        result = []
        # need sot for groping similar elements, leiter in while we skip
        candidates.sort()

        def dfs(index, uniq_subset, sum_uniq_subset):
            if sum_uniq_subset == target:
                # add subset
                result.append(uniq_subset.copy())
                return
            if sum_uniq_subset >target or index >= len(candidates):
                return
            # add element for checking subset in next call
            uniq_subset.append(candidates[index])

            # got to left subtree to check uniq combination
            # sum_uniq_subset + candidates[index] could be equal to target and it will be added to result array
            dfs(index+1, uniq_subset, sum_uniq_subset + candidates[index])

            # remove element for changing subset combination
            uniq_subset.pop()

            # index +1 < len(candidates) - this line avoid exception (IndexError)
            # skipp index element for move to next uniq element in given array (actually move will be in recursive call)
            while index +1 < len(candidates) and candidates[index]==candidates[index+1]:
                index +=1
            # go to right subtree, index incremented for check new element (combination) from given array
            dfs(index+1,uniq_subset, sum_uniq_subset)

        dfs(0,[],0)
        return result

obj = Solution()
r =obj.cambination_sum_2([2,2,2,3,5,7],7)
print(r)