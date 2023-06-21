#SMS brana

#funkce na kontrolu delky tel.cisl
def delkaTelCisla():
    telCislo = input("Zadejte tel. cislo: ")
    telCislo = telCislo.replace(" ", "")
    delka = len(telCislo)

    if delka<9 or delka>13: kontrola = False
    elif (telCislo[0:4] == '+420' and delka == 13) or delka == 9: kontrola = True
    else: kontrola = False
    return kontrola

#funkce na zadani zpravy a spocteni ceny
def cenaZpravy():
    zprava = input("Zadejte vasi zpravu (cena je 3 Kc za kazdych zapocatych 180 znaku): ")
    delkaZpravy = len(str(zprava))
    dalsichZapocatych180 = 0
    if delkaZpravy % 180 > 0: dalsichZapocatych180 = True
    cena = (delkaZpravy // 180)*3 + dalsichZapocatych180*3
    print(f"Cena vasi zpravy je {cena} Kc.")

#volani funkci
kontrola = delkaTelCisla()
if kontrola == True: cenaZpravy()
else: print("Neplatne tel. cislo.")

