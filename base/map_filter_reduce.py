def func1(a):
    return a * 2


l1 = [1, 2, 3, 4, 5]
# map do something with elements
# зробить дію над елементом у масипі по заданій функції
m = map(func1, l1)  # return generator object
print(m)
print(list(m))


def funk2(a):
    return a % 2

# відфільтрує елементи у масиві по заданій функції
# filter do condition for element
f = filter(funk2, l1)  # return generator object
print(f)
print(list(f))


def funk3(a, b):
    return a + b


from functools import reduce

# виконає дію функції між усіма елементами масива і верне результат
r = reduce(funk3, l1)  # return results of function for all elements
print("reduce:", r)


# instead of reduce function (it is can be more readable)
number = 1
for i in l1:
    number = number * i
print(number)
