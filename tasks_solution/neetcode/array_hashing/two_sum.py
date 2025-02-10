def two_sum(nums, target):
    p_map = {}

    for i, n in enumerate(nums):
        diff=target - n
        if diff in p_map:
            return [p_map[diff],i]
        p_map[n] = i