def remove_duplicates(nums):
    count = 0
    for i in range(len(nums)):
        if i < len(nums) - 2 and nums[i] == nums[i + 1]:
            continue
        nums[count] = nums[i]
        count += 1
    return count


print(remove_duplicates([1,1,2,2,3,3,4,4]))
