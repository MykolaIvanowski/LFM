# given linked list, revere linked list
#
# Input: head = [0,1,2,3] or   link_obj1 -> link_obj2 -> link_obj3 -> link_obj4
# Output: [3,2,1,0]       to   link_obj4 -> link_obj3 -> link_obj2 -> link_obj1
#
#
# Definition for singly Linked-list
# class LinkedList
#   def __init__(self, val = 0, next = None):
#       self.val = val
#       self.next = next
class ListNode:
  def __init__(self, val = 0, next = None):
      self.val = val
      self.next = next
from typing import Optional


class Solution:
    def reverse_list(self, head: Optional[ListNode])-> Optional[ListNode]:
        previous_node, current_node  = None, head

        # making swipe directions from left to right direction
        while current_node:
            temporary_link = current_node.next # return next node from the right side
            current_node.next = previous_node # asight previous node from the left side
            previous_node = current_node # asight current node to previous
            current_node = temporary_link # asight node from the left to current node

        # return previous_node because this node on the last iteration on center
        # current_node become None (last element point on None)
        return previous_node

obj=Solution()
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2) # head node

print(obj.reverse_list(n1).val)
print()
class SolutionRecursive:
    def recursive_list(self, head: Optional[ListNode])->Optional[ListNode]:
        if not head:
            return None

        current_node = head # saved linked object
        if head.next: # if head last element in linkedlist the skip
            current_node = self.recursive_list(head.next) # asight previous node from right

            # sight pointer from right to left
            head.next.next = head # obj3 next obj4 next None = obj3 next obj4 next obj3

        head.next = None # remove pointer from left  to right (obj3 next obj4)

        # why return current_node, not a head?
        # current_node pass from the deepest recursive call and it will return last element (now it first element)
        # if pass head it will return first element from linked list
        # but our first element turn to last element in linked list
        return current_node # return obj4

obj = SolutionRecursive()
n4 = ListNode(4)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1, n2)
x=obj.recursive_list(n1)
print(x.val)
