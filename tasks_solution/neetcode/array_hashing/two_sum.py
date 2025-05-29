def two_sum(nums, target):
    p_map = {} # as we use hash and add value for every iteration space complexity is O(n)

    # we run through iteration only
    for i, n in enumerate(nums):
        diff=target - n
        if diff in p_map: #  search in hash map ant it search with O(1)
            return [p_map[diff],i]
        p_map[n] = i