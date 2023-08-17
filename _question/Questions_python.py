# Polymorphism - possibility to change objects (classes/methods)
# Encapsulation - 1. private, 2. methods in methods
# Inheritance - parent/child classes
# Abstraction - API abstraction layer
class Example:
    def __init__(self):
        self._content = None # protected variable - class, subclasses
        self.__content = None  # private variable - class

class Cup:
    def __init__(self, color):
        self._color = color    # protected variable
        self.__content = None  # private variable
redCup = Cup("red")
redCup._Cup__content = "tea"
---------------------------------------------------------------------------------------------
# REST - Representational State Transfer (SOAP, XML-RPC)
# URI - resource identifier
# CONNECT, DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT, TRACE
# JSON or XML as the result

# GET /book/ — отримати список всіх книг
# GET /book/3/ — отримати книгу номер 3
# PUT /book/3 — змінити книгу (данні в тілі запита)
# PATCH /book/3 — змінити книгу (данные в теле запита), на відмвнно від PUT робить часткове оновлення даних
# POST /book/ – добавити книгу (данные в теле запита)
# DELETE /book/3 – видалити книгу

# CRUD - create read update delete

from eve import Eve
app = Eve()
if __name__ == '__main__':
    app.run()

# The API is now live, ready to be consumed:
# $ sudo apt install curl
# $ curl -i http://example.com/people
# HTTP/1.1 200 OK


---------------------------------------------------------------------------------------------
# Python:
# +
# easy to understand/use
# no extra compiling
# lots of built-in - lists, strings procedures
# lots of additional libs for all life cases
# all is objects - have flexible "changebility"
# -
# CPU-expencive: Memory & CPU usage, memory licks
# as all is wrapped/dynamic - not very quick
# Python програє в швидкості статично типізованим мовам (C/C++, Java, Go).


# Analogies - PyPy, Pyston, Jython, Cython
#
# Usage:
# Розробка веб аплікацій (django, flask).
# Аналіз данних і машинне навчання (пакеты scipy, scikit-question, pandas, numpy признанные мировым ученым сообществом).
# Введеня в програмування (pygame, turtle дляя дітей).
# Быстрое прототипирование идей в бизнесе за счёт обилия готовых библиотек, низкого порога вхождения в язык и высокой продуктивности программистов, пишущих на Python.
# Написание скриптов (сценариев) для автоматизации задач. Python по-умолчанию поставляется со всеми дистрибутивами unix-like систем и является отличной заменой Bash во всех смыслах.

---------------------------------------------------------------------------------------------
The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching. User has no control for it.

Python memory management is been divided into two parts.
    Stack memory
    Heap memory
Methods and variables are created in Stack memory.
Objects and instance variables values are created in Heap memory.
In stack memory - a stack frame is created whenever methods and variables are created.
These stacks frames are destroyed automaticaly whenever functions/methods returns.
Python has mechanism of Garbage collector, as soon as variables and functions returns, Garbage collector clear the dead objects.

y = x
if(id(x) == id(y)):
   print('x and y refer to the same object')

sys.getsizeof(x)

import copy
copy.deepcopy(dict)

# python -m memory_profiler memory-profile-me.py
import copy
import memory_profiler
@profile
def function():
    x = list(range(1000000))  # allocate a big list
    y = copy.deepcopy(x)
    del x
    return y
if __name__ == "__main__":
    function()

picklе очень плохо влияет на потребление памяти.

for _ in xrange(1000000)

import numpy
numpy.load('model.zip')

---------------------------------------------------------------------------------------------
#!/usr/bin/env python shebang == $PATH, $PYTHONPATH, if different python versions installed
# The only reason to set PYTHONPATH is to maintain directories of custom Python libraries that you do not want to install in the global default location (i.e., the site-packages directory).

# backslash - escape sequence
# license - Berkeley Software Distribution (BSD), GNU GPL

---------------------------------------------------------------------------------------------
import sys
print(sys.version)

python --version 
or
python -V

# Python 2
python -m SimpleHTTPServer

# Python 3
python -m http.server

cat file.json | python -m json.tool

python -m cProfile my_script.py

--cov

python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"

from pprint import pprint

In [18]: time.asctime()
Out[18]: 'Wed Nov 28 00:53:53 2018'

time -p python timing_functions.py

---------------------------------------------------------------------------------------------
# Mutable vs Immutable Objects in Python

Mutable - list, set, dict
Immutable - bool, int, float, tuple, str, frozenset

# Immutable objects doesn’t allow modification after creation

# Python Immutable Function Argument
def foo1(a):
    a += 1
    print(id(a))
    return a
x = 10
y = foo1(x)
print(id(y))
# id(y) == id(a)

# Mutable
list1 = [10, 20]
list2 = list1   # list1 and list2 point to same list object

---------------------------------------------------------------------------------------------
# for/while-else

# If 'break' - 'else' is not executed
for value in values:
    if value == 5:
        print "Found it!"
        break
else:
    print "Nowhere to be found. :-("
# If loop ends and no 'break' - 'else' is executed
while (Date != "January 1st"):
    time.sleep(1)
else:
    print("Happy new year!")

---------------------------------------------------------------------------------------------
# List comprehensions
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num) # Output: [2, 3, 4]

list_a = [1, 2, 3]
list_b = [2, 7]
different_num = [(a, b) for a in list_a for b in list_b if a != b]
print(different_num) # Output: [(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]

list_a = [1, 2, 3]
square_cube_list = [ [a**2, a**3] for a in list_a]
print(square_cube_list) # Output: [[1, 1], [4, 8], [9, 27]]

# Dict comprehensions
{v: k for k, v in some_dict.items()}

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
                   for k in mcase.keys()}
# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}

# Set comprehensions
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}

# Generator comprehensions
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Output: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
  print(x)
# Output: 0 3 6 9 12 15 18 21 24 27

---------------------------------------------------------------------------------------------
# zip/map/filter/lambda/any

# zip, map, filter - iterators.

