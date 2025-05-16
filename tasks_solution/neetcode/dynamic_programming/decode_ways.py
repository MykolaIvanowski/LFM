# given string of number represent some decode letters
# some of the can heve several way to decode it
#  example '11' => AA or K
# find how many ways to decode have this string of integers
#
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Input: s = "01"
# Output: 0
# Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.
#


class SolutionTopDown:
    def decode_ways(self, s : str)-> int:
        # why use cache_dp - reduce time complexity, spedds up execution, avoids recomputing
        cache_dp = {len(s): 1}

        def dfs(i):
            if i in cache_dp:
                return cache_dp[i]
            if s[i] =='0':
                return 0

            result = dfs(i+1)
            if i + 1< len(s)    and (s[i]=='1' or s[i]=='2' and s[i + 1]  in '0123456'):
                result+= dfs(i + 2)
            cache_dp[i] = result
            return result
        r = dfs(0)
        return r

obj = SolutionTopDown()
r = obj.decode_ways('1249756')
print(r)


class SolutionBottomUp:
    def decode_ways(self, s:str)-> int:
        cache_dp = {len(s): 1}
        for i in range(len(s), -1, -1):
            if s[i] ==  '0':
                cache_dp[i] = 0
            else:
                cache_dp[i] = cache_dp[i+1]

            if i + 1 < len(s) and ( s[i] =='1' or s[i] == '2' or s[i+1] in '0123456'):
                cache_dp[i] += cache_dp[i+2]

            return cache_dp[0]


class SolutionSpaceOptimized:
    def decode_way(self, s: str)-> int:
        dp = dp2 = 0
        dp1 = 1
        for i in range(len(s), -1,-1):
            if s[i] =='0':
                dp =0
            else:
                dp = dp1

            if i + 1 < len(s) and ( s[i] == '1' or s[i] == '2' or s[i+1] in '0123456'):
                dp += dp2

            dp, dp1, dp2 = 0, dp, dp1

        return dp1

