# Subsystem Classes
class Amplifier:
    def turn_on(self):
        print("Amplifier ON")

    def set_volume(self, level):
        print(f"Volume set to {level}")


class DVDPlayer:
    def play_movie(self, movie):
        print(f"Playing movie: {movie}")


class Projector:
    def turn_on(self):
        print("Projector ON")

    def set_mode(self, mode):
        print(f"Projector mode set to {mode}")


class Lights:
    def dim(self):
        print("Lights dimmed")


# Façade Class
class HomeTheaterFacade:
    def __init__(self, amp, dvd, projector, lights):
        self.amp = amp
        self.dvd = dvd
        self.projector = projector
        self.lights = lights

    def watch_movie(self, movie):
        print("\nStarting movie mode...")
        self.lights.dim()
        self.projector.turn_on()
        self.projector.set_mode("Cinema")
        self.amp.turn_on()
        self.amp.set_volume(10)
        self.dvd.play_movie(movie)


# Client Code
if __name__ == "__main__":
    home_theater = HomeTheaterFacade(
        Amplifier(),
        DVDPlayer(),
        Projector(),
        Lights()
    )

    home_theater.watch_movie("Interstellar")