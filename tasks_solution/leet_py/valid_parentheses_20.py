
def is_valid(st):
    check = [("[", "]"), ("{", "}"), ("(", ")")]
    stack = []
    for i in st:
        if i == " ":
            continue
        if len(stack) > 0 and (stack[-1], i) in check:
            stack.pop()
        else:
            stack.append(i)
    return len(stack) == 0


print(is_valid("{}{}{}[][]()"))
print(is_valid("  {[}]   "))
print(is_valid("{[}]"))
print(is_valid(" ({[ ]} ) "))



def isValid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    dict = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for i in s:
        if i in dict.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i != dict[a]:
                return False
    return stack == []


print(isValid('({)}[]'))