# lambda
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]

# zip
list_a = [1, 2, 3]
list_b = [4, 5, 6]
zipped = zip(list_a, list_b) # Output: [(1, 4), (2, 5), (3, 6)]
len(zipped) # Output: 3
zipped[0] # Output: (1, 4)
list_c = list(zipped) #Output: [(1, 4), (2, 5), (3, 6)]
list_d = list(zipped) # Output []... Output is empty list becuase by the above statement zip got exhausted.

# parallel sorting
data = zip(list1, list2)
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))

# map
# Neither we can access the elements of the map object with index
# nor we can use len() to find the length of the map object
map(lambda x : x*2, [1, 2, 3, 4]) #Output [2, 4, 6, 8]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
map(lambda x : x['name'], dict_a) # Output: ['python', 'java']
map(lambda x : x['points']*10,  dict_a) # Output: [100, 80]
map(lambda x : x['name'] == "python", dict_a) # Output: [True, False]

# filter
a = [1, 2, 3, 4, 5, 6]
filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]

# any(iterable)
# The any() method takes an iterable (list, string, dictionary etc.) in Python.
When 	                               Return Value
All values are true 	                True
All values are false 	                False
One value is true (others are false) 	True
One value is false (others are true) 	True
Empty Iterable 	                        False

l = [1, 3, 4, 0]
print(any(l)) # Output is True
---------------------------------------------------------------------------------------------
# iterators
>>> x = iter([1, 2, 3])
>>> x
<listiterator object at 0x1004ca850>
>>> x.next()
1
>>> x.next()
2
>>> x.next()
3
>>> x.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

# Here is an iterator that works like reversed iterator.
class reverse_iter:
    def __init__(self, n):
        n.reverse()        
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        while self.i < len(self.n):
            i = self.i
            self.i += 1
            return self.n[i]
        else:
            raise StopIteration()
x = reverse_iter([1, 2, 3])
In [7]: x.next()
Out[7]: 3
In [8]: x.next()
Out[8]: 2
In [9]: x.next()
Out[9]: 1
In [10]: x.next()
StopIteration                             Traceback (most recent call last)

# Here is an iterator that works like built-in xrange function.
class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
>>> y = yrange(3)
>>> y.next()
0
>>> y.next()
1
>>> y.next()
2
>>> y.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 14, in next
StopIteration

>>> list(yrange(5))
[0, 1, 2, 3, 4]
>>> sum(yrange(5))
10

---------------------------------------------------------------------------------------------
# generators

# Generators simplifies creation of iterators.
# A generator is a function that produces a sequence of results instead of a single value.
# Each time the yield statement is executed the function generates a new value.
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
>>> y = yrange(3)
>>> y
<generator object yrange at 0x401f30>
>>> y.next()
0
>>> y.next()
1
>>> y.next()
2
>>> y.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

# When next method is called for the first time, the function starts executing until it reaches yield statement.
>>> def foo():
...     print "begin"
...     for i in range(3):
...         print "before yield", i
...         yield i
...         print "after yield", i
...     print "end"
...
>>> f = foo()
>>> f.next()
begin
before yield 0
0
>>> f.next()
after yield 0
before yield 1
1
>>> f.next()
after yield 1
before yield 2
2
>>> f.next()
after yield 2
end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>

# Example:
def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    """Returns first n values from the given sequence."""
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(seq.next())
    except StopIteration:
        pass
    return result

print take(5, squares()) # prints [1, 4, 9, 16, 25]

# Generator Expressions
In [24]: [x*x for x in range(10)]
Out[24]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

In [25]: (x*x for x in range(10))
Out[25]: <generator object <genexpr> at 0x7f18b44598c0>

>>> sum(x*x for x in range(10))
285

