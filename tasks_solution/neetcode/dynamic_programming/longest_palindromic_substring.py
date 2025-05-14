# give a sequence of letters, find longest palindrome (substring)
#
# Input: s = "ababd"
# Output: "bab"
#
# Input: s = "abbc"
# Output: "bb"
#


class Solution:
    def longest_palindrome(self, s: str)-> str:
        sub_index,sub_len = 0, 0 # starting index and length palindrome
        n = len(s)

        # create matrix 2d array where columns = rows = len(s)
        dp = [[False]*n for _ in range(n)]

        # run loop in reversed order
        # i - row index
        for i in range(n-1,-1,-1):
            # j - column index
            for j in range(i, n):

                # palindrome detection
                # one chars is palindrome to itself
                # if two chars is equal they are palindrome
                # three symbols are palindrome if outer symbols are equal
                #
                # for mo then three symbols we use dp[i+1][j-1], to check if symbols mark as palindrome and
                # we expanded palindrome, check if it more symbols for palindrome
                if s[i] == s[j]  and (j-i <= 2 or dp[i+1][j-1]):
                    # mark it as a palindrome
                    dp[i][j] = True
                    # so we find palindrome
                    # check if founded palindrome is longer then previous longest palindrome
                    if sub_len <(j - i + 1):
                        # if this new palindrome longer
                        # then update new started index
                        sub_index = i
                        # and length for palindrome
                        sub_len = j - i + 1

        return s[sub_index: sub_len+sub_index]


obj = Solution()
print(obj.longest_palindrome('qrbasabkd'))


# Below is a visual table of the final dp matrix for "banana". (Cells are only filled for i <= j.)
# Here, T indicates that dp[i][j] was set to True (the substring s[i:j+1] is a palindrome), and F means it wasn’t:
# |          | b | a | n | a | n | a |
# |    i \ j | 0 | 1 | 2 | 3 | 4 | 5 |
# | b  0     | T | F | F | F | F | F |
# | a  1     |   | T | F | T | F | T |
# | n  2     |   |   | T | F | T | F |
# | a  3     |   |   |   | T | F | T |
# | n  4     |   |   |   |   | T | F |
# | a  5     |   |   |   |   |   | T |
#
# !!! Cells below the main diagonal remain unused since we're only checking substrings where i <= j
# But in cases where i > j, it would mean trying to define a substring where the "start" comes after the "end"—which isn't valid