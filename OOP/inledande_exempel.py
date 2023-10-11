class Fordon:
    def kör(self):
        print("Jag kör")


class Bil(Fordon):
    def tuta(self):
        print("Tuuuuut")


class Cykel(Fordon):
    def plinga(self):
        print("Ring ring")


class Sportbil(Bil):
    def kör(self):
        print("Jag kör snabbt")
