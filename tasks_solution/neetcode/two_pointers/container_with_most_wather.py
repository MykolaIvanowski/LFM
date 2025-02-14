from typing import List


class Solution:
    def max_area(self,height: List[int])-> int:
        left, right = 0, len(height)-1
        result = 0

        while left< right:
            area = min(height[left], height[right]) * (right-left)
            result = max(result, area)
            if height[left]<= height[right]:
                left +=1
            else:
                right -= 1
        return result


# Initialize two pointers: left at the beginning and right at the end of the list.
#
# Use a while loop to iterate until the left pointer meets the right pointer.
#
# Calculate the area between the lines pointed by left and right,
# updating the maximum area found.
#
# Move the pointer that points to the shorter line towards the center
# to potentially find a larger area.