# give an array  and k ; k is sliding window
# fine maximum value from sliding window per iteration
#
# Input: nums = [1,2,1,0,4,2,6], k = 3
#
# Output: [2,2,4,4,6]
#
# Explanation:
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2    ps: it is not matrix it is the same array [1,2,1,0,4,2,6]
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6

from collections import deque
from typing import List


class Solution:
    def max_sliding_window(self, nums: List[int], k : int)-> int:
        queue = deque() # it contain indexes in decreasing order by value in nums
        result = []
        left = right = 0

        while right < len(nums):
            # element in right greater then element teken by index (from left part of queue)
            while queue and nums[queue[-1]] < nums[right]:
                # remove element from right
                queue.pop()

            queue.append(right)

            # check for removing redundant indexes in queue pointed in left side of nums
            # update queue in k range
            if left > queue[0]:
                queue.popleft() # remove passed indexes

            # (right+1)>=k ensures that the sliding window has reached its full size of k
            # before we start recording the maximum in result
            if (right+1)>=k:
                result.append(nums[queue[0]]) # add greater value to result (greater is in beginning, left side)
                left+=1
            right+=1

        return result


obj = Solution()
print(obj.max_sliding_window([1,2,1,0,1,4,2,6], 3))