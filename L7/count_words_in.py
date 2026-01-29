def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            continut = file.read()
            cuvinte = continut.split()
            return len(cuvinte)

    except FileNotFoundError:
        print("Eroare: Fișierul nu a fost găsit.")
        return 0

    except PermissionError:
        print("Eroare: Nu ai permisiunea să citești fișierul.")
        return 0

    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")
        return 0


rezultat = count_words_in_file("r.txt")
print("Număr de cuvinte:", rezultat)