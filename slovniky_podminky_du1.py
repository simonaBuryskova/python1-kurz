baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kodBaliku = input("Kód balíku?: ")
if kodBaliku in baliky:
    if baliky[kodBaliku]==True: print(f"Balík s kódem {kodBaliku} byl předán kurýrovi.")
    else: print(f"Balík s kódem {kodBaliku} zatím nebyl předán kurýrovi.")
else: print(f"Balík s kódem {kodBaliku} nenalezen.")
