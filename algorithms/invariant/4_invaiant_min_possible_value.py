# low = min_possible
# high = max_possible
#
# while low < high:
#     mid = (low + high) // 2
#
#     if can(mid):
#         high = mid      # шукаємо менше
#     else:
#         low = mid + 1   # треба більше
#
# return low
#


def binary_search_on_answer(nums):

    def can(x):
        # Перевіряємо, чи можлива відповідь <= x
        # (логіка залежить від задачі)
        pass

    low = 0
    high = 10**18  # або інший максимум

    while low < high:
        mid = (low + high) // 2

        if can(mid):
            high = mid
        else:
            low = mid + 1

    return low