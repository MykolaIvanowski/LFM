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

class Solution:
    def letter_combination(self, digits: str)-> List[str]:
        result  = []


        def backtrack(index_digit, variety_char):
            # achieve max depth of tree, and save a result
            if len(variety_char) == len(digits):
                result.append(variety_char)
                return

            # this loop is correspond for variety of chars
            # example: give me value (this value is string) from dictionary,
            # then iterate through each symbol of this value
            for c in digits_char[digits[index_digit]]:

                # update  index (for going to next digit) and concatenate chard for achieve variety
                # ad then go deper in tree
                backtrack(index_digit + 1, variety_char + c)

        # entry point
        if digits:
            backtrack(0, '')

        return result

obj  = Solution()
r = obj.letter_combination('23')
print(r)


class SolutionIterable:
    def letter_combination(self, digits: str)-> List[str]:
        if not digits:
            return []
        result = ['']

        # main loop run for digit (it is key for  dictionary)
        for digit in digits:
            tmp = [] # we should use temp array because it may create unexpected behavior

            # take symbols from result array, which we will concatenate  with new symbol for creating variety
            for base_char in result:

                # take values (it is string) from base dictionary and iterate through it
                for c in digits_char[digit]:
                    # add new variety of symbols to temporary array
                    result.append(base_char + c)

            # we can not use result, because it will create endless loop as we use result loop on in second for
            result = tmp

        return result


obj = SolutionIterable()
print('9000000000000')
r = obj.letter_combination('232')
print(r)
