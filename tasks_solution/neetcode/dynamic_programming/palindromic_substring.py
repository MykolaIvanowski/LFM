# given s string, return the number of substring in this string
#
# Input: s = "abc"
# Output: 3
#
# Input: s = "aaa"
# Output: 6
#
#


class Solution:
    def palindromic_substring(self, s: str)->int:
            n, result = len(s), 0

            cache_dp =  [[False]* n for _ in range(n)] # create a 2d matrix n*n

            # run the loop in reverse order
            for i in range(n-1, -1, -1):
                # run loop in regular order
                # we go through each element i to n
                for j in range(i,n):

                    # s[i]==s[j] - palindrome must start and end with the same letter
                # j-i <=2 - substring with length less or equal to 3 is palindrome if firs and last chars is match (aba)
                #  cache_dp[i + 1][j - 1] - if inner substring is palindrome it is also palindrome (if s[i]==s[j])
                    if s[i]==s[j] and (j-i <= 2 or cache_dp[i + 1][j - 1]):
                        # find palindrome update palindrome cache
                        cache_dp[i][j]=True
                        # update result
                        result+=1

            return result

obj = Solution()
print(obj.palindromic_substring('qsedd'))