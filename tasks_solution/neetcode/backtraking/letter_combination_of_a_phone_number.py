# old phone have a digits and letters on buttons
# given digits string
# find all letter combination for this digits
#
# digit 2 have abc letter , digit 3 have def
# Input: digits = "34"
# Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
#
# Input: digits = ""
# Output: []
from typing import List


class Solution:
    def letter_combination(self, digits: str)-> List[str]:
        result  = []
        digits_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'qprs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, veriaty_char):

            if len(veriaty_char) == len(digits):
                print(veriaty_char)
                result.append(veriaty_char)
                return
            for c in digits_char[digits[index]]:
                backtrack(index + 1, veriaty_char + c)

        if digits:
            backtrack(0, '')

        return result

obj  = Solution()
r = obj.letter_combination('23')
print(r)