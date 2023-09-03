
def longest_common_prefix(list_compare):
    size = len(list_compare)
    if size == 0:
        return ""
    if size == 1:
        return list_compare[0]
    list_compare.sort()

    end = min(len(list_compare[0]), len(list_compare[size - 1]))
    i = 0
    while (i < end and
           list_compare[0][i] == list_compare[size - 1][i]):
        i += 1

    prefix = list_compare[0][0: i]
    return prefix


list_1 = ["onew", "tweo", "three"]
list_2 = ["floweryerw","flow","flight1111","flirght", "flsdcwkko"]


print(longest_common_prefix(list_1))
print(longest_common_prefix(list_2))


def new_longest_common_prefix(strs):
    strs.sort()
    x = len(strs[0]) if len(strs[0]) < len(strs[-1]) else len(strs[-1])
    prefix_count = 0
    for i in range(x):
        if strs[0][i] == strs[-1][i]:
            prefix_count += 1
        else:
            break
    prefix = strs[0][0:prefix_count]
    return prefix


print(new_longest_common_prefix(list_2))
print(new_longest_common_prefix(list_1))
