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
        # min used to calculate the value in stack
        self.min = float('inf')
        self.stack = []


    def push(self,x:int)->None:
        if not self.stack:
            # If the stack is empty, it appends 0 and sets min to x.
            self.stack.append(0)
            self.min = x
        else:
            # If the stack is not empty, it appends the difference x - self.min
            # to the stack.If x is smaller than the current min, it updates min to x.
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self)-> None:
        #  If the stack is not empty, it returns immediately.
        if not self.stack:
            return

        pop = self.stack.pop()

        #If the popped element is negative, it means the minimum value was changed when
        # it was pushed, so it adjusts the min accordingly.
        if pop < 0:
            self.min = self.min - pop


    def top(self)-> int:
        top = self.stack[-1]
        if top > 0:
            #If the top element is positive, it returns top + self.min
            return top + self.min
        else:
            # If the top element is not positive, it simply returns min.
            return self.min

    def getMin(self)-> int:
        return self.min


# Why Calculations Matter
# Efficiency: By storing differences instead of raw values,
# we can achieve constant-time complexity for push, pop, top, and getMin operations.
# This efficiency is crucial for applications requiring frequent stack operations.
#
# Space Optimization: Using differences allows us to avoid maintaining
# an additional stack to track minimum values. Instead,
# we leverage the existing stack to hold both element values
# and necessary information to track the minimum.

#
# Initialize MinStack
#         |
# +-------v-------+
# | self.min = ∞  |
# | self.stack = []|
# +---------------+
#
#     push(x)
#        |
# +------v------+
# | Is stack    |
# | empty?      |
# +------+------+
#        | No
#        v
# +------v------+
# | Append (x - |
# | min) to     |
# | stack       |
# +------v------+
#        | Yes
# +------v------+
# | Append 0    |
# | Set min to  |
# | x           |
# +-------------+
#
#     pop()
#        |
# +------v------+
# | Is stack    |
# | empty?      |
# +------v------+
#        | No
#        v
# +------v------+
# | pop =       |
# | stack.pop() |
# +------v------+
#        |
# +------v------+
# | Is pop < 0? |
# +------v------+
#        | Yes
#        v
# +------v------+
# | min = min - |
# | pop         |
# +-------------+
#
#     top()
#        |
# +------v------+
# | top =       |
# | stack[-1]   |
# +------v------+
#        |
# +------v------+
# | Is top > 0? |
# +------v------+
#        | Yes
#        v
# +------v------+
# | return top +|
# | min         |
# +------v------+
#        | No
#        v
# +------v------+
# | return min  |
# +-------------+
#
#     getMin()
#        |
# +------v------+
# | return min  |
# +-------------+


st = MinStack()
st.push(1)
st.push(3)
st.push(0)
print(st.stack, st.min)     # [0, 2, -1] 0
print(st.getMin())          # 0
st.pop()
print(st.top())             # 3
print(st.getMin())          # 1