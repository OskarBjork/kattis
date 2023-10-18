class däggdjur:
    def __init__(self, namn, vikt):
        self.namn = namn
        self.vikt = vikt

    def äta(self, mat):
        print(f"{self.namn} äter {mat}")

    def sova(self):
        print(f"{self.namn} sover")

    def springa(self):
        print(f"{self.namn} springer")


class landdjur:
    def __init__(self, namn, vikt, antal_ben):
        self.namn = namn
        self.vikt = vikt
        self.antal_ben = antal_ben

    def röra_på_sig(self):
        print(f"{self.namn} rör sig med sina {self.antal_ben} ben")

    def sova(self):
        print(f"{self.namn} sover på marken")

    def äta(self, mat):
        print(f"{self.namn} äter {mat} på marken")


class havsdjur:
    def __init__(self, namn, vikt, djup):
        self.namn = namn
        self.vikt = vikt
        self.djup = djup

    def simma(self):
        print(f"{self.namn} simmar på djupet {self.djup}")

    def äta(self, mat):
        print(f"{self.namn} äter {mat} i havet")


class val(däggdjur, havsdjur):
    def __init__(self, namn, vikt, djup):
        däggdjur.__init__(self, namn, vikt)
        havsdjur.__init__(self, namn, vikt, djup)


class fisk(havsdjur):
    def __init__(self, namn, vikt, djup, färg):
        havsdjur.__init__(self, namn, vikt, djup)
        self.färg = färg

    def simma(self):
        print(f"{self.namn} simmar i vattnet")

    def byt_färg(self, ny_färg):
        print(f"{self.namn} byter färg från {self.färg} till {ny_färg}")
        self.färg = ny_färg


class ödla(landdjur):
    def __init__(self, namn, vikt, antal_ben):
        landdjur.__init__(self, namn, vikt, antal_ben)

    def klättra(self):
        print(f"{self.namn} klättrar på en sten")
