# given linked list, find if it have a cycle?
# return True if linked have a cykle
#
# obj1 -> obj2 -> obj3->obj4->|
#          ^-----------------<|
#
from typing import Optional


class ListNode:
    def __init__(self,val=0, next=None):
        self.val =val
        self.next= next

class SolutionFastSlowPointer():
    def linked_list_cycle(self, head: Optional[ListNode])-> bool:
        fast, slow = head, head

        while fast and fast.next: # check if current and next not None for fast pointer
            slow = slow.next      # move reference for slow on one positions
            fast = fast.next.next # move reference for fast pointer on two positions
            if slow == fast:
                return True
        return False

class SolutionHashSet:
    def linked_list_cycle(self, head: Optional[ListNode])-> bool:
        hashset = set()    # using set for checking if a node already added
        current_node = head

        while current_node:
            if current_node in hashset: # if node in hashset it is a cycle
                return True
            hashset.add(current_node)
            current_node = current_node.next
        return False