# Pythogorian Triplet (x*x + y*y == z*z)
>>> pyt = ((x, y, z) for z in integers() for y in xrange(1, z) for x in range(1, y) if x*x + y*y == z*z)
>>> take(10, pyt)
[(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (15, 20, 25), (7, 24, 25), (10, 24, 26), (20, 21, 29)]

# Reading files
def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print(line)

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

In [75]: main("lines", ["/home/probook/Документи/NewWork/Questions_pytest.py", "/home/probook/Документи/NewWork/Questions_python.py"])
"# decorators"

# Itertools
# chain – chains multiple iterators together.
>>> it1 = iter([1, 2, 3])
>>> it2 = iter([4, 5, 6])
>>> itertools.chain(it1, it2)
<itertools.chain at 0x7f18b445a4d0>
>>> list(itertools.chain(it1, it2))
[1, 2, 3, 4, 5, 6]

# izip – iterable version of zip
In [37]: a = itertools.izip(["a", "b", "c"], [1, 2, 3])
    ...: a.next()
    ...:  
Out[37]: ('a', 1)

# enumerate
>>> list(enumerate(["a", "b", "c"])
[(0, "a"), (1, "b"), (2, "c")]

---------------------------------------------------------------------------------------------
# decorators

# A decorator may involve entire classes if they have __call__(self) method.

def decorator_func(some_func):
  # define another wrapper function which modifies some_func
  def wrapper_func():
    print("Wrapper function started")
    some_func()
    print("Wrapper function ended")
  return wrapper_func # Wrapper function add something to the passed function and decorator returns the wrapper function
    
def say_hello():
  print ("Hello")
say_hello = decorator_func(say_hello)
# Or
@decorator_func
def say_hello():
    print 'Hello'

say_hello()
# Output:
#  Wrapper function started
#  Hello
#  Wrapper function started

def decorator_func(say_hello_func):
  def wrapper_func(hello_var, world_var):
    if not hello_var:
      hello_var = "Hello"
    if not world_var:
      world_var = "World"
    return say_hello_func(hello_var, world_var)
  return wrapper_func
@decorator_func
def say_hello(hello_var, world_var):
  print hello_var + ", " + world_var
say_hello("Hello", "")
# Output:
#  Hello, World

# @wraps - to have proper function name, docstring, arguments list, etc. saved, not the "decorator_name"
from functools import wraps
def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated
@decorator_name
def func():
    return("Function is running")
can_run = True
print(func())
# Output: Function is running
can_run = False
print(func())
# Output: Function will not run
print(func.__name__)
# Output: func

# Time decorator
import time
from functools import wraps

def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ("Total time running %s: %s seconds" %
               (function.func_name, str(t1-t0))
               )
        return result
    return function_timer

@fn_timer
def random_sort(n):
    return sorted([random.random() for i in range(n)])
if __name__ == "__main__":
 random_sort(2000000)
---------------------------------------------------------------------------------------------
# property

# It’s preferable to use Duck Typing (type checking be deferred to run-time,
# and is implemented by means of dynamic typing or reflection) rather than inspecting the type of an object.
# Python code to illustrate duck typing 
  
class User(object): 
    def __init__(self, firstname): 
        self.firstname = firstname
    @property
    def name(self): 
        return self.firstname 
  
class Animal(object): 
    pass
  
class Fox(Animal): 
    name = "Fox"
  
class Bear(Animal): 
    name = "Bear"
  
# Use the .name attribute (or property) regardless of the type 
for a in [User("Geeksforgeeks"), Fox(), Bear()]: 
    print(a.name) 

Output:

Geeksforgeeks
Fox
Bear

# getter
@property
def x(self):
    return self._x
# is equivalent to
def getx(self):
    return self._x
x = property(getx)

# getter/setter/deleter
class C(object):
    def __init__(self):
        self._x = None
    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x
#Is the same as:
class C(object):
    def __init__(self):
        self._x = None
    def _x_get(self):
        return self._x
    def _x_set(self, value):
        self._x = value
    def _x_del(self):
        del self._x
    x = property(_x_get, _x_set, _x_del, 
                    doc="I'm the 'x' property.")
# Example:
class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents
    # Getter and setter for dollars...
    @property
    def dollars(self):
        return self.total_cents // 100
    @dollars.setter
    def dollars(self, new_dollars):
        self.total_cents = 100 * new_dollars + self.cents
    # And the getter and setter for cents.
    @property
    def cents(self):
        return self.total_cents % 100
    @cents.setter
    def cents(self, new_cents):
        self.total_cents = 100 * self.dollars + new_cents

# when we now call from our library
money = Money(27, 12)
print("I have {} dollar and {} cents.".format(money.dollars, money.cents))
# prints: I have 27 dollar and 12 cents.

money.dollars += 2
print("I have {} dollar and {} cents.".format(money.dollars, money.cents))
# prints: I have 29 dollar and 12 cents.

money.cents += 10
print("I have {} dollar and {} cents.".format(money.dollars, money.cents))
# prints: I have 29 dollar and 22 cents.

---------------------------------------------------------------------------------------------
# try/except

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong") 

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

try:
    if os.path.isfile(file_path):
        os.unlink(file_path)
except TGException as err:
    logging.error(err)

class TGException(PyNetTestException):
    """@brief Base class for TG exceptions"""
    pass

# myexception.py
import exceptions
class CustomException(exceptions.Exception):
    def __init__(self):
        return
    def __str__(self):
        print "","Custom exception occurred!"

if __name__ == "__main__":
    raise CustomException

    BaseException - базовое исключение, от которого берут начало все остальные.
        SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
        KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
        GeneratorExit - порождается при вызове метода close объекта generator.
        Exception - а вот тут уже заканчиваются полностью системные исключения (которые лучше не трогать) и начинаются обыкновенные, с которыми можно работать.
            StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
            ArithmeticError - арифметическая ошибка.
                FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике встречается нечасто.
                OverflowError - возникает, когда результат арифметической операции слишком велик для представления. Не появляется при обычной работе с целыми числами (так как python поддерживает длинные числа), но может возникать в некоторых других случаях.
                ZeroDivisionError - деление на ноль.
            AssertionError - выражение в функции assert ложно.
            AttributeError - объект не имеет данного атрибута (значения или метода).
            BufferError - операция, связанная с буфером, не может быть выполнена.
            EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
            ImportError - не удалось импортирование модуля или его атрибута.
            LookupError - некорректный индекс или ключ.
                IndexError - индекс не входит в диапазон элементов.
                KeyError - несуществующий ключ (в словаре, множестве или другом объекте). 
            MemoryError - недостаточно памяти.
            NameError - не найдено переменной с таким именем.
                UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее. 
            OSError - ошибка, связанная с системой.
                BlockingIOError
                ChildProcessError - неудача при операции с дочерним процессом.
                ConnectionError - базовый класс для исключений, связанных с подключениями.
                    BrokenPipeError
                    ConnectionAbortedError
                    ConnectionRefusedError
                    ConnectionResetError
                FileExistsError - попытка создания файла или директории, которая уже существует.
                FileNotFoundError - файл или директория не существует.
                InterruptedError - системный вызов прерван входящим сигналом.
                IsADirectoryError - ожидался файл, но это директория.
                NotADirectoryError - ожидалась директория, но это файл.
                PermissionError - не хватает прав доступа.
                ProcessLookupError - указанного процесса не существует.
                TimeoutError - закончилось время ожидания.
            ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
            RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
            NotImplementedError - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
            SyntaxError - синтаксическая ошибка.
                IndentationError - неправильные отступы.
                    TabError - смешивание в отступах табуляции и пробелов.
            SystemError - внутренняя ошибка.
            TypeError - операция применена к объекту несоответствующего типа.
            ValueError - функция получает аргумент правильного типа, но некорректного значения.
            UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
                UnicodeEncodeError - исключение, связанное с кодированием unicode.
                UnicodeDecodeError - исключение, связанное с декодированием unicode.
                UnicodeTranslateError - исключение, связанное с переводом unicode.
            Warning - предупреждение.

---------------------------------------------------------------------------------------------
# Context managers (PEP 343)

$ ulimit -n # limit of opened context managers in system

with something_that_returns_a_context_manager() as my_resource:
    do_something(my_resource)
    ...
    print('done using my_resource')

def test_02_1(self):
    with pytest.raises(ZeroDivisionError):
        my_var = 1 / 0

# After "with" statement has executed, the file object in f will have been automatically closed, even if the for loop raised an exception part-way through the block.
with open('what_are_context_managers.txt', 'r') as infile:
    for line in infile:
        print('> {}'.format(line))

# A string, define which mode you want to open the file in:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exist
# In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

# Create context manager - define a class that contains two special methods: __enter__() and __exit__().
class File():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
files = []
for _ in range(10000):
    with File('foo.txt', 'w') as infile:
        infile.write('foo')
        files.append(infile)

# Lock objects in threading are context managers too.
from threading import Lock
lock = Lock()
def do_something_dangerous():
    with lock:
        raise Exception('oops I forgot this code could raise exceptions')
try:
    do_something_dangerous()
except:
    print('Got an exception')
lock.acquire()
print('Got here')

# context manager lib
from contextlib import contextmanager
@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()
files = []
for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)
for f in files:
    if not f.closed:
        print('not closed')

from contextlib import contextmanager
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)
>>> with tag("h1"):
...    print("foo")
...
<h1>
foo
</h1>

