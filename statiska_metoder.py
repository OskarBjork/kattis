class Bil:
    _antal_bilar = 0

    def __init__(self) -> None:
        Bil._antal_bilar += 1

    @staticmethod
    def honk():
        print("Honk honk")

    @staticmethod
    def miles_to_km(miles):
        return miles * 1.60934

    def __hello(self):
        print("Hello")


bil1 = Bil()
bil2 = Bil()
bil3 = Bil()

print(Bil._antal_bilar)
bil1._Bil__hello()
