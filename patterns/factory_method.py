from abc import ABC, abstractmethod

# Step 1: Define an abstract product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Step 2: Create concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Step 3: Define the factory method
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Step 4: Client code using the factory method
dog_factory = DogFactory()
dog = dog_factory.create_animal()
print(dog.speak())  # Output: Woof!

cat_factory = CatFactory()
cat = cat_factory.create_animal()
print(cat.speak())  # Output: Meow!