from contextlib import ContextDecorator
class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self
    def __exit__(self, *exc):
        print('</p>')
        return False
@makeparagraph()
def emit_html():
    print('Here is some non-HTML')
emit_html()
# The output will be:
<p>
Here is some non-HTML
</p>

---------------------------------------------------------------------------------------------
# type and isinstance in Python

type(object)
type(name, bases, dict)

# If you need to check type of an object, it is recommended to use Python isinstance() function instead.
# It’s because isinstance() function also checks if the given object is an instance of the subclass.

#python code to illustrate the lack of 
#support for inheritance in type() 
  
class MyDict(dict): 
    """A normal dict, that is always created with an "initial" key"""
    def __init__(self): 
        self["initial"] = "some data"
  
d = MyDict() 
print(type(d) == dict) 
print(type(d) == MyDict) 
  
d = dict() 
print(type(d) == dict) 
print(type(d) == MyDict) 

Output:

False
True
True
False

#python code to show isintance() support 
#inheritance 
class MyDict(dict): 
    """A normal dict, that is always created with an "initial" key"""
    def __init__(self): 
        self["initial"] = "some data"
  
d = MyDict() 
print(isinstance(d, MyDict)) 
print(isinstance(d, dict)) 
  
d = dict() 
print(isinstance(d, MyDict)) 
print(isinstance(d, dict)) 

Output:

True
True
False
True

---------------------------------------------------------------------------------------------
# Metaprogramming

# type is the built-in metaclass Python uses. To change the behavior of classes in Python (like the behavior of SomeClass), we can define a custom metaclass by inheriting the type metaclass.
class SomeClass:
...     pass
>>> some_object = SomeClass()
>>> type(some_obj)
<__main__.SomeClass instance at 0x7f8de4432f80>
>>> import inspect
>>>inspect.isclass(SomeClass)
True
>>>inspect.isclass(some_object)
False
>>>inspect.isclass(type(some_object))
True
>>> type(SomeClass)
<type 'classobj'>>>>
inspect.isclass(type(SomeClass))
True
>>> isinstance(some_obj,SomeClass)
True
>>> isinstance(SomeClass, type)
True

# The namespaces of classes are layered as dictionaries. For example:
>>> class SomeClass:
...     class_var = 1
...     def __init__(self):
...         self.some_var = 'Some value'
>>> SomeClass.__dict__
{'__doc__': None,
 '__init__': <function __main__.__init__>,
 '__module__': '__main__',
 'class_var': 1}
>>> s = SomeClass()
>>> s.__dict__
{'some_var': 'Some value'}

# The default metaclass is called "type". The arguments when invoking type are the name of the class, a list of base classes, and a dictionary giving the namespace for the class (all the fields and methods):
class C: pass
# is:
C = type('C', (), {})

# Example:
class ParentClass:
    pass
class SomeClass(ParentClass):
    some_var = 5
    def some_function(self):
        print("Hello!")
# Equivalents to:
def some_function(self):
    print("Hello")
ParentClass = type('ParentClass', (), {})
SomeClass = type('SomeClass',
                 [ParentClass],
                 {'some_function': some_function,
                  'some_var':5})
# Decorators: A common example of metaprogramming in Python
@some_decorator
def some_func(*args, **kwargs):
    pass

# Metaprogramming/Change var name to snake case
def camel_to_snake(name):
    """
    A function that converts camelCase to snake_case.
    Referred from: https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    """
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
class SnakeCaseMetaclass(type):
    def __new__(snakecase_metaclass, future_class_name,
                future_class_parents, future_class_attr):
        snakecase_attrs = {}
        for name, val in future_class_attr.items():
            snakecase_attrs[camel_to_snake(name)] = val
        return type(future_class_name, future_class_parents,
                    snakecase_attrs)
>>> class SomeClass(metaclass=SnakeCaseMetaclass):
...     camelCaseVar = 5
>>> SomeClass.camelCaseVar
AttributeError: type object 'SomeClass' has no attribute 'camelCaseVar'
>>> SomeClass.camel_case_var
5

# Metaprogramming/MyList.py
def howdy(self, you):
    print("Howdy, " + you)
MyList = type('MyList', (list,), dict(x=42, howdy=howdy))
ml = MyList()
ml.append("Camembert")
print(ml)
print(ml.x)
ml.howdy("John")
print(ml.__class__.__class__)
""" Output:
['Camembert']
42
Howdy, John
"""

# Metaprogramming/SimpleMeta1.py
# Two-step metaclass creation in Python 2.x
class SimpleMeta1(type):
    def __init__(cls, name, bases, nmspc):
        super(SimpleMeta1, cls).__init__(name, bases, nmspc)
        cls.uses_metaclass = lambda self : "Yes!"
