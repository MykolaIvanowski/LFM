def foo():
    a = [0,1,1,1]
    for i in range(len(a)):
        print(i)  # print index

foo()
print('='*20)


# range(start, stop)
def foo():
    for i in range(1, 5):  # from 1 to 4 not include five
        print(i)

foo()
print('='*20)


# range(start, stop, step)
def foo():
    for i in range(0, 10, 2):
        print(i)

foo()

