# slidig window
# for right:
#     додати елемент
#     while умова порушена:
#         прибрати left
#         left++
#     оновити відповідь
#
#
# two pointers
# while left < right:
#     if sum < target: left++
#     elif sum > target: right--
#     else: found
#
# fast slow
# slow = head
# fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast: цикл