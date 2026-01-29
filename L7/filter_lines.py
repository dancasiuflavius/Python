def filter_lines(input_file, output_file, keyword):
    try:
        with open(input_file, "r", encoding="utf-8") as fin, \
             open(output_file, "w", encoding="utf-8") as fout:

            for linie in fin:
                if keyword in linie:
                    fout.write(linie)

    except FileNotFoundError:
        print("Eroare: Fișierul de intrare nu a fost găsit.")

    except PermissionError:
        print("Eroare: Nu ai permisiunea necesară pentru fișiere.")

    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")

filter_lines("input.txt", "filtered.txt", "Python")
print("Fișierul filtered.txt a fost creat.")