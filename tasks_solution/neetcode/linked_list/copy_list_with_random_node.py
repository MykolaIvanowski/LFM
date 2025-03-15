# given linked list, in every node  have two reference
# regular reference from left to right, and random reference
# create a deep copy of the linked list
#
# Input: head = [[3,null],[7,3],[4,0],[5,1]]
# Output: [[3,null],[7,3],[4,0],[5,1]]
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val= val
        self.next = next
        self.random = random


class Solution:
    def copy_random_list(self, head: Optional[ListNode])-> Optional[ListNode]:
        old_to_copy = {None: None}

        current = head


        while current:
            copy = ListNode(current.val)
            old_to_copy[current] = copy
            current  = current.next

        current=head


        while current:
            copy=old_to_copy[current]
            copy.next=old_to_copy[current.next]
            copy.random=old_to_copy[current.random]
            current=current.next

        return current