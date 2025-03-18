# given k linked lists, merge them in one linked list
#
# Input: lists = [[1,2,4],[1,3,5],[3,6]]
# Output: [1,1,2,3,3,4,5,6]
from typing import Optional, List

from base.passed_list_as_paraam import list1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val =val
        self.next= next


class Solution:
    def merge_k_sorted_lists(self, linked_lists: List[Optional[ListNode]])-> Optional[ListNode]:
        if not linked_lists or len(linked_lists) == 0:
            return None

        while len(linked_lists) > 1: # check lists for merge, for merging need at lest two
            list_result = []

            for i in range(0, len(linked_lists),2): #iterate on array with step 2, because we merge two lists
                list1 = linked_lists[i]
                # check if obj exist in linked list and return None or obj
                list2 = linked_lists[i + 1] if (i + 1) < len(linked_lists) else None
                # call the function for merging two lists
                list_result.append(self.merge_lists(list1, list2))
            linked_lists = list_result

        return linked_lists[0]

    def merge_lists(self,list_one, list_two):
        dummy  = ListNode()
        tail = dummy

        while list_one and list_two:
            # compare the value and assign lower object to linked list and update pointer
            if list_one.val > list_two.val:
                tail.next = list_two
                list_two = list_two.next
                # assign lower value to linked and update pointer
            else:
                tail.next  = list_one
                list_one = list_one.nxt
            tail = tail.next   # update pointer , move pointer to just new assigned obj (because it's last)

        if list_one:
            tail.next = list_one
        if list_two:
            tail.next = list_two

        return dummy.next


