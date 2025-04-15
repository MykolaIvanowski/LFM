# given array, this time it may contain duplicates
# find all subset for this sequence, result should not contain duplicates,
# duplicates contain in main array count as not duplicate and should be in result
#
# Input: nums = [1,2,1]
# Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
#
# Input: nums = [7,7]
# Output: [[],[7], [7,7]]
#
from typing import List


class SolutionIteration:
    def subset_with_duplicates(self, nums: List[int])-> List[List[int]]:
        nums.sort()
        result = [[]]
        result_max_index = index = 0

        # this loop go through main array
        for i in range(len(nums)):
            # next line help skip duplicated, prevent adin them to result array
            # how? in next loop instead to tmp add empty list it will add duplicated value
            # and base on this it will create next uniq subset
            index = result_max_index if i >= 1 and nums[i] == nums[i-1] else 0
            # this index used in next loop for point last element in current result array
            # it help top go through result list and made new uniq subset
            result_max_index = len(result)

            # in this loop created uniq subsets
            for j in range(index, result_max_index):
                # temp use for creating subset, based on what we have in result array
                tmp = result[j].copy()
                #  update temp subset from given array
                # if we have duplicated then j should not be 0 for escape adding duplicates
                tmp.append(nums[i])
                # add recently made subset to result array
                result.append(tmp)

        return result

obj = SolutionIteration()
r = obj.subset_with_duplicates([1,2,2,5,5])
print(r)


class SolutionBacktracking:
    def subset_with_duplicates(self, nums: List[int])-> List[List[int]]:
        result = []
        nums.sort()# group duplicates

        def backtracking(index, subset):
            # this if tell as that we achieved end of depth and result is founded
            if len(nums) == index:
                result.append(subset[::])#  shallow copy
                return
            subset.append(nums[index])
            backtracking(index+1, subset)
            subset.pop() # clear last added element, it prepare subset to next subset veriaty
            # this loop for skipping duplicates, duplicated hide under index that why we use index+1
            # nums[index] == nums[index+1] this help recognise duplicates
            # index + 1 < len(nums) this help pass already passed values in given array
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            # go to next subtree, right subtree
            backtracking(index+1, subset)
        backtracking(0, [])
        return result

obj = SolutionBacktracking()
r  = obj.subset_with_duplicates([1,2,2,4])
print(r)