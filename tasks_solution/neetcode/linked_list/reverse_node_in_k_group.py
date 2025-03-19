# given an sorted linked list  and k value
# list have n elements, k is group of element needed to reverse
# return linked list where each group is reversed
#
# Input: head = [1,2,3,4,5], k = 3  # 1,2,3 - is a group ; 4,5 is not a group
# Output: [3,2,1,4,5]
from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def reverse_node_in_k_group(self, head: Optional[ListNode], k : int)-> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        group_previous = dummy_node

        while True:
            group_tail = self.get_k_group_tail(group_previous,k)
            if not group_tail:
                break
            head_next_group = group_tail.next

            previous, current  = group_tail.next, group_previous.next
            # reverse linked list group
            while current != head_next_group:# on first iteration current is a head of group
                tmp = current.next # save node from the right side
                current.next = previous # left node assign to right
                # update pointers
                previous = current # current pointer now is on left position
                current = tmp # right pointer now on the current position

            # merge tail left group with head of right group;
            # update position for finding tail in method get_k_group_tail
            tmp = group_previous.next # save the tail of reverted group
            group_previous.next = group_tail # assign (glued) head and tail (0->3 or 1->6 etc  )
            group_previous = tmp # now tail is assign

        return dummy_node.next


    def get_k_group_tail(self, node, k):
        # iterate until go to tail fo k group
        while node and k > 0:
            node = node.next
            k -= 1
        return node # return tail of group k

n7 = ListNode(7)
n6 = ListNode(6,n7)
n5 = ListNode(5,n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
k = 3

obj = Solution()
o = obj.reverse_node_in_k_group(n1,k)
print(o)