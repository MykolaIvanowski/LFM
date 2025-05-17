# given n number,
# n representing numbers of steps to reach the top of staircase
# you can yse step 1 or tep 2
#
# Input: n = 2
# Output: 2     explanation : step 1 + step 1, step 2, there are two way to reach the top
#
# Input: n = 3
# Output: 3    explanation: step1 + step1+ step1; step2 + step1;step1+ step2, the are three way to reach the top
#
#

# space optimized
# solution based on idea:   index 0 1 2 3 4 5 6  7    - this we pass
#                    fibo numbers 1 1 2 3 5 8 13 21   - this we return
#  we need to run
class Solution:
    def climb_stairs(self, n: int)-> int:
        second_number, first_number = 1,1

        # as we start from step 1, we only need (n-1), it is like representation fibonaci sequence
        #  f(n-1) + f(n-2)
        for i in range(n-1):

            # save number into temp
            temp = second_number
            # the result is the sum of two numbers before
            second_number = second_number + first_number
            first_number = temp # reassign number to next variable

        return second_number

obj = Solution()
res = obj.climb_stairs(6)
print(res)

# solution based on fibonaci sequences
class SolutionTopDown:
    def climb_stairs(self, n : int)-> int:
        cache = [-1] * n

        def dfs(i):

            if i >= n : # base case if it is reach end of dfs (exceeding n)
                return i == n # return 1 if exactly at n  else return 0
            if cache[i] != -1:  # check if result is already computed
                return cache[i]  # if yes return result

            cache[i] = dfs(i+1) + dfs(i+2) # recursively computing result by fibo formula  f(n-1) + f(n-2)

            return cache[i] # return i element, during recursion it is from n-1 ->..., 5, 4, 3, 2, 1, 0

        return dfs(0)

obj = SolutionTopDown()
res = obj.climb_stairs(6)
print(res)

class SolutionBottomUp:
    def climb_stairs(self, n : int)->int:
        if n <= 2:  # step 1 -> result 1, step 2 -> result 2
            return n
        array = [0] * (n +1) # filed array with zeros
        array[1] , array[2] = 1,2 #  base cases for step 1, step 2; [0,1,2,0,0,...]

        # compute result, start from i = 3
        for i in range(3, n + 1):

            # compute i element based on sum of two previous elements,  index-1, index - 2, that's why we need  [0,1,2]
            array[i] = array[i-1] + array[i - 2]

        return array[n] # return n element, the last element

obj = SolutionBottomUp()
res = obj.climb_stairs(5)
print(res)