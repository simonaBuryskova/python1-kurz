class Polozka:
  def __init__(self, nazev, zanr):
    self.nazev = nazev
    self.zanr = zanr
  def __str__(self):
      return(f"Nazev:{self.nazev}, Zanr: {self.zanr}")

class Film(Polozka):
  def __init__(self, nazev, zanr,delka):
    super().__init__(nazev, zanr)
    self.delka = delka
  def __str__(self):
       return(super().__str__() + f", delka: {self.delka}")

class Serial(Polozka):
  def __init__(self, nazev, zanr,pocet_epizod, delka_epizody):
    super().__init__(nazev, zanr)
    self.pocet_epizod = pocet_epizod
    self.delka_epizody = delka_epizody
  def __str__(self):
      return(super().__str__() + f", pocet epizod: {self.pocet_epizod}, delka epizody: {self.delka_epizody}")

film = Film("Hledá se Nemo", "Rodinný film", "1 h 40 min")
serial = Serial("Geniální přítelkyně", "Drama", "24", "43-74 min" )

print(film)
print(serial)
