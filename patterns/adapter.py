# Existing classes with incompatible interfaces
class MotorCycle:
    def __init__(self):
        self.name = "MotorCycle"

    def two_wheeler(self):
        return "TwoWheeler"

class Truck:
    def __init__(self):
        self.name = "Truck"

    def eight_wheeler(self):
        return "EightWheeler"

# Adapter class
class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

# Using the adapter
if __name__ == "__main__":
    vehicles = []

    motorcycle = MotorCycle()
    vehicles.append(Adapter(motorcycle, wheels=motorcycle.two_wheeler))

    truck = Truck()
    vehicles.append(Adapter(truck, wheels=truck.eight_wheeler))

    for vehicle in vehicles:
        print(f"{vehicle.name} is a {vehicle.wheels()}")