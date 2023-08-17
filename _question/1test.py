# # sorted down
# l = [0, 1, 4, 7, 5, 25, 36, 49, 64, 81]
# a = sorted(l, reverse=True)
# print(a)


# protected
# class Employee:
#     def __init__(self, name, sal):
#         self._name=name # protected attribute
#         self._salary=sal # protected attribute
#  e1=Employee("Swati", 10000)
# >>> e1._salary
# 10000
# >>> e1._salary=20000
# >>> e1._salary
# 20000
#
# protecte
# class Employee:
# def __init__(self, name, sal):
#     self._name=name  # private attribute
#     self._salary=sal # private attribute
# >>> e1=Employee("Bill",10000)
# >>> e1._Employee__salary
# 10000
# >>> e1._Employee__salary=20000
# >>> e1._Employee__salary
# 20000

# def decorator_func(some_func):
#     # define another wrapper function which modifies some_func
#     def wrapper_func():
#         print("Wrapper function started")
#         some_func()
#         print("Wrapper function ended")
#
#     return wrapper_func
#
#
# # Wrapper function add something to the passed function and decorator returns the wrapper function
# def say_hello():
#     print("Hello")
#
#
# say_hello = decorator_func(say_hello)
# print(say_hello())
# # Or
# @decorator_func
# def say_hello():
#     print 'Hello'

# say_hello()
# Output:
#  Wrapper function started
#  Hello
#  Wrapper function ended
#

# def factorial (n):
#     f=1
#     for i in range(2,n+1):
#         f=f*i
#     return f
#
# print(factorial(5))

# def fibo(n):
#     a=0
#     b=1
#     l=[0, 1]
#     for i in range(0,n-1):
#         b=a+b
#         a=b-a
#         l.append(b)
#     return l
#
# print(fibo(5))

# def fibo(n):
#     l = [0, 1]
#     for i in range(0, n):
#         l.append(l[i] + l[i + 1])
#     return l
#
# print(fibo(5))


# enumerated list
# from collections import Counter
# m_list = ['a','a','a','b','b','b','b','c']
# print(Counter(m_list))
# dict((x,m_list.count(x)) for x in set(m_list))

# generator
# def generator_function():
#     for i in range(10):
#         yield i

# for item in generator_function():
#     print(item, end=" ")

# #filter
# number_list = [0, 1, 4, 7, 5, 25, 36, 49, 64, 81, -1]
# less_than_zero = list(filter(lambda x: x < 1, number_list))
# print(less_than_zero)

# reduce
# from functools import reduce
# items = [2, 2, 1, 1, 1, 2]
# double_sum = reduce(lambda x, y: x * y, items)
#
# print(double_sum)

# zip
# a = [1, 2, 3]
# b = "xyz"
# c = (None, True)
#
# res = list(zip(a, b, c))
# print(res)

# [(1, 'x', None), (2, 'y', True)]

# map
# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = list(map(int, old_list))
# print (new_list)
#
# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = list(map(lambda x: int(x), old_list)) #return int instead str
# print (new_list)

# map
# phone = input("phone: ")
# digits_map = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
# output = ""
# for i in phone:
#     output+=digits_map.get(i,5)+ " "
# print(output)


# total
# price = [1, 24, 17, 14, 9, 32, 2]
#
# total=0
# for item in price:
#     total=total+item
#
# print(total)

# F
# n=[5,2,5,2,2]
# for i in n:
#     output = ""
#     for a in range(i):
#         output+="x" #print (i*"*")
#     print(output)

# max/min number`
# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if  max > number :
#         max = number
#
# print(max)

# uniques
# numbers = [3, 6, 2, 8, 4, 10, 3, 8]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

#
#
# from collections import Counter

# text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
# eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
# nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
# officia deserunt mollit anim id est laborum."""
# def count_words(text):
#
#     new_list = text.split()
#     z = Counter(new_list)
#     new_list = text.split()
#     z = Counter(new_list)
#     list = [(k, v) for k, v in z.items()]

# list.sort(key=lambda x: x[1],reverse=True)
# list.reverse()
# return list

# numbers = "thdfngngff"
#
# for number in list(numbers):
#     uniques = []
#     if numbers.count(number) == 1:
#         uniques.append(number)
# print(uniques)

# print(count_words(text))

# text ='olleH dlroW'
#
# text1 = text.split()
# text1.join(reversed(text))
# print(text1)
# n = [5, 2, 5, 2, 2]
# gen = (x for x in n if x>2)
# print (gen)
#
# for x in gen:
# #     print(x)
# if "dag" > "ccc":
#     print("true")
# else:
#     print("false")
from functools import reduce

# items = [1, 2, 3, 4, 5]
# sum_all = reduce(lambda x, y: x * y, items)

# print(sum_all)

# foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

# print(list(filter(lambda x: x % 3 == 0, foo)))
# [18, 9, 24, 12, 27]

# print(list(map(lambda x: x * 2 + 10, foo)))
# [14, 46, 28, 54, 44, 58, 26, 34, 64]

# import itertools
# alist = [[1, 2], [3, 4]]
# print(list(itertools.chain.from_iterable(alist)))

# with open(r'x.txt', 'r') as f:  # w
#     data = f.read()
#     print(data)
# f.write("Hello")

# decorator
# def my_decorator(fun):
#     def my(*args, **kwargs):
#         print("Before")
#         fun(*args, **kwargs)
#         print("after")
#
#     return my
#
#
# @my_decorator
# def my_name(name):
#     print(f" hi {name}")
#

# print(my_name('ira'))


# global count
# COUNT = 0
#
#
# def increment():
#     global COUNT
#     COUNT = COUNT + 1
#
#
# increment()

# revert string
# print(COUNT)
#
# text = 'olleH dlroW'
# "".join(reversed(text))
# 'World Hello'

# l = "sehfiowjssgpow"
# a =[]
#
#
# def ret(a):
#     for i in list(l):
#         if l.count(i) == 1:
#             a.append(i)
#         return a[0]
#
#
# print(ret(l))

# g = {1: 1, 2: 6, 0: 8}
# # g1 = list(g.keys())
# # g2 = list(g.values())
# # print(dict(zip(g2, g1)))
# print(dict(zip(g.values(), g.keys())))

x = [9]
z = '',
if True and (not False or True) and x:
    print("A")
elif False or True and False:
    print("B")
elif True and z:
    print("C")
else:
    print("D")


def outer():
    x = "local"

    def inner():
        nonlocal x

    x = "nonlocal"
    print("inner:", x)

    inner()
    print("outer:", x)


outer()