

def isValid(s: str) -> bool:
    sequence = []
    for i in s:
        if i == '{' or '[' or '(' or '}'or')'or']':
           sequence.append(i)



    return True


print(isValid('{}'))