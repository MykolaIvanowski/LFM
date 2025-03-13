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
        # run cycle until it end, fast poit to end of linked list, slow ppoint to half of linked list
        while slow_ref and fast_ref:
            slow_ref = slow_ref.next
            fast_ref = fast_ref.next.next

        second_current_node = slow_ref.next
        second_previous_node = slow_ref.next = None # erase pointer in linked list on half part

        # change reference direction for second part of linked list
        # making swipe from left side to right side
        while second_current_node:
            temp_liked_obj = second_current_node.next # obj5 -> obj6 -> obj7 turn into temp = obj6->obj7
            second_current_node.next = second_previous_node # second part o5->o6->o7 turn into o5
            second_previous_node = second_current_node #  previous and current point on the same obj
            second_current_node = temp_liked_obj # None  turn to obj6->obj7

        first_current_node, second_current_node = head, second_previous_node

        # merge linked lists (on formula [0, n-1, 1, n-2, 2, n-3, ...])
        while second_current_node:
            # temporary values used for saved linked sequences
            tmp1, tmp2 = first_current_node.next, second_current_node.next
            first_current_node.next = second_current_node # add n+1  object to right reference
            second_current_node.next = tmp1 # add n obj to second linked list
            first_current_node, second_current_node = tmp1, tmp2 # update linked pointers


n7 = ListNode(7)
n6 = ListNode(6, n7)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

obj = Solution()
obj.reorder_list(n1)