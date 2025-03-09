# given linked list, revere linked list
#
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]
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
    def reverse_list(self, head: Optional[ListNode]):
        previous_node, current_node  = None, head

        while current_node:
            temperary_link = current_node.next # return next node
            current_node.next = previous_node
            previous_node = current_node
            current_node = temperary_link

