
class ClassName:
    def __init__(self):
        print("this init")
        print(self)

    def __new__(cls, *args, **kwargs):
        print("this new")
        print(cls)
        return super(ClassName, cls).__new__(cls, *args, **kwargs)




ClassName()
