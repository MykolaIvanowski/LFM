def missing_number(nums):
    n = len(nums)
    for i in range(n):
        if i in nums:
            continue
        else:
            return i
    return len(nums)


print(missing_number([1,2,3,4,0]))
print(missing_number([1]))