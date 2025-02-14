# You are given an array non-negative integers height which represent an
# elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
#
# Return the maximum area of water that can be trapped between the bars.
from typing import List


class Solution:
    def trap(self, height: List[int])->int:
        if not height:
            return 0
        left,right =0, len(height)-1

        left_max, right_max =height[left], height[right]
        res=0

        while left > right_max:
            if left_max < right_max:
                left +=1
                left_max=max(left_max,height[left])
                res+=left_max-height[left]
            else:
                right=-1
                right_max=max(right_max,height[right])
                res+=right_max-height[right]

        return res
#
# If left_max is less than right_max, it means the limiting factor for
# trapping water is on the left side. The left pointer is moved one step to the right.
#
# left_max is updated to be the maximum of the current left_max and
# the new height at the left pointer.
#
# The trapped water at this position is left_max - height[left],
# and this value is added to res.
#
# Otherwise, the limiting factor is on the right side.
# The right pointer is moved one step to the left.
#
# right_max is updated to be the maximum of the current right_max
# and the new height at the right pointer.
#
# The trapped water at this position is right_max - height[right],
# and this value is added to res.