# You are given a string s consisting of the
# following characters: '(', ')', '{', '}', '[' and ']'.

# chek if it is in correct order

class Solution:
    def is_valid(self, s: str)-> bool:
        stack = []
        parentheses = {'}':'{',']':'[',')':'('}

        for p in s:
            # if character is a closed parentheses
            if p in parentheses:
                # Check if the stack is not empty
                # and the top of the stack is the corresponding opening bracket.
                if stack and stack[-1] == parentheses[p]:
                    stack.pop()
                else:
                    # if parentheses not in dictionary that means
                    # it have incorrect structure
                    return False
            else:
                # in stack adds only opening parentheses
                stack.append(p)
                
        # If the stack is empty, return True(all brackets are matched).
        # If the stack is not empty, return False(there are unmatched opening brackets).
        return True if not stack else False