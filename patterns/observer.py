# The Subject
class TemperatureSensor:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, value):
        print(f"\nSensor: New temperature is {value}°C")
        self._temperature = value
        self.notify()

# The Observer Interface
class TemperatureDisplay:
    def update(self, temperature):
        print(f"Display: Temperature updated to {temperature}°C")

class TemperatureLogger:
    def update(self, temperature):
        print(f"Logger: Recorded temperature {temperature}°C")

# Usage
sensor = TemperatureSensor()
display = TemperatureDisplay()
logger = TemperatureLogger()

sensor.attach(display)
sensor.attach(logger)

sensor.set_temperature(22)
sensor.set_temperature(25)