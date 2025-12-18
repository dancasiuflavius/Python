x = int(input("Introdu un număr: "))

if x == 2:
    print("Numărul este prim.")
elif x % 2 == 0 or x <= 1:
    print("Numărul nu este prim.")
else:
    este_prim = True
    for i in range(3, x // 2 + 1, 2):
        if x % i == 0:
            este_prim = False
            break

    if este_prim:
        print("Numărul este prim.")
    else:
        print("Numărul nu este prim.")
