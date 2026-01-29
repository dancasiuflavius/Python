import math

class Forma:
    def aria(self):
        raise NotImplementedError("Metoda aria() trebuie suprascrisă în subclasă")


class Cerc(Forma):
    def __init__(self, raza):
        if raza <= 0:
            raise ValueError("Eroare: Raza trebuie să fie pozitivă!")
        self.raza = raza

    def aria(self):
        return math.pi * self.raza ** 2

    def __str__(self):
        return f"Cerc cu raza {self.raza} are aria {self.aria():.2f}"


class Dreptunghi(Forma):
    def __init__(self, latime, inaltime):
        if latime <= 0 or inaltime <= 0:
            raise ValueError("Eroare: Lățimea și înălțimea trebuie să fie pozitive!")
        self.latime = latime
        self.inaltime = inaltime

    def aria(self):
        return self.latime * self.inaltime

    def __str__(self):
        return f"Dreptunghi cu lățimea {self.latime} și înălțimea {self.inaltime} are aria {self.aria():.2f}"


try:
    cerc = Cerc(5)
    dreptunghi = Dreptunghi(10, 4)
    print(cerc)
    print(dreptunghi)

except ValueError as e:
    print(e)
