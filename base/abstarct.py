from abc import ABC, ABCMeta, abstractmethod

# Висновок в пайтоні немає прямого (синтаксису) способу зробити абстракний клас але є ліба abc
# яка може зробити клас абстракний.
# ABC наслідує метаклас ABCMeta (приклад в лібі)
# Екземляр абстрактного класу сторити не можна якщо написати абстракний метод (@abstractmethod)


class AbstractMeta(metaclass=ABCMeta):
    pass


class Abstract(ABC):
    pass


class AbstractAndMethod(ABC):
    @abstractmethod
    def method(self):
        pass


class AbstractAndMethod_1(ABC):
    def method(self):
        pass



abst = AbstractMeta()
abst_1 = Abstract()
# abst_2 = AbstractAndMethod()# TypeError: Can't instantiate abstract class AbstractAndMethod with abstract methods
abst_3 = AbstractAndMethod_1()


class Derived(AbstractAndMethod):
    # обовязково потрібно реалізовувати методи з декоратором абстракт
    pass


class DerivedMeta(AbstractMeta):

    pass

# d = Derived()  # TypeError: Can't instantiate abstract class Derived with abstract methods method
d1 = DerivedMeta()
