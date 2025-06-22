# Element classes
class Animal:
    def accept(self, visitor):
        visitor.visit(self)

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"

# Visitor class
class AnimalSoundVisitor:
    def visit(self, animal):
        if isinstance(animal, Dog):
            print(animal.bark())
        elif isinstance(animal, Cat):
            print(animal.meow())
        else:
            print("Unknown animal")

# Usage
animals = [Dog(), Cat()]
visitor = AnimalSoundVisitor()

for animal in animals:
    animal.accept(visitor)