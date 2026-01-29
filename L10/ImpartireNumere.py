def imparte(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Eroare: Împărțirea la zero nu este permisă!")
        return None

print(imparte(10, 2))
print(imparte(5, 0))
