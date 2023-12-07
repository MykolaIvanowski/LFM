def is_palindrome(s):
    import re
    s = re.sub('[^0-9a-zA-Z]+', '', s).lower()
    r = len(s)
    for i in range(len(s)):
        if i == r-1:
            return True
        if s[i] == s[r-1]:
            r -= 1
            continue
        return False
    return True



print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("0P"))
print(is_palindrome(" "))