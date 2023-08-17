

def my_decorator(function):
    def inner(first_param):  # you can use *arks, **kwargs
        print("do some my_decorator")
        result = function(first_param)
        return result
    return inner


def my_dec(func):
    def inner(*args, **kwargs):
        print("do some my_dec")
        return func(*args, **kwargs)  # necessary need pass with *args, **kwargs
    return inner


@my_dec
@my_decorator
def my_function(value):
    print(f"print value {value}")
    return value


print(my_function("param"))
print("_" * 20)


def decorator_with_param(dec_value):
    def decorator(function):
        def inner(value):
            print(dec_value)
            print(f"value in decor : {value}")
            result = function(value)
            return result
        return inner
    return decorator


@decorator_with_param("argument for decorator")
def function_two(value):
    print("do some work %s".format(value))
    return value


print(function_two("some arguments"))
print("_" * 20)


from functools import wraps


def my_decorator_without_tools(param):
    """docstring without functools"""
    def wrapper(func):
        """"docstring without wrap"""
        def inner(*args, **kwargs):
            """docstring without inner"""
            return func(*args, **kwargs)
        return inner
    return wrapper


def my_decorator_func_tools(param):
    """docstring with functools"""
    def wrapper(func):
        """docstring wraps func with"""
        @wraps(func)  # без цього декоратора буде тянути невірні значення для help, __doc__, __name__
        def inner(*args, **kwargs):
            """docstring inner with"""
            return func(*args, **kwargs)
        return inner
    return wrapper


@my_decorator_without_tools("hi")
def foo_1():
    """docstring method foo one"""
    print("foo_1")


@my_decorator_func_tools("hi")
def foo_2():
    """docstring method foo two"""
    print("foo_2")


print(foo_1.__doc__)
print()
print(foo_2.__doc__)
print("-"*30)
print(foo_1.__name__)
print(foo_2.__name__)

print("help_1_"*7)
print()
print(help(foo_1))
print("_help_2"*7)
print()
print(help(foo_2))
