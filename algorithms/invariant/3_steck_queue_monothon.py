```python
def monotonic_stack(nums, increasing=True):
    stack = []  # зберігаємо індекси

    for i, x in enumerate(nums):
        # якщо increasing=True → стек зростає
        # якщо False → стек спадає
        while stack and (
            (increasing and nums[stack[-1]] > x) or
            (not increasing and nums[stack[-1]] < x)
        ):
            stack.pop()

        stack.append(i)

    return stack


# pseudo for steck

# stack = []
#
# for i in range(n):
#     while stack and violates(stack.top, nums[i]):
#         stack.pop()
#     stack.push(i)
#
# dq = []
#


# pseudo for queue

# for i in range(n):
#     while dq and nums[dq[-1]] violates nums[i]:
#         dq.pop()
#
#     dq.append(i)
#
#     if dq[0] == i - k:
#         dq.popleft()
#
#     if i >= k - 1:
#         answer.append(nums[dq[0]])