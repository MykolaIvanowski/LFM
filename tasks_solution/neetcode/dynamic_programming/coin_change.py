# given integer array (coins) it represent coins can be used,
# given the integer  represent the target amount of money to achieve with given coins.
# return the fewest number of coins that you need to make up exact target amount
#
# Input: coins = [1,5,10], amount = 12
# Output: 3
#
# Input: coins = [2], amount = 3
# Output: -1
#
# Input: coins = [1], amount = 0
# Output: 0
#
from typing import List

class SolutionTopDown:
    def coin_change(self, coins: List[int], amount : int)-> int:
        # we will filed this cache with all numbers till amount {1: 1, 2:1, ...n:m}
        # end calculate lowest coin change
        cache_amount_coin = {} # we store sum and

        def dfs(amount):
            # edge case
            if amount==0:
                return 0
            # if amount in cache avoid additional calculation
            if amount in cache_amount_coin:
                return  cache_amount_coin[amount]

            result = 1e9 #  1 billion, hier number represent infinity

            # run loop for all coins to calculate all possibilities
            for coin in coins:
                # if amount - coin greater or equal to zero the we should go and calculate possibilities
                 if amount - coin >= 0:
                    # result represent infinity
                    # update with min result
                    # pass 23 we go through 23 till 1 then
                    # from 1 till 23 we calculate all possibilities for every coin and how much space it takes in amount
                    # after each recursive call we chose min and add to +1
                    # every recursive call for result example
                    # 23-5 =18 (it is + 1 to result)
                    # end alot of redundant calculation like 23-1=22( not add to result because of min function)
                    # 18-5 =13 (it is + 1 to result)
                    # and final 1-1 =0 (+ 1 to result)
                    result = min(result , 1 + dfs(amount-coin))
            cache_amount_coin[amount] = result

            return result
        min_coin = dfs(amount)
        # if result is infinity then return -1, there is no coins for result
        return -1 if min_coin >= 1e9 else min_coin


obj = SolutionTopDown()
res = obj.coin_change([1,2,5], 23)
print(res)


class SolutionBottomUp:
    def coin_change(self, coins: List[int], amount: int)->int:
        cache_coint = [amount+1]* (amount+1) # amount+ 1 array, amount+1 -represent infinity
        cache_coint[0] = 0


        # run loop from 1 till amount
        for a in range(1, amount+1):

            # for each number run all coins
            for c in coins:
                # if amount - count is less equal than zero
                if a-c>=0:
                    # iteration by iteration calculate all numbers and min coint count for this number
                    # and min possibility add to result
                    # coin 1 cache_coin[1-1=0] + 1, so for cache[1] = 1
                    # coin 2 cache_coin[2-1] +1 , so cache_coin[1] = 2
                    # coin 2 cache_coin[2-2] +1 , so chache_coin[2] = 1 update
                    # as you see it calculate all possible result for every coin end ashign lover result
                    cache_coint[a]= min(cache_coint[a], 1 + cache_coint[a-c])

        # if result not infinity (amount+1) return result
        return cache_coint[amount] if cache_coint!= amount+1 else -1


obj = SolutionBottomUp()
res = obj.coin_change([1,2,5], 23)
print(res)

# this solutions is not optimal as we calculate all possible result for every number in amount sequence
# but we need only for one for number for amount