class Djur:
    def __init__(self, namn) -> None:
        self.namn = namn

    def at(self):
        print("Jag äter")

    def sov(self):
        print("Jag sover")


class Fagel(Djur):
    def __init__(self, namn, vingspann) -> None:
        super().__init__(namn)
        self.vingspann = vingspann


class Fisk(Djur):
    def __init__(self, namn, maxdjup) -> None:
        super().__init__(namn)
        self.maxdjup = maxdjup

    def simma(self):
        print("Jag simmar")


class Haj(Fisk):
    def __init__(self, namn, maxdjup, antal_tänder) -> None:
        super().__init__(namn, maxdjup)
        self.antal_tänder = antal_tänder

    def at(self, djur):
        print(f"{self.namn} äter {djur.namn}")


class Torsk(Fisk):
    def __init__(self, namn, maxdjup, hastighet) -> None:
        super().__init__(namn, maxdjup)
        self.hastighet = hastighet


min_haj = Haj("kalle", 10, 50)
min_torsk = Torsk("bob", 10, 20)


def fånga(haj, torsk):
    return torsk.hastighet < 30 and haj.maxdjup >= torsk.maxdjup


fånga(min_haj, min_torsk)
