from collections.abc import Iterator, Iterable

class CustomIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        if self._index >= len(self._collection):
            raise StopIteration
        value = self._collection[self._index]
        self._index += 1
        return value

class CustomIterable(Iterable):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return CustomIterator(self._collection)

# Example usage:
my_list = [1, 2, 3, 4, 5]
iterable = CustomIterable(my_list)

for item in iterable:
    print(item)