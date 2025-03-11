# given two sorted list, merge into one sorted linked list
#
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]
#
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def two_sorted_list(self,list1:ListNode,list2: ListNode)-> ListNode:
        result_linkedlist = node =  ListNode()

        while list2 and list1:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node=node.next

        node.next = list1 or list2

        return result_linkedlist.next