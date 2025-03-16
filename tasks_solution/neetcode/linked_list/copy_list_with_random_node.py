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
        # in this list we will save as key our main linked list
        # as value store new linked list
        main_linked__transfer_to__copy_linked = {None: None}

        current = head

        # create object and copy value from original linked list
        while current:
            copy = ListNode(current.val)
            main_linked__transfer_to__copy_linked[current] = copy
            current  = current.next

        current=head

        # coppy pointers from original linked lists
        while current:
            copy = main_linked__transfer_to__copy_linked[current] # can be replaced copy = copy.next

            # when you pass as key an old references you will returned as a value a deep copied node
            # hash_map[key1] returned obj_1; hash_map[key1.next] returned obj_2
            copy.next = main_linked__transfer_to__copy_linked[current.next]
            # hash_map[key1.random] returned obj_random
            copy.random = main_linked__transfer_to__copy_linked[current.random]
            current = current.next

        return current



n6 = ListNode(6)
n5 = ListNode(5,n6)
n4 = ListNode(4,n5,n5)
n3 = ListNode(3, n4,None)
n2 = ListNode(2,n3,n4)
n1 = ListNode(1, n2,n6)
n5.random = n5
n6.random = n1

obj = Solution()
ln = obj.copy_random_list(n1)
print(ln.val)