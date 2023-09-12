def contains_duplicate(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

print(contains_duplicate([1,2,3,4,5,67,1]))


def contains_duplicate_b(nums):
    set_nums = set(nums)
    return len(set_nums) != len(nums)


print(contains_duplicate_b([1,2,3,4,5,67,1]))


def contains_duplicate_c(nums):
    from collections import defaultdict
    d = defaultdict(int)
    for i in nums:
        d[i] += 1
        if d[i] == 2:
            return True
    return False


print(contains_duplicate_c([1,2,3,4,5,67,1]))