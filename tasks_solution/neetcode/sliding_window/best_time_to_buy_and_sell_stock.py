# give an array with integers (represent prices)
# return maximum prifite when you buy low and sell high

# Input: prices = [10,1,5,6,7,1]
# Output: 6

from typing import List


class Solution:
    def max_profit(self, prices: List[int])-> int:
        l, r = 0, 1
        max_p = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit  = prices[r] - prices[l]
                max_p = max(max_p, profit)
            else:
                l = r
            r += 1

        return max_p


obj = Solution()
print(obj.max_profit([10,1,5,6,7,1]))