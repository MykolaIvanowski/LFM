class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.color = None

    def __str__(self):
        return f'{self.make} {self.color} {self.model}'


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model
        return self

    def set_make(self, make):
        self.car.make = make
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car

builder_obj = CarBuilder()
car = (builder_obj.set_make('SEAT')
       .set_color('white').set_model('Leon').build())

print(car)