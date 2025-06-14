from abc import ABC, abstractmethod

# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass

# Concrete Mediator
class ChatMediator(Mediator):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def notify(self, sender, event):
        for user in self.users:
            if user != sender:
                user.receive_message(event)

# Colleague Class
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.add_user(self)

    def send_message(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.notify(self, message)

    def receive_message(self, message):
        print(f"{self.name} received: {message}")

# Usage
mediator = ChatMediator()
user1 = User("Alice", mediator)
user2 = User("Bob", mediator)

user1.send_message("Hello, Bob!")
user2.send_message("Hey, Alice!")