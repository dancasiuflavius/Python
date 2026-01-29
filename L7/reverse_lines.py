def reverse_lines(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as fin, \
             open(output_file, "w", encoding="utf-8") as fout:

            for linie in fin:
                linie_fara_newline = linie.rstrip("\n")
                linie_inversata = linie_fara_newline[::-1]
                fout.write(linie_inversata + "\n")

    except FileNotFoundError:
        print("Eroare: Fișierul de intrare nu a fost găsit.")

    except PermissionError:
        print("Eroare: Nu ai permisiunea necesară pentru fișiere.")

    except Exception as e:
        print(f"A apărut o eroare neașteptată: {e}")

reverse_lines("r.txt", "output.txt")
print("Fișierul output.txt a fost creat.")