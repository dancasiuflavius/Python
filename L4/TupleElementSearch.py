input_utilizator = input("Introduceti valori separate prin virgula: ")

tupla = tuple(int(x.strip()) for x in input_utilizator.split(","))

print("Tupla:", tupla)

valoare_cautata = int(input("Search for: "))

if valoare_cautata in tupla:
    index = tupla.index(valoare_cautata)
    print(f"{valoare_cautata} se regaseste in tupla la indexul {index}.")
else:
    print(f"{valoare_cautata} nu se regaseste in tupla.")
