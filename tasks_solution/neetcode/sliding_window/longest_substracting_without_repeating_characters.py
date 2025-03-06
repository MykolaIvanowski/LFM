# given string s, find in string non repeating substring
#
# Input: s = "abcabbabc"
# Output: 3
#
# Explanation: The string "abc" is the longest without duplicate characters.


class Solution:
    def length_of_longest_substring(self, s: str)-> int:
        left = 0
        res = 0
        char_set = set()

        for right in range(len(s)):
            while s[right]in char_set:
                char_set.remove(s[right])
                left += 1
            char_set.add(s[right])

            # To get the length of this substring, you take the difference
            # between right and left, which gives you the number of indices between left and right,
            # adding +1 because index start from 0
            res = max(res, right-left+1) # If left = 0 and right = 2, the substring is "abc".
                                         # Its length is res = 2 - 0 + 1 = 3

        return res