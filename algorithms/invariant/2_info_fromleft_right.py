def solve(nums):
    acc = 0          # акумулятор (префікс)
    answer = 0       # відповідь

    for x in nums:
        acc += x                 # крок 1: оновлюємо префікс
        answer = max(answer, acc)  # крок 2: використовуємо префікс

    return answer

#prefix sum
def subarraySum(nums, k):
    prefix = 0
    seen = {0: 1}
    count = 0

    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count

#kadan
def maxSubArray(nums):
    best_ending = nums[0]
    best = nums[0]

    for x in nums[1:]:
        best_ending = max(x, best_ending + x)
        best = max(best, best_ending)

    return best


#prefix hash
def prefix_hash(s):
    base = 131
    h = 0
    hashes = []

    for ch in s:
        h = h * base + ord(ch)
        hashes.append(h)

    return hashes