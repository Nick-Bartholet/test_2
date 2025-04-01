import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Figur:
    def __init__(self, name="Figur"):
        self.name = name

    def umfang(self):
        return 0

    @staticmethod
    def dist(p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def __str__(self):
        return self.name

class Dreieck(Figur):
    def __init__(self, p1, p2, p3):
        super().__init__("Dreieck")
        self.p1, self.p2, self.p3 = p1, p2, p3

    def umfang(self):
        return (self.dist(self.p1, self.p2) + 
                self.dist(self.p2, self.p3) + 
                self.dist(self.p3, self.p1))

    def __str__(self):
        return f"{self.name} {self.p1} – {self.p2} – {self.p3}"

class Rechteck(Figur):
    def __init__(self, p1, p2):
        super().__init__("Rechteck")
        self.p1, self.p2 = p1, p2

    def umfang(self):
        width, height = abs(self.p2.x - self.p1.x), abs(self.p2.y - self.p1.y)
        return 2 * (width + height)

    def __str__(self):
        return f"{self.name} {self.p1} – {self.p2}"

class Kreis(Figur):
    def __init__(self, center, radius):
        super().__init__("Kreis")
        self.center, self.radius = center, radius

    def umfang(self):
        return round(2 * math.pi * self.radius, 2)

    def __str__(self):
        return f"{self.name} M={self.center} r={self.radius}"

class Polygon(Figur):
    def __init__(self, *ecken):
        super().__init__("Polygon")
        self.ecken = ecken

    def umfang(self):
        return sum(self.dist(self.ecken[i], self.ecken[(i + 1) % len(self.ecken)])
                   for i in range(len(self.ecken)))

    def __str__(self):
        return f"{self.name} " + " – ".join(str(ecke) for ecke in self.ecken)

# Test
p1, p2, p3, p4 = Punkt(0, 0), Punkt(10, 15), Punkt(10, 0), Punkt(0, 15)

dreieck = Dreieck(p1, p2, p3)
rechteck = Rechteck(p1, p2)
kreis = Kreis(Punkt(2.3, 4.2), 3.4)
polygon = Polygon(p1, p2, p3, p4)

for figur in [dreieck, rechteck, kreis, polygon]:
    print(figur)
    print(f"Umfang: {figur.umfang()}\n")
