#  given two string, find permutation s1 in s2, return true is s1 in s2
#
# Input: s1 = "abc", s2 = "lecabee"
# Output: true
#
# Input: s1 = "abc", s2 = "lecaabee"
# Output: false


class Solution:
    def permutation(self, s1: str, s2: str)-> bool:
        if len(s1)> len(s2):
            return False
        s1_quantity, s2_quantity = [0]*26, [0]*26

        # to filed arrays with number representations of character
        # minus number representation of a character and  +1
        # for s1 and s2
        for i in range(len(s1)):
            s1_quantity[ord(s1[i])-ord('a')]+=1
            s2_quantity[ord(s2[i])-ord('a')]+=1

        matches = 0
        for i in range(26):
            matches += 1 if s1_quantity[i] == s2_quantity[i] else 0


        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[right]) - ord('a')
            s2_quantity[index]+=1
            if s1_quantity[index] == s2_quantity[index]:
                matches += 1
            elif s1_quantity[index]+1 == s2_quantity[index]:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2_quantity[index] -= 1
            if s1_quantity[index] == s2_quantity[index]:
                matches +=1
            elif s1_quantity[index]-1 == s2_quantity[index]:
                matches -=1

            left+=1

        return matches==26

obj = Solution()
print(obj.permutation('abc', 'abrttiycab'))