class Simple1(object):
    __metaclass__ = SimpleMeta1
    def foo(self): pass
    @staticmethod
    def bar(): pass
simple = Simple1()
print([m for m in dir(simple) if not m.startswith('__')])
# A new method has been injected by the metaclass:
print simple.uses_metaclass()
""" Output:
['bar', 'foo', 'uses_metaclass']
Yes!
"""

# Metaprogramming/SimpleMeta2.py
# Combining the steps for metaclass creation in Python 2.x
class Simple2(object):
    class __metaclass__(type):
        def __init__(cls, name, bases, nmspc):
            # This won't work:
            # super(__metaclass__, cls).__init__(name, bases, nmspc)
            # Less-flexible specific call:
            type.__init__(cls, name, bases, nmspc)
            cls.uses_metaclass = lambda self : "Yes!"
class Simple3(Simple2): pass
simple = Simple3()
print simple.uses_metaclass()
""" Output:
Yes!
"""

# Metaprogramming/SimpleMeta3.py
# A function for __metaclass__ in Python 2.x
class Simple4(object):
    def __metaclass__(name, bases, nmspc):
        cls = type(name, bases, nmspc)
        cls.uses_metaclass = lambda self : "Yes!"
        return cls
simple = Simple4()
print simple.uses_metaclass()
""" Output:
Yes!
"""

# The main reason to use metaclasses over having all of this logic defined in the class definitions itself is to avoid the code repetition throughout the codebase (Don’t Repeat Yourself — DRY).

---------------------------------------------------------------------------------------------
# Abstract base classes
# Classes that are only meant to be inherited from and not to be instantiated.
from abc import ABCMeta, abstractmethod
 
class Vehicle(metaclass=ABCMeta):
    @abstractmethod
    def refill_tank(self, litres):
        pass
    @abstractproperty
    def tires(self):
        pass

NotImplementedError

class Vehicle(Transport):
    __metaclass__ = ABCMeta    
    @abstractmethod
    def refill_tank(self, litres):
        pass
    @abstractproperty
    def tires(self):
        pass

# Register subclass as a “virtual subclass” of this ABC.
class Foo(object):
    def __getitem__(self, index):
        ...
    def __len__(self):
        ...
    def get_iterator(self):
        return iter(self)

class MyIterable:
    __metaclass__ = ABCMeta
    @abstractmethod
    def __iter__(self):
        while False:
            yield None
    def get_iterator(self):
        return self.__iter__()
    @classmethod
    def __subclasshook__(cls, C):
        if cls is MyIterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

MyIterable.register(Foo)

---------------------------------------------------------------------------------------------
# Handlers
handlers = {}
 
class CustomMetaclass(type):
    def __new__(meta, name, bases, attrs):
        cls = type.__new__(meta, name, bases, attrs)
        for ext in attrs["files"]:
            handlers[ext] = cls
        return cls
 
class Handler(metaclass=CustomMetaclass):
    formats = []
    # common stuff for all kinds of file format handlers

class ImageHandler(Handler):
    formats = ["jpeg", "png"]
 
class AudioHandler(Handler):
    formats = ["mp3", "wav"]
>>> handlers
{'mp3': __main__.AudioHandler,
 'jpeg': __main__.ImageHandler,
 'png': __main__.ImageHandler,
 'wav': __main__.AudioHandler}

---------------------------------------------------------------------------------------------
# __init__
# The __init__() method gets called for you when you instantiate a class:
class A:
     def __init__(self, x):
          self.x = x
class B(A):
     def __init__(self, x, y):
          A.__init__(self, x)
          self.y = y
# Note, the above call can also be written using super:
class B(A):
     def __init__(self, x, y):
          super().__init__(x)
          self.y = y

---------------------------------------------------------------------------------------------
# classmethod vs staticmethod
class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)
    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)
    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x
a=A()
print(a.foo)
"<bound method A.foo of <__main__.A object at 0xb7d52f0c>>"
# With a.class_foo, a is not bound to class_foo, rather the class A is bound to class_foo.
print(a.class_foo)
"<bound method type.class_foo of <class '__main__.A'>>"
# Here, with a staticmethod, even though it is a method, a.static_foo just returns a good 'ole function with no arguments bound.
print(a.static_foo)
"<function static_foo at 0xb7d479cc>"

---------------------------------------------------------------------------------------------
# Serialization

# Data serialization is the concept of converting structured data into a format that allows it to be shared or stored in such a way
# that its original structure to be recovered. In some cases, the secondary intention of data serialization is to minimize the size
# of the serialized data which then minimizes disk space or bandwidth requirements.

## marshal

# The marshal module is not intended to be secure against erroneous or maliciously constructed data.
# Never unmarshal data received from an untrusted or unauthenticated source. 
import marshal
marshal_string = marshal.dumps([1, 2, 3, "a", "b", "c"])
print(marshal.loads(marshal_string))
# prints: [1, 2, 3, 'a', 'b', 'c'
print(marshal.loads(marshal_string))

# The pickle module keeps track of the objects it has already serialized, so that later references to the same object won’t be serialized again. marshal doesn’t do this.
# marshal cannot be used to serialize user-defined classes and their instances. pickle can save and restore class instances transparently, however the class definition must be importable and live in the same module as when the object was stored.
# The marshal serialization format is not guaranteed to be portable across Python versions. Because its primary job in life is to support .pyc files, the Python implementers reserve the right to change the serialization format in non-backwards compatible ways should the need arise. The pickle serialization format is guaranteed to be backwards compatible across Python releases.

## pickle

import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))
# prints: [1, 2, 3, 'a', 'b', 'c']
print(pickle.loads(pickled_string))

import pickle
dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
filename = 'dogs'
outfile = open(filename,'wb')
pickle.dump(dogs_dict,outfile)
outfile.close()

infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

print(new_dict) # Printed: {'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16}
print(new_dict==dogs_dict) # Printed: True
print(type(new_dict)) # Printed: <class 'dict'>

