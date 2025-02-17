# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
#
# Return the integer that represents the evaluation of the expression.
#
#     The operands may be integers or the results of other operations.
#     The operators include '+', '-', '*', and '/'.
#     Assume that division between integers always truncates toward zero.
from typing import  List


class Solution:
    def evaluate_RPN(self, tokens: List[str])->int:
        stack = []
        for t in tokens:
            if t == '+':
                #This pops the two top elements from the stack,
                # adds them, and pushes the result back.
                stack.append(stack.pop()+stack.pop())
            elif t == '-':
                #This pops the two top elements from the stack,
                # storing them in a and b respectively.This subtracts a from b
                a,b = stack.pop() , stack.pop()
                stack.append(b-a)
            elif t == '/':
                #This converts b and a to floats for division,
                # then converts the result back to an integer before pushing it back onto the stack
                a,b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            elif t == '*':
                #This pops the two top elements from the stack,
                # multiplies them, and pushes the result back onto the stack.
                stack.append(stack.pop()* stack.pop())
            else:
                stack.append(int(t))
        return stack[0]


#    tokens = ["2", "1", "+", "3", "*"]

#   Step	Token	Stack Transformation	            Stack State
#   1	    2	    Push val 2              	        [2]
#   2	    1	    Push val 1  	                    [2, 1]
#   3	    +   	Pop val 1, Pop val 2,Push val3	    [3]
#   4	    3	    Push val 3	                        [3, 3]
#   5	    *	    Pop val 3, Pop val 3, Push val 9	[9]