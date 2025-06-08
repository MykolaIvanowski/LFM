# Implementor (Defines the base interface)
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


# Concrete Implementors (Different device implementations)
class TV(Device):
    def turn_on(self):
        print("TV is now ON")

    def turn_off(self):
        print("TV is now OFF")


class Radio(Device):
    def turn_on(self):
        print("Radio is now ON")

    def turn_off(self):
        print("Radio is now OFF")


# Abstraction (Base class using the Implementor)
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def power_on(self):
        self.device.turn_on()

    def power_off(self):
        self.device.turn_off()


# Extended Abstraction (More complex functionality)
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        print("Device is now muted")


# Client Code (Using the Bridge Pattern)
tv = TV()
remote = RemoteControl(tv)
remote.power_on()  # Output: TV is now ON
remote.power_off()  # Output: TV is now OFF

radio = Radio()
advanced_remote = AdvancedRemoteControl(radio)
advanced_remote.power_on()  # Output: Radio is now ON
advanced_remote.mute()  # Output: Device is now muted