# zipping
import bz2
import pickle
sfile = bz2.BZ2File('smallerfile', 'w')
pickle.dump(dogs_dict, sfile)

# unpickling if numpy (works with arrays) is used
infile = open(filename,'rb')
new_dict = pickle.load(infile, encoding='bytes')

# pickling classes - when converting to other languages
import pickle
class Animal:
   def __init__(self, number_of_paws, color):
       self.number_of_paws = number_of_paws
       self.color = color
class Sheep(Animal):
   def __init__(self, color):
       Animal.__init__(self, 4, color)
# Step 1: Let's create the sheep Mary
mary = Sheep("white")
# Step 2: Let's pickle Mary
my_pickled_mary = pickle.dumps(mary)
# Step 3: Now, let's unpickle our sheep Mary creating another instance, another sheep... Dolly!
dolly = pickle.loads(my_pickled_mary)
# Dolly and Mary are two different objects, in fact if we specify another color for dolly
# there are no conseguencies for Mary
dolly.color = "black"
print (str.format("Dolly is {0} ", dolly.color))
print (str.format("Mary is {0} ", mary.color))

# __setstate__() and __getstate__() to specify what you want to pickle and how to re-initialize (during the unpickling process) the objects that you haven’t pickled before.
import pickle

class my_zen_class:
   number_of_meditations = 0
   def __init__(self, name):
       self.number_of_meditations = 0
       self.name = name
   def meditate(self):
       self.number_of_meditations = self.number_of_meditations + 1
   def __getstate__(self):
       # this method is called when you are 
       # going to pickle the class, to know what to pickle
       state = self.__dict__.copy()
       # You will never get the Buddha state if you count 
       # meditations, so 
       # don't pickle this counter, the next time you will just 
       # start meditating from scratch :)
       del state['number_of_meditations']
       return state
   def __setstate__(self, state):
       # this method is called when you are going to 
       # unpickle the class,
       # if you need some initialization after the 
       # unpickling you can do it here.
       self.__dict__.update(state)

## json

import json
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
# prints: [1, 2, 3, 'a', 'b', 'c']
print(json.loads(json_string))

#    JSON is a text serialization format (it outputs unicode text, although most of the time it is then encoded to utf-8), while pickle is a binary serialization format;
#    JSON is human-readable, while pickle is not;
#    JSON is interoperable and widely used outside of the Python ecosystem, while pickle is Python-specific;
#    JSON, by default, can only represent a subset of the Python built-in types, and no custom classes; pickle can represent an extremely large number of Python types (many of them automatically, by clever usage of Python’s introspection facilities; complex cases can be tackled by implementing specific object APIs).

## yaml

# Technically YAML is a superset of JSON. This means that, in theory at least, a YAML parser can understand JSON, but not necessarily the other way around.

import json
import yaml
sample = {
  "foo": "bar",
  "baz": [
    "qux",
    "quxx"
  ],
  "corge": None,
  "grault": 1,
  "garply": True,
  "waldo": "false",
  "fred": "undefined",
  "emptyArray": [],
  "emptyObject": {},
  "emptyString": ""
}
json_obj = json.dumps(sample)
print 'json_obj =', json_obj
ff = open('data.yml', 'wb')
yaml.dump(sample, ff, default_flow_style=False)
ydump = yaml.dump(sample, default_flow_style=False)
print 'ydump =', ydump
ff.close()

# convert yml to json
stream = file('data.yml', 'r')
yml_loaded = yaml.load(stream)

with open('data.json','wb') as f:
    json.dump(yml_loaded, f)
# The data.json looks like this: {"emptyObject": {}, "emptyArray": [], "waldo": "false", "baz": ["qux", "quxx"], "emptyString": "", "corge": null, "grault": 1, "garply": true, "foo": "bar", "fred": "undefined"}

## protobuf

# If you’re looking for a serialization module that has support in multiple languages, Google’s Protobuf library is an option.
# Read the existing address book.
try:
  f = open(sys.argv[1], "rb")
  address_book.ParseFromString(f.read())
  f.close()
except IOError:
  print sys.argv[1] + ": Could not open file.  Creating a new one."

# Add an address.
PromptForAddress(address_book.people.add())

# Write the new address book back to disk.
f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()

---------------------------------------------------------------------------------------------
# Magic methods
https://rszalski.github.io/magicmethods/

