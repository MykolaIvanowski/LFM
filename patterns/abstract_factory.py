from abc import ABC, abstractmethod

# Abstract Product A
class Chair(ABC):
    @abstractmethod
    def get_material(self):
        pass

# Concrete Product A1
class WoodenChair(Chair):
    def get_material(self):
        return "Wooden Chair"

# Concrete Product A2
class PlasticChair(Chair):
    def get_material(self):
        return "Plastic Chair"

# Abstract Factory
class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

# Concrete Factory 1
class WoodenFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return WoodenChair()

# Concrete Factory 2
class PlasticFurnitureFactory(FurnitureFactory):
    def create_chair(self):
        return PlasticChair()

# Client Code
def get_furniture(factory: FurnitureFactory):
    chair = factory.create_chair()
    print(f"Created: {chair.get_material()}")

# Usage
wood_factory = WoodenFurnitureFactory()
plastic_factory = PlasticFurnitureFactory()

get_furniture(wood_factory)  # Output: Created: Wooden Chair
get_furniture(plastic_factory)  # Output: Created: Plastic Chair