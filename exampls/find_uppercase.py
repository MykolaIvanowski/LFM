import time
import datetime
string_to_find_1 = "Learnpython"
string_to_find_2 = "learnpythoN"
string_to_find_3 = "learnPython"
string_to_find_4 = "learnpython"


def find_iterative(string_to_find):
    for i in range(len(string_to_find)):
        if string_to_find[i].isupper():
            return string_to_find[i]
    return "No uppercase character"


def find_recursive(string_to_find, inx=0):
    if string_to_find[inx].isupper():
        return string_to_find[inx]
    elif inx == len(string_to_find) - 1:
        return "No uppercase character"
    else:
        return find_recursive(string_to_find, inx+1)


t = time.time()
t1 = datetime.datetime.now()
print(find_iterative(string_to_find_1))
print(find_iterative(string_to_find_2))
print(find_iterative(string_to_find_3))
print(find_iterative(string_to_find_4))
print("time: {}".format(time.time()-t))
z = (datetime.datetime.now() - t1)
print("time: {}".format(datetime.datetime.now() - t1))

print("______________________________")

t = time.time()
t1 = datetime.datetime.now()
print(find_recursive(string_to_find_1))
print(find_recursive(string_to_find_2))
print(find_recursive(string_to_find_3))
print(find_recursive(string_to_find_4))
print("time: {}".format(time.time() - t))
print("time: {}".format(datetime.datetime.now() - t1))
