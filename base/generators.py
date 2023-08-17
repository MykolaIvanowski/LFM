
# symple one


def gen(array):
    for i in array:
        yield i * i
        print(f"value {i}")  # прінтане при другому використанні next


g = gen([1, 2, 3, 4])
print(gen([1, 2, 3, 4]))  # return generator object
print(next(g))
print(next(g))
print(next(g))

print("_"*20)


# певноп приклад ітератора (думав що генератора)
class Iterator:
    def __init__(self, max=0):  # max it is  built-in method
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= self.max:
            raise StopIteration  # якщо не рейзнути буде зациклення
        result = self.n * self.n
        self.n += 1
        return result


it = Iterator(5)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))  # Stopteration

print("_"*20)
print()


for i in Iterator(10):
    print(i)  # стоп ітрерайшен не рейзниться

print("_"*20)
print()

# it = Iterator(5)
# for i in range(10):
#     print(next(it))


def my_gen(max=0):
    n = 0
    while n < max:
        yield n * n
        n += 1


for i in my_gen(10):
    print(i)

