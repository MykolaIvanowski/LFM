from typing import List

from tasks_solution.coint_exchange import array


class Solution:
    def encode(self,strs: List[str])-> str:
        r = ''
        for i in  strs:
            r += str(len(i)) + '#' + i
        return r

    def decode(self,s : str)-> List[str]:
        array = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            array.append(s[i:j])
            i = j

        return array

###
# While s[j] != '#': j += 1: This loop increments j until it finds the # character.
###
# length = int(s[i:j]): The substring from i to j is converted to an integer
# representing the length of the next string.
###
# i = j + 1: Move the index i past the # character.
###
# j = i + length: Calculate the end index of the current string
###
# array.append(s[i:j]): Append the substring from i to j to the list array
###
# i = j: Update i to j to start processing the next length indicator.