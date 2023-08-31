
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
list_2 = ["flower","flow","flight"]


print(longest_common_prefix(list_1))
print(longest_common_prefix(list_2))