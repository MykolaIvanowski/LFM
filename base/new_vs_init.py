
class A:
    def __new__(cls):
        print("new A")

    def __init__(self):
        print("init A") # this doesn't print

a = A()
print("--------------------------------")


class A1:
    def __new__(cls):
        print("new A1")

class A2:

    def __init__(self):
        print("init A2") # this print


A1()
print("--------------------------------")
A2()

print("--------------------------------")

class C:
    def __new__(cls, *args, **kwargs):
        print("new C")
    def __init__(self):
        print("int C") # this doesn't print

C()
print("--------------------------------")

class B:
    def __new__(cls):
        print("new B")
        return "NEW B"

    def __init__(self):
        print("init B") # this doesn't print
        return "INIT B"


print(B())
print("--------------------------------")

class B1:
    def __new__(cls):
        print("new B1")
        return "NEW"

class B2:
    def __init__(self):
        print("int B2") # this isn't print
        return "INIT"


print(B1())
print("--------------------------------")
print(B2())
print("--------------------------------")


# What is the difference between __init__ and __new__?
#
# Ok, this is a FAQ but a good one. When you know this one, you know how python
# instantiates objects at the python level.
#
# So here is the thing. When __init__ executes, you get a first parameter
# that is the instance of your class. Normally, this first parameter is called self.
# Inside init you do all you want on this empty instance, normally set member vars.
#
# However, that instance has been created somehow. Who creates it?
#
# here is where __new__ enters the game. __new__ is a class method,
# that is, when executed, it gets passed the class. The objective of new is
# to create the instance that will then emerge as self into __init__.
#
# What is the default implementation of __new__? Generally,
# for a simple class (e.g. has no parents) it just calls object.__new__,
# something that creates a new instance of your class,
# but you can override it and do something before or after that.
# Technically, you could only use __new__, put all the stuff you have
# in __init__ just after the call to object.__new__() and be done with it.
# In practice, you prefer init because you don't want to repeat all the
# boilerplate to create the instance, which is mostly the same for all classes,
# and focus only on the unique part, that is, the initialization.
#
# When should you use __new__? There are some special cases where you want to,
# but in general, ask yourself the question: do I need to introduce
# this logic before the instance is created? if yes, then you need to override __new__.
# If the answer is no, then you should put it in __init__
