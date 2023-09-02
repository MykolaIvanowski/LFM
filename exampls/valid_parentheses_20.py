
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



