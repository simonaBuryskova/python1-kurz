class Auto:
    def __init__(self, spz, typ, km, obsazenost = True):
        self.spz = spz
        self.typ = typ
        self.km = km
        self.obsazenost = obsazenost
    def pujc_auto(self):
        if self.obsazenost == True: 
            self.obsazenost = False
            print("Potvrzuji zapůjčení vozidla.")
        else: print("Vozidlo není k dispozici")
    def get_info(self):
        print(f"Informace o vozidle: {self.spz}, {self.typ}")

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

def dotazNaUzivatele():
    dotazNaUzivatele = input("Chcete Peugeot, nebo Škodu?: ")
    if dotazNaUzivatele == "Peugeot": 
        print(peugeot.get_info())
        peugeot.pujc_auto()
    elif dotazNaUzivatele == "Škoda": 
        print(skoda.get_info())
        skoda.pujc_auto()
    else: print("Nemáme.")

dotazNaUzivatele()
dotazNaUzivatele()
