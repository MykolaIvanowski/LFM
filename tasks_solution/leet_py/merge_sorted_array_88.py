
def merge_sorted_array(nums1,m, nums2,n):
    for _ in range(n):
        nums1.pop()
    nums1 += nums2
    nums1.sort()


print(merge_sorted_array([1,2,3,0,0,0,], 3,[2,5,6],3))


#  good solution)
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        # Start from the end of the combined array and work backwards.
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy the remaining elements of nums2 to nums1.
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
