# eplane binary search
from typing import List


class Solution:
    def binary_search(self,target: int, nums:List[int])->int:
        left_pointer = 0,
        right_pointer = len(nums)-1

        while left_pointer <= right_pointer:

            middle_pointer = (left_pointer + right_pointer) // 2

            # next line not lead to overflow in case number 2^32
            # middle_pointer = left_pointer + ((left_pointer-right_pointer)//2)

            # if target less than number in array, then update right pointer
            if nums[middle_pointer] > target:
                right_pointer = middle_pointer - 1
            # if target greater than target in array, then update left pointer
            elif nums[middle_pointer] < target:
                left_pointer = middle_pointer+1
            # target is equal to number from array
            else:
                return middle_pointer

        # if target is not found
        return - 1