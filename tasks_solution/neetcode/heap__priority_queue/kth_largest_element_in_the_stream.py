# design a class to find a k-th largest element in the stream
#  including duplicates
#
# class should have two methods
# constructor(int k, int[] nums)  # find k-th largest from nums
# add(int val) add integer to stream and  and return k-th largest from stream
#
# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]
# Output:
# [null, 3, 3, 3, 5, 6]
#
# Explanation:
# KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
# kthLargest.add(3);   // return 3
# kthLargest.add(5);   // return 3
# kthLargest.add(6);   // return 3
# kthLargest.add(7);   // return 5
# kthLargest.add(8);   // return 6
import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        heapq.heapify(self.min_heap) # transform list to min heap

        # in loop we remove element until quantity of element will be equal to k
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap) # function heappop remove and return smallest element fro the heap

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap,val) # add element to heap  works in O(lon n) complexity
        # add one element then remove one element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0] # return k-th largest element

obj = KthLargest(3, [2,3,4,6,3,1])
r = obj.add(2)
print(r)
