while True:
    scor = int(input("Introdu scorul procentual (0-100): "))

    if 0 <= scor <= 100:
        break
    else:
        print("Scor invalid! Te rog introdu un număr între 0 și 100.")

if scor >= 90:
    print("Nota A")
elif scor >= 80:
    print("Nota B")
elif scor >= 70:
    print("Nota C")
elif scor >= 60:
    print("Nota D")
else:
    print("Nota F")