Construction and Initialization
__new__(cls, [...) - 1 called
__init__(self, [...) - 2 called
__del__(self)

Comparison magic methods
__cmp__(self, other) - <, ==, !=, etc.
__eq__(self, other) - ==
__ne__(self, other) - !=
__lt__(self, other) - <
__gt__(self, other) - >
__le__(self, other) - <=
__ge__(self, other) - >=

Unary operators and functions
Normal arithmetic operators
Reflected arithmetic operators (some_object + other <=> other + some_object)
Augmented assignment (+=, -=, etc.)
Type conversion magic methods

Representing your Classes
__str__(self)
__repr__(self)
__unicode__(self)
__format__(self, formatstr)
__hash__(self)
__nonzero__(self)
__dir__(self)
__sizeof__(self)

Controlling Attribute Access
__getattr__(self, name) - calling attribute that doesn't exist. Is only invoked if the attribute wasn't found the usual ways
__setattr__(self, name, value) - defining behavior for assignment to an attribute.
__delattr__(self, name)
__getattribute__(self, name) - defining rules for whenever an attribute's value is accessed. Is invoked before looking at the actual attributes on the object.

Making Custom Sequences
__len__(self)
__getitem__(self, key) - self[key]
__setitem__(self, key, value) - self[key] = value
__delitem__(self, key) - del self[key]
__iter__(self)
__reversed__(self)
__contains__(self, item) - in
__missing__(self, key) - d["george"] if d is dict() without "george"

Reflection
__instancecheck__(self, instance) - isinstance(instance, class)
__subclasscheck__(self, subclass) - issubclass(subclass, class)

Callable Objects
__call__(self, [args...]) - allows instances of your classes to behave as if they were functions.

Context Managers (with)
__enter__(self)
__exit__(self, exception_type, exception_value, traceback)

Abstract Base Classes

Building Descriptor Objects
__get__(self, instance, owner)
__set__(self, instance, value)
__delete__(self, instance)
# Python uses descriptors underneath the covers to build properties, bound / unbound methods and class methods. If you look up the property class in Python’s documentation, you will see that it follows the descriptor protocol very closely:
property(fget=None, fset=None, fdel=None, doc=None)

class MyDescriptor():
    """
    A simple demo descriptor
    """
    def __init__(self, initial_value=None, name='my_var'):
        self.var_name = name
        self.value = initial_value
    def __get__(self, obj, objtype):
        print('Getting', self.var_name)
        return self.value
    def __set__(self, obj, value):
        msg = 'Setting {name} to {value}'
        print(msg.format(name=self.var_name, value=value))
        self.value = value
class MyClass():
    desc = MyDescriptor(initial_value='Mike', name='desc')
    normal = 10
if __name__ == '__main__':
    c = MyClass()
    print(c.desc)
    print(c.normal)
    c.desc = 100
    print(c.desc)

Otput:
Getting desc
Mike
10
Setting desc to 100
Getting desc
100

Copying
__copy__(self)
__deepcopy__(self, memodict={})

Pickling Your Objects
__getinitargs__(self) - __init__ to be called when your class is unpickled.
__getnewargs__(self) - influence what arguments get passed to __new__ upon unpickling.
__getstate__(self) - custom state to be stored when the object is pickled.
__setstate__(self, state) - the object's state will be passed to it instead of directly applied to the object's __dict__.
__reduce__(self) - how to pickle certain extension types if you want them to pickle them.
__reduce_ex__(self) - compatibility - will be called over __reduce__ on pickling.

import time

class Slate:
    '''Class to store a string and a changelog, and forget its value when pickled.'''
    def __init__(self, value):
        self.value = value
        self.last_change = time.asctime()
        self.history = {}
    def change(self, new_value):
        # Change the value. Commit last value to history
        self.history[self.last_change] = self.value
        self.value = new_value
        self.last_change = time.asctime()
    def print_changes(self):
        print 'Changelog for Slate object:'
        for k, v in self.history.items():
            print '%s\t %s' % (k, v)
    def __getstate__(self):
        # Deliberately do not return self.value or self.last_change.
        # We want to have a "blank slate" when we unpickle.
        return self.history
    def __setstate__(self, state):
        # Make self.history = state and last_change and value undefined
        self.history = state
        self.value, self.last_change = None, None

# Changes in Python 3

# Since the distinction between string and unicode has been done away with in Python 3, __unicode__ is gone and __bytes__ (which behaves similarly to __str__ and __unicode__ in 2.7) exists for a new built-in for constructing byte arrays.
# Since division defaults to true division in Python 3, __div__ is gone in Python 3
# __coerce__ is gone due to redundancy with other magic methods and confusing behavior
# __cmp__ is gone due to redundancy with other magic methods
# __nonzero__ has been renamed to __bool__

---------------------------------------------------------------------------------------------
# Bitwise operators
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print "Line 1 - Value of c is ", c
c = a | b;        # 61 = 0011 1101 
print "Line 2 - Value of c is ", c
c = a ^ b;        # 49 = 0011 0001 - XOR
print "Line 3 - Value of c is ", c
c = ~a;           # -61 = 1100 0011 - inversion
print "Line 4 - Value of c is ", c
c = a << 2;       # 240 = 1111 0000
print "Line 5 - Value of c is ", c
c = a >> 2;       # 15 = 0000 1111
print "Line 6 - Value of c is ", c

---------------------------------------------------------------------------------------------
# Design patterns
# GANG OF FOUR -book
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PatternConcept.html

## Creational Patterns

    # Singleton
    class Logger(object):
        def __new__(cls, *args, **kwargs):
            if not hasattr(cls, '_logger'):
                cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
            return cls._logger
    # Dependency Injection - Don’t get things to drink from the fridge yourself, tell your parents that you need something to drink.
    class Command:
        def __init__(self, authenticate=None, authorize=None):
            self.authenticate = authenticate or self._not_authenticated
            self.authorize = authorize or self._not_autorized
        def execute(self, user, action):
            self.authenticate(user)
            self.authorize(user, action)
            return action()
    if in_sudo_mode:
        command = Command(always_authenticated, always_authorized)
    else:
        command = Command(config.authenticate, config.authorize)
    command.execute(current_user, delete_user_action)
    # Prototype
    # Builder
    # Factory - creation of objects to occur through a common factory.
    import random
    class Shape(object):
        def factory(type):
            if type == "Circle": return Circle()
            if type == "Square": return Square()
            assert 0, "Bad shape creation: " + type
        factory = staticmethod(factory)
    class Circle(Shape):
        def draw(self): print("Circle.draw")
        def erase(self): print("Circle.erase")
    class Square(Shape):
        def draw(self): print("Square.draw")
        def erase(self): print("Square.erase")
    def shapeNameGen(n):
        types = Shape.__subclasses__()
        for i in range(n):
            yield random.choice(types).__name__
    shapes = [Shape.factory(i) for i in shapeNameGen(7)]
    for shape in shapes:
        shape.draw()
        shape.erase()

## Structural Patterns

    # Facade - add an interface object exposing a set of well known subset of API methods. If something is ugly, hide it inside an object.
    class Car(object):
        def __init__(self):
            self._tyres = [Tyre('front_left'),
                           Tyre('front_right'),
                           Tyre('rear_left'),
                           Tyre('rear_right'), ]
            self._tank = Tank(70)
        def tyres_pressure(self):
            return [tyre.pressure for tyre in self._tyres]
        def fuel_level(self):
            return self._tank.level
    # Adapter
    import socket
    class SocketWriter(object):
        def __init__(self, ip, port):
            self._socket = socket.socket(socket.AF_INET,
                                         socket.SOCK_DGRAM)
            self._ip = ip
            self._port = port
        def write(self, message):
            self._socket.send(message, (self._ip, self._port))
    def log(message, destination):
        destination.write('[{}] - {}'.format(datetime.now(), message))
    upd_logger = SocketWriter('1.2.3.4', '9999')
    log('Something happened', udp_destination)
    # Bridge
    # Proxy - specific case of State. Remote proxy, Virtual Proxy, Protection proxy, Smart Reference (additional actions)
    class Implementation:
        def f(self):
            print("Implementation.f()")
        def g(self):
            print("Implementation.g()")
        def h(self):
            print("Implementation.h()")
    class Proxy:
        def __init__(self):
            self.__implementation = Implementation()
        def __getattr__(self, name):
            return getattr(self.__implementation, name)
    p = Proxy()
    p.f(); p.g(); p.h();
    # Decorator
    def autheticated_only(method):
        def decorated(*args, **kwargs):
            if check_authenticated(kwargs['user']):
                return method(*args, **kwargs )
            else:
                raise UnauthenticatedError
        return decorated
    def authorized_only(method):
        def decorated(*args, **kwargs):
            if check_authorized(kwargs['user'], kwargs['action']):
                return method(*args, **kwargs)
            else:
                raise UnauthorizedError
        return decorated
    @authorized_only
    @authenticated_only
    def execute(action, *args, **kwargs):
        return action()
     
## Behavioral Patterns

    # Chain of responsibility - Every piece of code must do one, and only one, thing.
    class ContentFilter(object):
        def __init__(self, filters=None):
            self._filters = list()
            if filters is not None:
                self._filters += filters
        def filter(self, content):
            for filter in self._filters:
                content = filter(content)
            return content
    filter = ContentFilter([offensive_filter,
                            ads_filter,
                            porno_video_filter])
    filtered_content = filter.filter(content)
    # Command - preparing what will be executed and then to execute it when needed.
    class RenameFileCommand(object):
        def __init__(self, from_name, to_name):
            self._from = from_name
            self._to = to_name
        def execute(self):
            os.rename(self._from, self._to)
        def undo(self):
            os.rename(self._to, self._from)
    class History(object):
        def __init__(self):
            self._commands = list()
        def execute(self, command):
            self._commands.append(command)
            command.execute()
        def undo(self):
            self._commands.pop().undo()
    history = History()
    history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
    history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
    history.undo()
    history.undo()
    # Interpreter
    # Iterator
    # Mediator
    # Memento
    # Observer - if a group of objects needs to update themselves when some object changes state.
    # State
    class State_d:
        def __init__(self, imp):
            self.__implementation = imp
        def changeImp(self, newImp):
            self.__implementation = newImp
        def __getattr__(self, name):
            return getattr(self.__implementation, name)
    class Implementation1:
        def f(self):
            print("Fiddle de dum, Fiddle de dee,")
        def g(self):
            print("Eric the half a bee.")
        def h(self):
            print("Ho ho ho, tee hee hee,")
    class Implementation2:
        def f(self):
            print("We're Knights of the Round Table.")
        def g(self):
            print("We dance whene'er we're able.")
        def h(self):
            print("We do routines and chorus scenes")
    def run(b):
        b.f()
        b.g()
        b.h()
        b.g()
    b = State_d(Implementation1())
    run(b)
    b.changeImp(Implementation2())
    run(b)
    # Strategy
    # Template
    class ApplicationFramework:
        def __init__(self):
            self.__templateMethod()
        def __templateMethod(self):
            for i in range(5):
                self.customize1()
                self.customize2()
    class MyApp(ApplicationFramework):
        def customize1(self):
            print("Nudge, nudge, wink, wink! ",)
        def customize2(self):
            print("Say no more, Say no more!")
    MyApp()
    # Visitor - add methods to the base class, but you can’t touch the base class.
    class Flower(object):
        def accept(self, visitor):
            visitor.visit(self)
        def pollinate(self, pollinator):
            print(self, "pollinated by", pollinator)
        def eat(self, eater):
            print(self, "eaten by", eater)
        def __str__(self):
            return self.__class__.__name__
    class Gladiolus(Flower): pass
    class Runuculus(Flower): pass
    class Chrysanthemum(Flower): pass
    class Visitor:
        def __str__(self):
            return self.__class__.__name__
    class Bug(Visitor): pass
    class Pollinator(Bug): pass
    class Predator(Bug): pass
    class Bee(Pollinator):
        def visit(self, flower):
            flower.pollinate(self)
    class Fly(Pollinator):
        def visit(self, flower):
            flower.pollinate(self)
    class Worm(Predator):
        def visit(self, flower):
            flower.eat(self)
    bee = Bee()
    fly = Fly()
    worm = Worm()
    for flower in [Gladiolus(), Runuculus()]:
        flower.accept(bee)
        flower.accept(fly)
        flower.accept(worm)

---------------------------------------------------------------------------------------------
# State Machine
https://imatix-legacy.github.io/libero/lrintr.htm

# StateMachine/State.py
# A State has an operation, and can be moved
# into the next State given an Input:
class State:
    def run(self):
        assert 0, "run not implemented"
    def next(self, input):
        assert 0, "next not implemented"
# StateMachine/StateMachine.py
# Takes a list of Inputs to move from State to
# State using a template method.
class StateMachine:
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.run()
    # Template method:
    def runAll(self, inputs):
        for i in inputs:
            print(i)
            self.currentState = self.currentState.next(i)
            self.currentState.run()
input = [State(), State(), State()]
states = StateMachine(input[0])
states.runAll(input)

---------------------------------------------------------------------------------------------
# Fibonacci Row
# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

def fibon():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)



# Why is __init__() always called after __new__()?
# __new__ is the first step of instance creation. It's called first,
# and is responsible for returning a new instance of your class.
# In contrast, __init__ doesn't return anything; it's only responsible for
# initializing the instance after it's been created.
