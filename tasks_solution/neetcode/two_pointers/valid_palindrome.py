# Given a string s, return true if it is a palindrome, otherwise return false.
#
# A palindrome is a string that reads the same forward and backward.
# It is also case-insensitive and ignores all non-alphanumeric characters.


class Solution:
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:

            while left < right and not self.is_aplha_num(s[right]):
                right -= 1
            while left <= right and not self.is_aplha_num(s[left]):
                left += 1

            if s[left].lower() != s[right].lower():
                return False
            left,right = left+1, right-1
        return True


    def is_alpha_num(self, char):
        return (ord('A')<= ord(char)<= ord('Z') or
                ord('a') <= ord(char)<= ord('z') or
                ord('0')<= ord(char)<= ord('9')
                )
# first method
# These inner loops skip non-alphanumeric characters by moving
# the left pointer to the right and the right pointer to the left until
# an alphanumeric character is found.

# After skipping non-alphanumeric characters, the lowercase versions
# of the characters at left and right are compared. If they are not equal,
# the string is not a palindrome and False is returned.

# second method
# method is_alpha_num This returns True if char is between 'A' and 'Z', 'a' and
# 'z', or '0' and '9' in ASCII values, indicating that it is an alphanumeric character.