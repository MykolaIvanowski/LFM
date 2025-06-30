class CarModel:
    """Flyweight class: shared intrinsic state"""
    def __init__(self, model_name):
        self.model_name = model_name

    def display(self, color):
        print(f"Displaying {self.model_name} in {color} color.")

class CarFactory:
    """Flyweight Factory: manages shared instances"""
    _models = {}

    @classmethod
    def get_model(cls, model_name):
        if model_name not in cls._models:
            cls._models[model_name] = CarModel(model_name)
        return cls._models[model_name]

# Client code
if __name__ == "__main__":
    factory = CarFactory()

    red_sedan = factory.get_model("Sedan")
    red_sedan.display("Red")

    blue_sedan = factory.get_model("Sedan")
    blue_sedan.display("Blue")

    print(f"Same object? {red_sedan is blue_sedan}")  # True
