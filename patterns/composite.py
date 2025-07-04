from abc import ABC, abstractmethod

# main idea is when you need treat individual objects and groups uniformly.
# especially useful when you're working with tree-like structure

class FileSystemComponent(ABC):

    @abstractmethod
    def show_details(self):
        pass


# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f'file {self.name}')


# composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children  = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)


    def show_details(self):
        print(f'directory {self.name}')
        for chield in self.children:
            chield.show_details()


if __name__ == '__main__':
    root = Directory('root')
    home = Directory('home')
    user = Directory('user')

    file1 = File('file1.txt')
    file2 = File('file2.txt')
    file3 = File('config.json')

    user.add(file1)
    user.add(file2)
    home.add(user)
    root.add(home)
    root.add(file3)

    root.show_details()