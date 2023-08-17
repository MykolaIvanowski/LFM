#  Palindrome Number
# Easy
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
from typing import List


x = 32111123
# print(slice(x), x.len())


def isPalindrome(x):
    if x < 0:
        return False

    r = 1
    while x / r >= 10:
        r *= 10
    while r > 1:
        divided, x = divmod(x, r)
        x, moduled = divmod(x, 10)
        if divided != moduled:
            return False
        r //= 100

    return True
print(isPalindrome(x))