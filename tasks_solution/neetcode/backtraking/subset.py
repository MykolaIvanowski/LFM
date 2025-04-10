# given an array , give all possible subset from this array
# hit quantity possible solution is 2^n subsets
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# Input: nums = [7]
# Output: [[],[7]]
#
from typing import List

# hint from root to last leaf we have 2^n path
class Solution:
    def subset(self, nums: List[int])-> List[List[int]]:
        result = []
        subset = []

        def depth_for_search(index):
            # index is non local variable that means it will change when recursive call and and go back
            # every time when we go to last leaf we will have index >= len(nims),
            # and we will have finished uniq subset in variable subset
            if index >= len(nums):
                result.append(subset.copy())
                return
            # add element to stack ,
            # reason why it have right variety of subset
            # is that we pop() elements from stack in way when we change left path to rigth path
            subset.append(nums[index])

            # go to left leafs, and update index, index play roll to finis the recursive calls
            depth_for_search(index+1)

            # clear stack for next subset, it is crucial clear stack when we change path
            subset.pop()

            # go to  right leafs, and update index
            depth_for_search(index+1)

        depth_for_search(0)
        return result

a = [2,3,4]
obj = Solution()
r = obj.subset(a)
print(r)

class SolutionItrative:
    def subsets(self, nums: List[int])-> List[List[int]]:
        # add to result array empty set, it is base case (think as this not like matrix)
        result = [[]]

        for num in nums:
            # in every iteration to every result values we add num then add to result (+=)
            #  comprehension loop is array += num to elements, then array + comprehension_array
            # 1. [[]] + 1 => [[]] + [[1]] => [[], [1]]
            # 2. [[], [1]] + 2 => [[],[1]] + [[],[1]] + [[2], [1,2]] => [[],[1], [2], [1,2]]
            result += [subset+[num] for subset in result]

        return result


obj = SolutionItrative()
r = obj.subsets([1,2,3])
print(r)