def suma_numere_din_fisier(nume_fisier):
    suma = 0
    try:
        with open(nume_fisier, "r") as f:
            for linie in f:
                linie = linie.strip()
                if linie:  # dacă linia nu e goală
                    try:
                        suma += float(linie)
                    except ValueError:
                        print(f"Avertisment: '{linie}' nu este un număr valid și a fost ignorat.")
        return suma
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{nume_fisier}' nu există.")
    except IOError:
        print(f"Eroare: Nu s-a putut citi fișierul '{nume_fisier}'.")

print(suma_numere_din_fisier("numere.txt"))
