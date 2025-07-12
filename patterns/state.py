from abc import ABC, abstractmethod

# Abstract State
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass

# Concrete States
class StateA(State):
    def handle(self, context):
        print("StateA: Doing something and switching to StateB")
        context.state = StateB()

class StateB(State):
    def handle(self, context):
        print("StateB: Doing something else and switching to StateA")
        context.state = StateA()

# Context
class Context:
    def __init__(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)

# Usage
context = Context(StateA())
for _ in range(4):
    context.request()