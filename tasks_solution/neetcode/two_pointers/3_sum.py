# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
# and the indices i, j and k are all distinct. The output should not contain any duplicate triplets
from typing import List


class Solution:
    def threeSum(self, nums: List[int])->List[int]:
        result =  []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
            #If the current value a is greater than zero,
            # then we can't find any triplets that sum to zero
                break;

            if i > 0 and  a == nums[i-1]:
            #This condition skips the duplicate values to avoid redundant triplets ([a,b,c]).
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum=a+nums[right]+nums[left]
                if three_sum > right:
                    right-=1
                elif three_sum<left:
                    left+=1
                else:
                    result.append([a,nums[left],nums[right]])
                    left, right = left+1, right-1
                    while nums[left] == nums[right-1] and left<right:
                        left+=1

        return result



# If the sum of a, nums[l], and nums[r] is greater than zero, decrement r.
#
# If less than zero, increment l.
#
# If equal to zero, append the triplet to the result list, move both pointers inward,
# and skip duplicate values.