# yuo are given two sorted arrays nums1, nums2
# find the median value among all elements of the two arrays
# your solution must run in O(log(n+m)) time

# Input: nums1 = [1,2], nums2 = [3]
# Output: 2.0

# Input: nums1 = [1,3], nums2 = [2,4]
# Output: 2.5

from typing import List


class Solution:
    def find_median_sorted_arrays(self,nums1: List[int], nums2:List[int]) -> float :
        total_middle = (len(nums1) + len(nums2)) // 2

        # array num1 is always smaller
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        # binary search logic build on smaller array
        left, right  = 0, len(nums1) - 1

        while True:
            middle_one = (left + right) // 2 # num1

            # maintain balance around the half point of the combined array
            pointer_balancer = total_middle - middle_one - 2

            one_left  = nums1[middle_one]  if middle_one >= 0 else float("-infinity")
            one_right = nums1[middle_one + 1] if (middle_one+1) < len(nums1) else float("infinity")
            two_left = nums2[pointer_balancer] if pointer_balancer >= 0 else float("-infinity")
            two_right  = nums2[pointer_balancer + 1] if (pointer_balancer + 1) < len(nums2) else float("infinity")

            if one_left <= two_right and two_left <= one_right:
                if total_middle % 2:
                    return min(one_right, two_right)
                return (max(one_left, two_left)+ min(one_right, two_right)) / 2
            elif one_left > two_right:
                right = middle_one - 1
            else:
                left = middle_one + 1

obj = Solution()

print(obj.find_median_sorted_arrays([8,10,12,13,15,16,17], [1,2,3,4,4,4,4,4,4,4,5,6,7,8]))


# pointer_balancer represents the partition index in the second array, nums2.
# Its role is to complement the partition index i in the first array, nums1,
# ensuring that the combined left and right halves from both arrays
# are balanced around the total number of elements.


