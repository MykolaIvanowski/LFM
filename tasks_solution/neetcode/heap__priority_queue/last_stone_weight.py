# given array, on each step we chose the max numbers and then subtract them,
# we continue until we have only one number, then return it
#
# Input: stones = [2,3,6,2,4]
# Output: 1
#
# Input: stones = [1,2]
# Output: 1
#
import heapq
from typing import List


class Solution:
    def last_stone_weight(self, stones: List[int])->int:
        stones = [-i for i in stones] # make all integer as negative (because we can not use max heap )
        heapq.heapify(stones)

        #  as we pop values then we move our heap to len equal 0
        while 1 < len(stones):
            # as we use min heap that mean first element will be less or quel to second element
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            # if second == first , so nothing needs to be added back to the heap.
            # as we pop them from the heat it can be counted as we subtract them and result is zero, (do not need add zero)
            if second > first:
                heapq.heappush(stones, first-second)

        stones.append(0)# in case we have empty heap
        return abs(stones[0]) # abs return absolute value, and absolute value is positive

obj = Solution()
r = obj.last_stone_weight([1,2,3,4,5,7,7])
print(r)



