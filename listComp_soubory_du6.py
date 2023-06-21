nazev = input("zadejte nazev souboru: ")
with open(nazev, encoding='utf-8') as vstup:
    autaText = vstup.readlines()

autaText = [radek.replace(",", ".") for radek in autaText]
autaText = [radek.strip() for radek in autaText]
kilometry = [float(radek[9:13]) for radek in autaText]

print(f"Auta dohromady najezdila {sum(kilometry)} kilometrů.")

