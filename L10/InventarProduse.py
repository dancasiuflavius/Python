class Inventar:
    def __init__(self):
        self.produse = {}

    def adauga_produs(self, nume, cantitate):
        if cantitate < 0:
            print("Eroare: Cantitatea trebuie să fie pozitivă!")
            return
        if nume in self.produse:
            self.produse[nume] += cantitate
        else:
            self.produse[nume] = cantitate
        print(f"Produs adăugat: {nume}, cantitate: {self.produse[nume]}")

    def cauta_produs(self, nume):
        try:
            return self.produse[nume]
        except KeyError:
            print(f"Eroare: Produsul '{nume}' nu există.")
            return None

    def actualizeaza_cantitate(self, nume, cantitate_noua):
        if cantitate_noua < 0:
            print("Eroare: Cantitatea trebuie să fie pozitivă!")
            return
        if nume in self.produse:
            self.produse[nume] = cantitate_noua
            print(f"Produsul '{nume}' actualizat. Cantitate: {cantitate_noua}")
        else:
            print(f"Eroare: Produsul '{nume}' nu există.")

inv = Inventar()
inv.adauga_produs("mere", 10)
inv.adauga_produs("pere", 5)
print(inv.cauta_produs("mere"))
print(inv.cauta_produs("banane"))
inv.actualizeaza_cantitate("mere", 15)
inv.actualizeaza_cantitate("banane", 5)
