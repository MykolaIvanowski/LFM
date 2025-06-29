from abc import ABC, abstractmethod

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass

# Terminal Expression
class Number(Expression):
    def __init__(self, value: int):
        self.value = value

    def interpret(self) -> int:
        return self.value

# Non-Terminal Expressions
class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()

# Usage
expr = Add(Number(5), Subtract(Number(10), Number(3)))  # 5 + (10 - 3)
print(expr.interpret())  # Output: 12