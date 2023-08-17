class A:
    pass


class B:
    pass


class C(A, B):  # inheritance from left to right
    pass


print(C.__mro__)
print(C.mro())

