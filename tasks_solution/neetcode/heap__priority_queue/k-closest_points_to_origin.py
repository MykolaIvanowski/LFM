# given matrix (2-D array) - represents the coordinates of a point on  an x,y axis plane
# find k-th closest points to origin (0,0)
#
# Input: points = [[0,2],[2,2]], k = 1
# Output: [[0,2]]
#
# Input: points = [[0,2],[2,0],[2,2]], k = 2
# Output: [[0,2],[2,0]]
from typing import List
import heapq


class Solution:
    def k_closest(self, points: List[List[int]], k: int)-> List[List[int]]:
        min_heap = []
        for x, y in points:
            # a^2 + b^2 = c^2
            # from pythagoras formula we can find distance from point in array to point 0,0#
            # actually we  do not need to take root, as we squaring it turn to positive result
            distance_to_origin = (x**2) + (y**2)
            # add points and distance to heap
            min_heap.append([distance_to_origin, x,y])

        heapq.heapify(min_heap) # actually made the heap

        result = []

        while k > 0:
            # it will pop smallest 'a' value in array [[a,b,c],[a,b,c], [a,b,c]]
            distance_to_origin, x,y, = heapq.heappop(min_heap)
            result.append([x,y])
            # it need for appending only k sequence
            k -= 1

        return result


o = Solution()
r = o.k_closest([[0,2],[2,0],[-2,-2]],2)
print(r)
