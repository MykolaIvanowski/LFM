from copy import deepcopy


class Prototype:
    def __init(self):
        self._object = {}

    def register_object(self, name, obj):
        self._object[name] = obj

    def unregister_object(self, name):
        if name in self._object:
            del self._object[name]

    def clone(self, name, **attrs):
        if name not in self._object:
            raise ValueError(f'object {name} is not register')
        object = deepcopy(self._object[name])
        object.__dict__.update(attrs)
        return object


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f'Car(model=self{self.model},color={self.color})'


prototype = Prototype()
car1 = Car('Mazda','red')


clone_car = prototype.clone(name='normal car',color= 'blue', model='Mazda' )
print(clone_car)