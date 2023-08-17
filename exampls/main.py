from sortedcontainers import SortedList
l = SortedList()
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    l = s[-1]   
    s = reversed(s)
    rome_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    r = 0

    for i in s:
        if rome_dict[l] > rome_dict[i]:
            r -= rome_dict[i]
        else:
            r += rome_dict[i]
            l = i
    return r


# print(romanToInt("MXIV"))
def isBadVersion(n):
    if n >3:
        return True
    else:
        return False

def firstBadVersion( n):
    """
    :type n: int
    :rtype: int
    """
    if not isBadVersion(n):
        return n
    check_l = n // 2
    check_r = n // 2 + 1
    checked = check_r

    while (True):
        call_r = isBadVersion(check_r)
        call_l = isBadVersion(check_l)
        checked //= 2
        if checked == 0:
            checked = 1
        if call_r is True and call_l is False:
            break
        elif not call_l and not call_r:
            check_r = check_r + checked
            check_l = check_l + checked
        else:
            check_r = check_r - checked
            check_l = check_l - checked

    return check_l+1

print(firstBadVersion(5))