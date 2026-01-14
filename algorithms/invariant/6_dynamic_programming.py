
# dp = array of size n
# dp[0] = base_case
#
# for i in range(1, n):
#     dp[i] = transition(dp, i)
#
# return dp[n-1]


def dp_solve(nums):
    n = len(nums)
    dp = [0] * n

    dp[0] = base(nums[0])

    for i in range(1, n):
        dp[i] = transition(dp, nums, i)

    return dp[-1]