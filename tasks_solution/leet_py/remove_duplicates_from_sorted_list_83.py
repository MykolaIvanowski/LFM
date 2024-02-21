# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_duplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    c = head
    while c:
        while c.next and c.next.val == c.val:
            c.next = c.next.next
        c = c.next
    return head


