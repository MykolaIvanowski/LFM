# given two sorted list, merge into one sorted linked list
#
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]
#
# Definition for singly-linked list.
from typing import Optional

from base.passed_list_as_paraam import list1


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def two_sorted_list(self,list1:ListNode,list2: ListNode)-> ListNode:
        result_linkedlist = node =  ListNode() # head of result linked list

        while list2 and list1: # if nodes from both list not None
            if list1.val < list2.val:
                node.next = list1  # add next lowest linked object from list 1
                list1 = list1.next # move reference in linked list 1
            else:
                node.next = list2 # add next lowest linked object to node from list2
                list2 = list2.next #  move reference in linked list2
            node=node.next # move linked list reference (in the end of cycle node reference to last object)

        node.next = list1 or list2 #connect linked list which in not ended during while cycle

        # using next because first element it empty ListNode() which is declared in the beginning of method
        return result_linkedlist.next # still reference to first object

l1n4 = ListNode(7)
l1n3 = ListNode(5,l1n4)
l1n2 = ListNode(3,l1n3)
l1n1 = ListNode(1,l1n2)
l2n4 = ListNode(6)
l2n3 = ListNode(4, l2n4)
l2n2 = ListNode(2,l2n3)
l2n1 = ListNode(0, l2n2)

obj = Solution()
ln = obj.two_sorted_list(list1=l1n1,list2=l2n1)
print(ln.val)


class RecursiveSolution:
    def merge_two_lists(self, list1: Optional[ListNode], list2 : Optional[ListNode])-> Optional[ListNode]:
        if list1 is None:
            return list2 # list 1 if finished return instead list 2
        if list2 is None:
            return list1 # list 2 is finished return instead list 1

        if list1.val < list2.val:
            # greater value from list 2 connected to list 1 in sorted way
            list1.next = self.merge_two_lists(list1.next,list2)
            return list1
        else:
            # greater value from list 1 connected to list 2 in sorted way
            list2.next = self.merge_two_lists(list1, list2.next)
            return list2

obj = RecursiveSolution()
n = obj.merge_two_lists(l1n1, l2n1)
print(n)
