# given array , and in this array numbers only from 1 - n (1 to len()-1)
# numbers in array represent pointer to index
# we cen iterate like thought linked list
#
# Input: nums = [1,2,3,2,2]
# Output: 2
from typing import List


class Solution:
    def find_duplicates_number(self,nums: List[int])-> int:
        slow, fast =  0,0
        while True:
            slow = nums[slow]       # represent obj.next
            fast = nums[nums[fast]] # represent obj.next.next
            if slow == fast:
                # this loop break when slow and fast pointer point to middle 'object'
                # equidistant pointers start linked list and end loop linked list
                # 0->1->3->(4)->2->3-->4  (obj where slow and fast)
                break

        slow_second = 0
        while True:
            # moving pointers until it poit to equal object
            slow = nums[slow]
            slow_second = nums[slow_second]
            if slow == slow_second:# 0->1->(3)->4->2->(3)-->4 pointers point on 3 and 3
                return slow



obj = Solution()
print(obj.find_duplicates_number([1,3,3,4,2]))
print()