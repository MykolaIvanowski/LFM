
def fibo_recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibo_recursive(n-1) + fibo_recursive(n - 2)


for i in range(1, 36):
    print(fibo_recursive(i))  # every next step take more time

print("finish ____ 1")

recursive_cache = {}


def fibo_recursive_cache(n):
    if n in recursive_cache:
        return recursive_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibo_recursive_cache(n - 1) + fibo_recursive_cache(n - 2)

    recursive_cache[n] = value
    return value


for i in range(1, 1001):
    print(f"{i} : {fibo_recursive_cache(i)}")


print("finish ____ 2")

