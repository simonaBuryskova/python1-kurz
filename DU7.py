import re
with open('posta.txt', encoding='utf-8') as vstup:
    vstup = vstup.read()

nahradEnter = re.compile(r"\n")
vstup = nahradEnter.sub(" ",vstup)

nahradMezery = re.compile(r"\s+")
vstup = nahradMezery.sub(" ",vstup)

najdiAdresy = re.compile(r"\d{3} \d{2} [\w ]+[ \d+]*")
vysledky = najdiAdresy.findall(vstup)

for vysledek in vysledky:
    print(vysledek)

print(f"Počet výsledků je: {len(vysledky)}")

