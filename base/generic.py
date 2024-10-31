from typing import List, TypeVar

T = TypeVar("T")


def first(container: List[T]) -> T:
    return container[0]


if __name__ == "__main__":
    list_one: List[str] = ["a", "b", "c"]
    print(first(list_one))
    list_one.append(1)# give a hint but not error
    list_two: List[int] = [1, 2, 3]
    print(first(list_two))

    list_two.append("word")
    print(list_two)