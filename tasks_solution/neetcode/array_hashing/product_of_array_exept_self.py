# Given an integer array nums, return an array output where output[i]
# is the product of all the elements of nums except nums[i].
# O(n) time without using the division operation

#Input: nums = [1,2,4,6]
#Output: [48,24,12,8]

from typing import List

class Solution:
    def product_except_self(self, nums: List[int])-> List[int]:
        res = [1] *(len(nums))
        prefix = 1
        postfix = 1

        # calculate products prefix
        for i in  range(len(nums)):
            res[i] = prefix
            prefix *=nums[i]

        #calculate products postfix and update result
        for i in range(len(nums)-1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

## loop 1
# For each index i, you set res[i] to the value of prefix, then multiply prefix by nums[i].
##
# This step ensures that res[i] contains the product of all the elements to the left of i.

## loop 2
# For each index i, you multiply res[i] by postfix, then multiply postfix by nums[i].
##
# This step ensures that res[i] is now updated to contain the product of all
# the elements to the right of i.