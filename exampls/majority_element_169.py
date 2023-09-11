def majority_element(nums):
    from collections import defaultdict
    major = len(nums) // 2
    d = defaultdict(int)
    for n in nums:
        d[n] += 1
    for v, n in d.items():
        if n > major:
            return v


majority_element([1,1,1,4,5])