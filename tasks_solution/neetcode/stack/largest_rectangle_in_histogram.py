# find max rectangle transverse, longitudinal in array.
from typing import List


class Solution:
    def largest_rectangle_area(self,heights: List[int])->int:
        max_aria = 0
        stack=[]

        for i, h in enumerate(heights):
            start = i
            while stack and start[-1][0]> h:
                # If the stack isn't empty and the height of the current bar h is less
                # than the height of the bar at the top of the stack, i
                # We pop the top of the stack
                index, height = stack.pop()


                # calculate the area using the height of the popped bar and the distance
                # from the popped index to the current index (i - index).
                max_aria = max(max_aria, height* (i-index))

                #The variable start is updated to the popped index
                # to maintain the left boundary of potential rectangles.
                start = index
            stack.append((start,h))

        for i , h in stack:
            #This calculates the area of the remaining rectangles (extended)
            # and updates maxArea
            max_aria=max(max_aria, h * (len(heights)-i))

        return max_aria

# Input: heights = [2, 1, 5, 6, 2, 3]
#
# Step 1: Initialize maxArea to 0 and stack to []
#
# Step 2: Iterate through the heights array:
#         a. For i = 0, h = 2
#            - stack = [(0, 2)]
#         b. For i = 1, h = 1
#            - Pop (0, 2) from stack
#            - maxArea = max(0, 2 * (1 - 0)) = 2
#            - stack = [(0, 1)]
#         c. For i = 2, h = 5
#            - stack = [(0, 1), (2, 5)]
#         d. For i = 3, h = 6
#            - stack = [(0, 1), (2, 5), (3, 6)]
#         e. For i = 4, h = 2
#            - Pop (3, 6) from stack
#            - maxArea = max(2, 6 * (4 - 3)) = 6
#            - Pop (2, 5) from stack
#            - maxArea = max(6, 5 * (4 - 2)) = 10
#            - stack = [(0, 1), (2, 2)]
#         f. For i = 5, h = 3
#            - stack = [(0, 1), (2, 2), (5, 3)]
#
# Step 3: Process remaining elements in the stack:
#         a. Pop (5, 3) from stack
#            - maxArea = max(10, 3 * (6 - 5)) = 10
#         b. Pop (2, 2) from stack
#            - maxArea = max(10, 2 * (6 - 2)) = 10
#         c. Pop (0, 1) from stack
#            - maxArea = max(10, 1 * (6 - 0)) = 10
#
# Output: maxArea

