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
        # why use cache_dp - reduce time complexity, speeds up execution, avoids recomputing
        cache_dp = {len(s): 1} #  first entry help stop ih the end of depth in recursive call

        def dfs(i):
            # if in cache we already calculate it, also it is the end of depth,
            # in the end we have cache_dp[len(s)] - end it is return 1
            if i in cache_dp: # also avoid infinite cache
                return cache_dp[i]
            if s[i] =='0':
                # it is impossible to decode # valid to decode numbers  10,20 but not 01,02, 03 etc
                return 0
            # in first stage we achieve max depth in dfs
            # if 7 elements in s, we do to depth level 7, if s input '123456' then 0,1,2...6

            result = dfs(i+1) # result is from previous recursive level


            # we can calculate i+1 step only if i+1 less the the length of sequence
            # and if i (represent index for string) value under index is '1' or '2'
            # or value under index '2' and index + 1 in '0123456' because it cover 20-26 decoded latter
            if i + 1 < len(s)    and (s[i]=='1' or s[i]=='2' and s[i + 1]  in '0123456'):

                # why i+2 because we check s[i]and s[i+1] (in if state) and we need i+2
                # calculate possibility for decode 10-26 numbers
                result += dfs(i + 2)

            # store result  for calculate hove many decoding possibility we can have
            cache_dp[i] = result
            return result

        return dfs(0)

obj = SolutionTopDown()
r = obj.decode_ways('123456')
print(r)


class SolutionBottomUp:
    def decode_ways(self, s:str)-> int:
        cache_dp = {len(s): 1} # use cache for storing results

        # move in reversal order
        for i in range(len(s)-1, -1, -1):
            # '0' value can not be decoded so assign 0
            if s[i] ==  '0':
                cache_dp[i] = 0
            else:
                # if value under index not '0' we can decode it and decode in single number in letter (and result possibilities)
                cache_dp[i] = cache_dp[i+1]

            # check if we can use decoding fo 2 numbers
            # i+1<le(s) if we still in range
            # s[1]=='1' for decoding 10-19 numbers
            # s[i]=='2' and s[i+1]in '0123456' for decoding 20-26
            if i + 1 < len(s) and ( s[i] =='1' or s[i] == '2' and s[i+1] in '0123456'):
                # compute result for two numbers decoding in letter
                cache_dp[i] += cache_dp[i+2]
        # return result
        return cache_dp[0]

obj = SolutionBottomUp()
r = obj.decode_ways('123456')
print(r)
print('----')
class SolutionSpaceOptimized:
    def decode_way(self, s: str)-> int:
        #  dp2 number of decoding ways for 2 steps
        #  dp1 = number of decoding ways of one step and it is main result
        #  dp = it is like current update
        # use temporary value to store temp result
        dp = dp2 = 0  # tracking the last two computing values
        dp1 = 1

        # un loop in reverse order
        for i in range(len(s)-1, -1,-1):
            # if number is '0' we can not decode it
            if s[i] =='0':
                dp = 0
            else:
                # number is not a '0' so we put in temp result
                dp = dp1

            #  check if we can compute two numbers for decoding
            # i+1< len we in the renge
            # s[i] == '1' we in the range for numbers 10-19
            #  s[i] =='2' and s[i+1] in '0123456' we in range 20-16
            if i + 1 < len(s) and ( s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                #store result
                dp += dp2

            # shift variables
            dp, dp1, dp2 = 0, dp, dp1

        return dp1

obj = SolutionSpaceOptimized()
print(obj.decode_way('123456'))