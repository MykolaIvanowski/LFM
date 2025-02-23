# You are given an array of integers temperatures where temperatures[i]
# represents the daily temperatures on the ith day.
#
# Return an array result where result[i] is the number of days
# after the ith day before a warmer temperature appears on a future day.
# If there is no day in the future where a warmer temperature will appear
# for the ith day, set result[i] to 0 instead.

# Input: temperatures = [30,38,30,36,35,40,28]
#
# Output: [1,4,1,2,1,0,0]

from typing import List


class Solution:
    def daily_temperature(self, temperature: List[int])-> List[int]:
        res = [0] * temperature
        stack = []

        for i,t in enumerate(temperature):
            while stack and t > stack[-1][0]:
                #if temperature is higher than a temperature in last element in stack
                # then delete last element in stack
                stack_temperature, stack_index=stack.pop()
                # count difference between current index element and index added in stack
                # add as value to result array on position last stack index
                res[stack_index] = i - stack_index
            stack.append((t,i))  # add to stack index end temperature
        return res

# This algorithm efficiently calculates the number of
# days to wait for a warmer temperature by using a stack to keep track of
# indices of temperatures and updating the result array accordingly.


# Summary
# For each day, if the temperature is greater than the last recorded
# temperature in the stack, we pop from the stack, calculate the difference in days,
# and update the result array.
#
# If the temperature is not greater, we push the current temperature
# and its index onto the stack.
#
# This process continues until all temperatures are processed,
# giving us the required result array.