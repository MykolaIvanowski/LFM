
def two_sum( nums, target):
# Step 1: Again, create a dictionary to store numbers and their indices.
    numMap = {}
    # Step 2: During iteration over the numbers, the complement is calculated for each number.
    for i, num in enumerate(nums):
        complement = target - num
        # Step 3: It checks if the complement exists in the dictionary. If so, the indices are returned.
        if complement in numMap:
            return [numMap[complement], i]
        # Step 4: Otherwise, the current number and its index are added to the dictionary.
        numMap[num] = i
# Step 5: If no pair sums up to the target, return an empty list.
    return []


print(two_sum([1,2,3,4,6,7,8],10))