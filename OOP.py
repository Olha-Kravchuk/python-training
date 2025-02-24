class Auto():
    def __init__(self, marke, modell, jahr, tueren, ps):
        self.marke = marke
        self.modell = modell
        self.jahr = jahr
        self.raeder = 4
        self.tueren = tueren
        self.ps = ps

    def info(self):
        print("Dein Auto hat folgende Werte:")
        print("Marke", self.marke)
        print("Modell", self.modell)
        print("Jahr", self.jahr)
        print("Raeder", self.raeder)
        print("Tueren", self.tueren)

    def begruessung(self):
        print("Hallo mein Lieber, ich bin " + self.marke)

    def fahren(self):
        print("brmbrmbrm" * int(self.ps/10))

class Sportwagen(Auto):
    def __init__(self, marke, modell, jahr, tueren, ps, fulierung):
        super().__init__(marke, modell, jahr, tueren, ps)
        self.fulierung = fulierung
        self.auspeff = 2

    def turbo(self):
        print("turbo aktiwiren")

    def fahren(self):
        print("RACEEEE")

class Kombi(Auto):
    def __init__(self, marke, modell, jahr, tueren, ps, ladeflaeche):
        super().__init__(marke, modell, jahr, tueren, ps)
        self.ladeflaeche = ladeflaeche

sw1 = Sportwagen("seat", "Ibiza", 2020, 2, 20, "matt")
sw1.turbo()
sw1.fahren()
print(sw1.fulierung)

auto1 = Auto("Volswagen", "golf", "2019", 4, 100)
print(auto1.jahr)

auto1.begruessung()
auto1.fahren()
auto1.info()

kombi1 = Kombi("Audi", "A3", 1999, 4, 100, 10)
print(kombi1.ladeflaeche)