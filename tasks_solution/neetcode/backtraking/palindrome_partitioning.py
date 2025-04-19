# given string, find how much  palindromes in string
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
        result, part_result = [], [] # in part store some palindrome , part_result sometimes is stack

        def dfs(index):
            # achieved max depth and have palindrome
            if index >= len(s):
                print(part_result,'p res')
                result.append(part_result.copy())
                return

            # run cycle through given string
            for i in range(index, len(s)):

                # if we have palindrome then append to part_result
                if self.is_palindrome(s, index, i): # in this method check if s[index: i + 1] is palindrome
                    print(s[index:i+1])
                    # add to part result previous checked palindrome
                    part_result.append(s[index: i + 1])

                    # go deper in tree
                    dfs(i + 1)
                    print('--')
                    # remove last added palindrome
                    part_result.pop()
            print('end loop')
        dfs(0)
        return result

    # this method check if character of word is palindrome
    def is_palindrome(self, s, left, right):
        print(left,right, 'checker')
        # go through word if right > lett means we check all previous chars (letters)
        while left < right:
            if s[left] != s[right]: # symbols not mach return false
                return False
            left, right = left + 1, right - 1 # move two pointer to next possition

        return True


obj  = Solution()
r = obj.palindrome('aabb')
print(r)

#
# dfs(0)   [i=0, part_result = []]
# ├── Consider j=0:
# │    └── "a" (s[0:1]) is a palindrome.
# │         └── Append "a" → part_result = ["a"]
# │              └── Call dfs(1)  [i=1, part_result = ["a"]]
# │                   ├── Consider j=1:
# │                   │    └── "a" (s[1:2]) is a palindrome.
# │                   │         └── Append "a" → part_result = ["a", "a"]
# │                   │              └── Call dfs(2)  [i=2, part_result = ["a", "a"]]
# │                   │                   └── Consider j=2:
# │                   │                        └── "b" (s[2:3]) is a palindrome.
# │                   │                             └── Append "b" → part_result = ["a", "a", "b"]
# │                   │                                  └── Call dfs(3)  [i=3, part_result = ["a", "a", "b"]]
# │                   │                                       └── i == len(s) → **Add ["a", "a", "b"] to res**
# │                   │                             └── Backtrack: remove "b" → part = ["a", "a"]
# │                   └── Consider j=2:
# │                        └── "ab" (s[1:3]) is NOT a palindrome → Skip
# │                   └── Backtrack: remove "a" → part = ["a"]
# │              └── Backtrack: remove "a" → part = []
# ├── Consider j=1:
# │    └── "aa" (s[0:2]) is a palindrome.
# │         └── Append "aa" → part = ["aa"]
# │              └── Call dfs(2)  [i=2, part_result = ["aa"]]
# │                   └── Consider j=2:
# │                        └── "b" (s[2:3]) is a palindrome.
# │                             └── Append "b" → part_result = ["aa", "b"]
# │                                  └── Call dfs(3)  [i=3, part_result = ["aa", "b"]]
# │                                       └── i == len(s) → **Add ["aa", "b"] to res**
# │                             └── Backtrack: remove "b" → part = ["aa"]
# │              └── Backtrack: remove "aa" → part_result = []
# └── Consider j=2:
#      └── "aab" (s[0:3]) is NOT a palindrome → Skip