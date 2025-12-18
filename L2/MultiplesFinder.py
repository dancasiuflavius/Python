while True:
    try:
        x = int(input("Introdu numărul x: "))
        y = int(input("Introdu numărul y: "))

        if x == 0:
            print("x nu poate fi 0! Introdu altă valoare.")
            continue

        break  # dacă totul e valid, ieșim din loop
    except ValueError:
        print("Te rog introdu doar numere întregi!")

print(f"Multiplurile lui {x} mai mici decât {y} sunt:")

multiplu = x
while multiplu < y:
    print(multiplu)
    multiplu += x
