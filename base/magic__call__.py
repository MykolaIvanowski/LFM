class A():

    def __call__(self, some):
        print(some)


a = A()
a('some value')  # some value beacouce of __call__