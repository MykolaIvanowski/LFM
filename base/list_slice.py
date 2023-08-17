# https://stackoverflow.com/questions/509211/understanding-slice-notation
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array


# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items


# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])  # 9
print(a[1])  # 1

print(a[2:])  # [2, 3, 4, 5, 6, 7, 8, 9]
print(a[2: -1])  # [2, 3, 4, 5, 6, 7, 8]
print(a[2: 4])  # [2, 3]
print(a[-1: 2])  # []
print(a[-3:-1])  # [7, 8]


print(a[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(a[-1:5:-1])  # [9, 8, 7, 6]
print(a[1:5:-1])  # []

print(a[1::-1])  # [1, 0]
print(a[:-3:-1])  # [9, 8]
print(a[1::])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-3::-1])  # [7, 6, 5, 4, 3, 2, 1, 0]

bool