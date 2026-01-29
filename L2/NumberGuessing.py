import random

numar_de_ghicit = random.randint(1, 20)
incercari = 5

print("Ghiceste numărul (între 1 și 20). Ai 5 încercări!")

for i in range(incercari):
    try:
        guess = int(input(f"Încercarea {i + 1}: "))

        if guess < 1 or guess > 20:
            print("Introdu un număr între 1 și 20!")
            continue

        if guess < numar_de_ghicit:
            print("Prea mic!")
        elif guess > numar_de_ghicit:
            print("Prea mare!")
        else:
            print("Corect! Ai ghicit numărul!")
            break

    except ValueError:
        print("Te rog introdu un număr valid!")

else:
    print(f"Ai pierdut! Numărul corect era: {numar_de_ghicit}")
