class Component:
    """Base interface for objects."""
    def operation(self):
        return "Base Component"

class Decorator(Component):
    """Base decorator class."""
    def __init__(self, component):
        self._component = component

    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    """Adds behavior A."""
    def operation(self):
        return f"ConcreteDecoratorA({self._component.operation()})"

class ConcreteDecoratorB(Decorator):
    """Adds behavior B."""
    def operation(self):
        return f"ConcreteDecoratorB({self._component.operation()})"

# Usage
component = Component()
decorated = ConcreteDecoratorA(ConcreteDecoratorB(component))
print(decorated.operation())  # Output: ConcreteDecoratorA(ConcreteDecoratorB(Base Component))