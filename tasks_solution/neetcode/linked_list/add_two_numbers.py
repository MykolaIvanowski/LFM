# given two linked lists
# add values in this list, list1 represent number onme list2 represent number two
# numbers saved in reverse order
# return linked list with result
#
# solution represent math operation add from elementary school       321
#                                                                   +
#                                                                    654
#                                                                   -----
#                                                                    975
# Input: l1 = [1,2,3] ->321, l2 = [4,5,6]->654
# Output: [5,7,9]
#
# Explanation: 321 + 654 = 975.

class ListNode:
    def __init__(self, val = 0, next = 0 ):
        self.val = val
        self.next = next


class Solution:
    def add_tewo_lists(self,l1: ListNode, l2: ListNode)-> ListNode:
        dummy = ListNode()
        current  = dummy

        carry = 0

        while l1 or l2 or carry:
            # if exist value to assign, for future calculation
            number1 = l1.val if l1 else 0
            number2 = l2.val if l2 else 0

            number = number1 + number2 + carry
            # if it is >= 10 then we should carry number
            # 14//10 carry 1; 24//10 carry 2; 44//10 carry 4
            # if we have two digit number we get only right digit
            carry = number // 10
            # if we have two digit number we get only left digit
            number = number % 10
            current.next = ListNode(number) # new node to linkedlist result

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


l1n3 = ListNode(3)
l1n2 = ListNode(2,l1n3)
l1n1 = ListNode(1,l1n2)

l2n3 = ListNode(6)
l2n2 = ListNode(5,l2n3)
l2n1 = ListNode(4, l2n2)

obj = Solution()
n1r = obj.add_tewo_lists(l1n1,l2n1)
print()