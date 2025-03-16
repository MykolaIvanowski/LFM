# given a linked list, reorder this list on formula [0, n-1, 1, n-2, 2, n-3, ...]
# return linked list
#
# input obj1-> obj2-> obj3->obj4->obj5->obj6->obj7
# output obj1-> obj7-> obj2 -> obj6 -obj3-> obj5 ->obj4
from typing import Optional


class ListNode:
    def __init__(self,val= 0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorder_list(self, head:Optional[ListNode])-> None:
        slow_ref, fast_ref = head, head.next
        # run cycle until it end, fast poit to end of linked list, slow point to half of linked list
        while slow_ref and fast_ref:
            slow_ref = slow_ref.next
            fast_ref = fast_ref.next.next

        second_listnode = slow_ref.next
        second_previous_node = slow_ref.next = None # erase pointer in linked list on half part

        # change reference direction for second part of linked list
        # making swipe from left side to right side
        while second_listnode:
            temp = second_listnode.next # save next pointer
            second_listnode.next = second_previous_node # change pointer from right to left object
            second_previous_node = second_listnode #  previous node turn to next
            second_listnode = temp # current node turn to next node

        first_listnode, second_listnode = head, second_previous_node # l1 = 1,2,3,4; l2 = 7,6,5

        # merge linked lists (on formula [0, n-1, 1, n-2, 2, n-3, ...]) -> 1,7,2,6,3,5,4
        # mare is work in stages like moving pointers to temps and main nodes
        # and connect obj1 to obj7 and obj7 to obj2
        while second_listnode:
            # moving pointers further
            tmp1, tmp2 = first_listnode.next, second_listnode.next
            first_listnode.next = second_listnode # made references like ojb1-> obj7 etc
            second_listnode.next = tmp1 # made references like obj7 -> obj2
            first_listnode, second_listnode = tmp1, tmp2 # moving pointers to next object


n7 = ListNode(7)
n6 = ListNode(6, n7)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

obj = Solution()
obj.reorder_list(n1)
print()