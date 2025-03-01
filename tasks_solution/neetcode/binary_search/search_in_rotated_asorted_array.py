from typing import List


class Solution:
    def search(self, nums: List[int],  target: int)-> int:
        left, right =0, len(nums)

        while left <= right:
            middle = (left+ right)//2
            if target==nums[middle]:
                return middle  # Return the index if the target is found

            # check if subarray is sorted
            if nums[left] <= nums[right]:
                if target > nums[middle] or  target < nums[left]:
                    left = middle+1
                else:
                    right=middle-1

            # subarray is rotated
            else:
                # when target less than middle or grater right value
                # then move right pointer to middle
                if target < nums[middle] or target > nums[right]:
                    right = middle-1
                else:
                # when target  more than middle or less then left
                # then move left pointer to middle
                    left = middle+1

        return -1
