def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        s = nums[left] + nums[right]

        if s == target:
            return left, right
        elif s < target:
            left += 1
        else:
            right -= 1



def longest_unique_substring(s):
    seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right
        best = max(best, right - left + 1)

    return best


def remove_duplicates(nums):
    slow = 0

    for fast in range(len(nums)):
        if fast == 0 or nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1

    return slow