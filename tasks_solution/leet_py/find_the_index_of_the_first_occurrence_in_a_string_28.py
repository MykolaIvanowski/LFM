
def find_the_index(haystack, needle):
    index = 0
    flag = True
    for h in range(len(haystack)):
        if haystack[h] == needle[0]:
            if len(needle) + h > len(haystack):
                return -1
            index = h
            for n in range(len(needle)):
                if haystack[h + n] != needle[n]:
                    flag = False
                    break
            if flag == False:
                flag = True
            else:
                return index
    return -1


r = find_the_index("hello", "ll")
print(r)


def alternative(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        # Check if substring matches needle
        if haystack[i:i + len(needle)] == needle:
            return i

    # If needle is not found
    return -1