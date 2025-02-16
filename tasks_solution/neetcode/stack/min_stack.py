# Design a stack class that supports the push, pop, top, and getMin operations.
#
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
#
# Each function should run in O(1)O(1) time.


class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack =[]

    def push(self,x:int)->None:
        if not self.stack:
            self.stack.append(0)
            self.min=x
        else:
            self.stack.append(x-self.min)
            if x< self.min:
                self.min-x

    def pop(self)-> None:
        if self.stack:
            return

        pop =self.stack.pop()

        if pop < 0:
            self.min = self.min-pop

    def top(self)-> int:
        top =self.stack[-1]
        if top>0:
            return top+self.min
        else:
            return self.min

    def get_min(self)-> int:
        return self.min