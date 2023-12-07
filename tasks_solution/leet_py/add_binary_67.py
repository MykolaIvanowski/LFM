def add_binary(a,b):
    r = int(a,2) + int(b,2)
    return bin(r)[2:]

print(add_binary("11","1"))