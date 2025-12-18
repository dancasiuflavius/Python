input_utilizator = input("Introduceti o lista de numere separate prin virgula: ")
lista_numere = [int(numar.strip()) for numar in input_utilizator.split(",")]

minim = min(lista_numere)
maxim = max(lista_numere)

print("Minimul din lista este:", minim)
print("Maximul din lista este:", maxim)
