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

        while n >0:
            right = right.next
            n -=1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next