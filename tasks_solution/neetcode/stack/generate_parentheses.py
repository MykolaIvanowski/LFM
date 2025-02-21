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
            # If open_n (number of open parentheses) and closed_n (number of
            # closed parentheses) are both equal to n, it means a valid combination has been
            # formed. This combination is joined into a string and appended to result
            if open_n == closed_n == n:
                result.append(''.join(stack))
                return

            if open_n<n:
                # If open_n is less than n, add an open parenthesis
                # '(' to the stack and call backtrack with open_n + 1
                stack.append('(')
                backtrack(open_n+1, closed_n)
                stack.pop()
            if closed_n<open_n:
                # If closed_n is less than open_n, add a closed
                # parenthesis ')' to the stack and call backtrack with closed_n + 1
                stack.append(')')
                backtrack(open_n,closed_n+1)
                stack.pop()
        backtrack(0,0)
        return result

#  why condition closed_n < open_n?

# Balanced Parentheses: To have a valid combination, every opening parenthesis
# ( must have a corresponding closing parenthesis ). If closed_n exceeds open_n,
# it would mean there are more closing parentheses than opening ones,
# resulting in an invalid sequence

# Ensures Validity: By checking closed_n < open_n, we make sure that at
# every step of the backtracking process, the generated sequence
# is still potentially valid and can lead to a correct combination of parentheses.

# visualization
# n = 2
# 1. Initial state: stack = [], open_n = 0, closed_n = 0
# 2. Add '(': stack = ['('], open_n = 1, closed_n = 0
# 3. Add '(': stack = ['(', '('], open_n = 2, closed_n = 0
# 4. Add ')': stack = ['(', '(', ')'], open_n = 2, closed_n = 1
# 5. Add ')': stack = ['(', '(', ')', ')'], open_n = 2, closed_n = 2 (valid)
#
# If we attempted to add a closing parenthesis when closed_n >= open_n:
# 1. Initial state: stack = [], open_n = 0, closed_n = 0
# 2. Add ')': invalid, as closed_n > open_n

sol = Solution()
print(sol.generate_parentheses(3))