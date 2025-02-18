# You are given an integer n. Return all well-formed parentheses
# strings that you can generate with n pairs of parentheses.parentheses

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

from typing import List



class Solution:

    def generate_parentheses(self, n : int)-> List[str]:
        stack = []
        result = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                result.append(''.join(stack))
                return

            if open_n<n:
                stack.append('(')
                backtrack(open_n+1, closed_n)
                stack.pop()
            if closed_n<n:
                stack.append(')')
                backtrack(open_n,closed_n+1)
                stack.pop()
        backtrack(0,0)
        return result