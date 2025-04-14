# given an array, return all possible variety of sequences
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# permutation is n! for array (it is not time complexity)
from typing import List


class SolutionIterative:
    def permutation(self, nums: List[int])-> List[List[int]]:
        result_permutation = [[]]

        # in main loop, we iterate through given array
        for num in nums:
            copy_before_result_permutation = []

            # have empty list as value so at list one iteration
            for current_permutation in result_permutation:

                # on last iteration  we will have the same amount of integer in index array (array[index_array1,index_array2])
                # as we have in given array
                # len(given array) == len(index xarray)
                # used len()+1, it gives at least one iteration
                for i in range(len(current_permutation)+1):

                    # it used to reused permuted list from result
                    # copy help permutate next list
                    copy_current_permutation = current_permutation.copy() # made shallow copy

                    # insert method put value in specific position in list
                    # not update but add value and rest of sequence move to  positions +1 by index
                    # was [2,1] become [3,2,1], or was [2,1] become [2,3,1]
                    copy_current_permutation.insert(i , num) # play crucial role in forming permutation

                    #in this line we form main permuted array iteration by iteration
                    copy_before_result_permutation.append(copy_current_permutation)

            # when previous loop finished save permutation
            result_permutation = copy_before_result_permutation
        return result_permutation

obj = SolutionIterative()
r = obj.permutation([1,2,3])
print(len(r))

# how iteration can be visualized?
#  first loops ->   [[1]]
#  second loops ->  [[2, 1], [1, 2]]
#  third loops      [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
#
#
#           for i in range(len(current_permutation)+1):
# in this loop it is add like :
#                              [2, 1] -> [3, 2, 1]
#                              [2, 1] -> [2, 3, 1]
#                              [2, 1] -> [2, 1, 3]
#                              [1, 2] -> [3, 1, 2]
#                               etc.


class SolutionBacktracking:
    def permutation(self, nums: List[int])-> List[List[int]]:
        self.res = []
        self.backtracking(nums, 0)
        return self.res

    def backtracking(self, nums: List[int], index: int):
        # len == index when we reach the end of tree
        # after thet we should add result to result list
        if index==len(nums):
            self.res.append(nums[:])# add shallow copy
            return
        # on first iteration no swipes
        for i in range(index, len(nums)):
            # swiping elements create permuted array with we add to result array
            nums[index], nums[i] = nums[i], nums[index]
            self.backtracking(nums, index+1)
            nums[index], nums[i] = nums[i], nums[index]



obj = SolutionBacktracking()
r = obj.permutation([1,2,3,4])
print(r)

# Start: [1, 2, 3] (idx = 0)
#  ├── Swap idx=0, i=0 → [1, 2, 3]
#  │      ├── Swap idx=1, i=1 → [1, 2, 3]
#  │      │      ├── Swap idx=2, i=2 → [1, 2, 3] -> Solution: [1, 2, 3]  <- first save the leaf to result array
#  │      │      └── Backtrack → [1, 2, 3]
#  │      ├── Swap idx=1, i=2 → [1, 3, 2]
#  │      │      ├── Swap idx=2, i=2 → [1, 3, 2] -> Solution: [1, 3, 2]
#  │      │      └── Backtrack → [1, 2, 3]
#  │      └── Backtrack → [1, 2, 3]
#  ├── Swap idx=0, i=1 → [2, 1, 3]
#  │      ├── Swap idx=1, i=1 → [2, 1, 3]
#  │      │      ├── Swap idx=2, i=2 → [2, 1, 3] -> Solution: [2, 1, 3]
#  │      │      └── Backtrack → [2, 1, 3]
#  │      ├── Swap idx=1, i=2 → [2, 3, 1]
#  │      │      ├── Swap idx=2, i=2 → [2, 3, 1] -> Solution: [2, 3, 1]
#  │      │      └── Backtrack → [2, 1, 3]
#  │      └── Backtrack → [1, 2, 3]
#  ├── Swap idx=0, i=2 → [3, 2, 1]
#  │      ├── Swap idx=1, i=1 → [3, 2, 1]
#  │      │      ├── Swap idx=2, i=2 → [3, 2, 1] -> Solution: [3, 2, 1]
#  │      │      └── Backtrack → [3, 2, 1]
#  │      ├── Swap idx=1, i=2 → [3, 1, 2]
#  │      │      ├── Swap idx=2, i=2 → [3, 1, 2] -> Solution: [3, 1, 2]
#  │      │      └── Backtrack → [3, 2, 1]
#  │      └── Backtrack → [1, 2, 3]