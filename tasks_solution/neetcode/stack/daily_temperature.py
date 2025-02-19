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