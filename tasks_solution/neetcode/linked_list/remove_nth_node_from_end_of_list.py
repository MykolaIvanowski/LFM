# given linked list, given n
#  remove nth node counter from end fo the list and return head of list
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_node_from_list(self, head: Optional[ListNode], n:int)->Optional[ListNode]:
        dummy = ListNode(0,head)
        left, right = dummy, head
        # making a distance between left and right reference
        while n > 0:
            right = right.next
            n -= 1
        # move references right and left until right reference rich the end of linked list
        while right:
            left = left.next
            right = right.next
        # remove nth element in lintked list
        left.next = left.next.next
        return dummy.next

n5 = ListNode(6)
n4 = ListNode(5,n5)
n3 = ListNode(4,n4)
n2 = ListNode(3,n3)
n1 = ListNode(2,n2)
n0 = ListNode(1,n1)

obj = Solution()
r = obj.remove_nth_node_from_list(n0, 2)
print(r.val)