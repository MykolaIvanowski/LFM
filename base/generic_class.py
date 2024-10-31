from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content


box  = Box[int](12)
box1  = Box[int]('12')

print(type(box))
print(type(box))
