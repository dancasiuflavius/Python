while True:
    try:
        n = int(input("Introdu un număr n (pozitiv): "))
        if n <= 0:
            print("Te rog introdu un număr mai mare decât 0!")
            continue
        break
    except ValueError:
        print("Te rog introdu un număr întreg valid!")

print(f"Numerele impare până la {n} sunt:")
for i in range(1, n + 1, 2):
    print(i)
