def single_number(nums):
    res = 0
    for i in nums:
        res = i ^ res
    return res

print(single_number([4,1,2,1,2]))


# solution if use additional memory space
def single_number(nums):
    dup = set()
    ones = []
    for n in nums:
        if n not in dup:
            ones.append(n)
            dup.add(n)
        else:
            ones.remove(n)
    return ones[0]