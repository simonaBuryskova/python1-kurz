from datetime import datetime

datum = datetime.strptime(input("Zadejte datum: "),"%d. %m. %Y").date()
prvniCervenec = datetime.strptime('1. 7. 2021','%d. %m. %Y').date()
desatySrpen = datetime.strptime("10. 8. 2021","%d. %m. %Y").date()
jedenactySrpen = datetime.strptime("11. 8. 2021","%d. %m. %Y").date()
posledniSrpen = datetime.strptime("31. 8. 2021","%d. %m. %Y").date()

if prvniCervenec <= datum <= desatySrpen:
  cena = 250
  pocet = int(input("Zadejte počet osob: "))
  print(f"Cena: {cena*pocet}")
elif jedenactySrpen <= datum <= posledniSrpen:
  cena = 180
  pocet = int(input("Zadejte počet osob: "))
  print(f"Cena: {cena*pocet}")
else: 
    print('Kino je v tuto dobu zavřené.')






