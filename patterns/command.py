from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver
class Light:
    def turn_on(self):
        print("The light is ON")

    def turn_off(self):
        print("The light is OFF")

# Concrete Commands
class TurnOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class TurnOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# Client Code
light = Light()
remote = RemoteControl()

turn_on = TurnOnCommand(light)
turn_off = TurnOffCommand(light)

remote.set_command(turn_on)
remote.press_button()  # Output: The light is ON

remote.set_command(turn_off)
remote.press_button()  # Output: The light is OFF