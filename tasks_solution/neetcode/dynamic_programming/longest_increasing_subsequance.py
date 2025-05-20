# given array, retur longest subsequance from this array
# it is possible to delete some integer from this array to achieve the longest sequence
#  example [1,4,7,5] -> [1,4,5] (subsequence) -> return 3
#
# Input: nums = [9,1,4,2,3,3,7]
# Output: 4
#
# Input: nums = [0,3,1,3,2,3]
# Output: 4
#
#
from typing import List


class SolutionTopDown:
    def length_of_subsequence(self, nums: List[int])->int:
        n = len(nums)
        cache = [-1]*n

        def dfs(i):
            # if not -1 that mean we calculate this subsequence
            if cache[i] !=-1:
                return cache[i]
            subsequence = 1 # longest increasing subsequence
            # run loop from index +1  till the last index
            # why we check every possibility for  array
            for j in range(i + 1, n ):
                #if current value from index i less the values from j indexes

                if nums[i] < nums[j]: # this is skip larger int in sequence
                    # as we pass if we can add 1+ to dfs result, and chose max value
                    # recursive structure ensures the we move forward in the list and build
                    # the longest subsequence dynamically
                    # - we build for i index every subsequence possibility from j index
                    # - We add 1+ fs(j) because we are including nums[i] in the count
                    subsequence = max(subsequence, 1 + dfs(j))
            # we finish check for subsequence for current index store the result
            cache[i] = subsequence
            return subsequence

        # run dfs for every index
        return max(dfs(i) for i in range(n))

obj = SolutionTopDown()
print(obj.length_of_subsequence([1,3,5,2,4,6,3]))
# recursive tree
# nums = [10, 20, 15, 25, 30]
# dfs(0): 10
# ├── dfs(1): 20
# │      ├── dfs(3): 25
# │      │      └── dfs(4): 30
# │      └── dfs(4): 30
# ├── dfs(2): 15
# │      ├── dfs(3): 25
# │      │      └── dfs(4): 30
# │      └── dfs(4): 30
# ├── dfs(3): 25
# │      └── dfs(4): 30
# └── dfs(4): 30


class SolutionBottomUp:
    def length_of_subsequence(self, nums: List[int])-> int:
        subsequence = [1] * len(nums)# longest increasing subsequence

        # run loop for every number for opposite order
        for i in range(len(nums)-1, -1, -1):
            # for each number run loop in normal order
            # from i+1 run each index j again till end
            for j in range(i+1, len(nums)):
                # if we value less the current value under index i we will add it to sequence (actually count it)
                if nums[i]< nums[j]:
                    # for current i index we will count increasing larger subsequence (how much numbers it have)
                    # including current value under index i
                    # so we will count every possible longest increasing subsequence for every i index
                    subsequence[i] = max(subsequence[i],1+subsequence[j] )# +1 because we wont count i element
            print(subsequence)

        # just return max result
        return max(subsequence)

obj = SolutionBottomUp()
obj.length_of_subsequence([2,3,5,2,6,1,2,4,8,9])
#
# subsequence change after j loop finished
# given array [2, 3, 5, 2, 6, 1, 2, 4, 8, 9]
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#             [1, 1, 1, 1, 1, 1, 1, 1, 2, 1]
#             [1, 1, 1, 1, 1, 1, 1, 3, 2, 1]
#             [1, 1, 1, 1, 1, 1, 4, 3, 2, 1]
#             [1, 1, 1, 1, 1, 5, 4, 3, 2, 1]
#             [1, 1, 1, 1, 3, 5, 4, 3, 2, 1]
#             [1, 1, 1, 4, 3, 5, 4, 3, 2, 1]
#             [1, 1, 4, 4, 3, 5, 4, 3, 2, 1]
#             [1, 5, 4, 4, 3, 5, 4, 3, 2, 1]
#             [6, 5, 4, 4, 3, 5, 4, 3, 2, 1]
#