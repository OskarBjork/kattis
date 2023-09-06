from dataclasses import dataclass
import attrs


@attrs.define
class Plane:
    velocity: float
    acceleration: float
    position: float
    flight_number: int
    model: str
    manufacturer: str
    passengers: int
    fuel: float

    def fly(self, time: float):
        self.position += self.velocity * time + 0.5 * self.acceleration * time**2
        self.velocity += self.acceleration * time
        self.fuel -= self.acceleration * time

    def land(self):
        self.acceleration = 0
        self.velocity = 0

    def refuel(self, fuel: float):
        self.fuel += fuel


class Elev:
    def __init__(self, name: str, age: int, godkänd: bool) -> None:
        self.name = name
        self.age = age
        if godkänd:
            self.glad = True

    def presentera(self):
        print(f"Jag heter {self.name} och är {self.age} år gammal")


oskar = Elev("Oskar", 17, True)
oskar.presentera()
