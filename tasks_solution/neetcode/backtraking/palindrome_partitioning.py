# given string, find how much have palindromes in string
#
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]     # but not aba
#
# Input: s = "a"
# Output: [["a"]]
#
from typing import List


class Solution:
    def palindrome(self, s: str)-> List[List[str]]:
        result, part = [], []

        def dfs(index):
            if index >= len(s):
                result.append(part.copy())
                return

            for i in range(index, len(s)):
                if self.is_palindrome(s, index, i):
                    part.append(s[index: i + 1])
                    dfs(i + 1)
                    part.pop()

        dfs(0)
        return result

    def is_palindrome(self, s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1

        return True


obj  = Solution()
r = obj.palindrome('aab')
print(r)