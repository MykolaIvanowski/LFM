# You are given an array of integers temperatures where temperatures[i]
# represents the daily temperatures on the ith day.
#
# Return an array result where result[i] is the number of days
# after the ith day before a warmer temperature appears on a future day.
# If there is no day in the future where a warmer temperature will appear
# for the ith day, set result[i] to 0 instead.
from typing import List


class Solution:
    def daily_temperature(self, temperature: List[int])-> List[int]:
        res = [0] * temperature
        stack = []

        for i,t in enumerate(temperature):
            while stack and t > stack[-1][0]:
                stack_t, stack_i=stack.pop()
                res[stack_i] = i- stack_i
            stack.append((t,i))
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