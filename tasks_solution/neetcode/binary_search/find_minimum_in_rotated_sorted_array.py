#find minimum in rotated array
# left part is continuation of the right part

from typing import List


class Solution:
    def find_minimum(self,nums: List[int])->int:
        res = nums[0]
        left, right = 0, len(nums)-1

        while left <= right:
            #  The condition if nums[left] < nums[right] checks
            #  if the subarray between the left and right pointers is already sorted.
            if nums[left] < nums[right]:
                res = min(res,nums[left])
                break

            middle  = (left+right)//2
            res = min(res,nums[middle])
            # when value from middle >= left move left pointer to right side (to middle pointer)
            if nums[middle]>=nums[left]:
                left= middle+1
            else:
                # when value from middle < left move right pointer to left side (to middle pointer)
                right= middle-1

        return res

o = Solution()
print(o.find_minimum([22,22,22,22,-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21]))
