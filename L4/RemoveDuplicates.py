input_utilizator = input("Introduceti o lista de numere separate prin virgula: ")

lista_numere = [int(x.strip()) for x in input_utilizator.split(",")]

lista_unica = []
for numar in lista_numere:
    if numar not in lista_unica:
        lista_unica.append(numar)

print("Output:", ", ".join(str(x) for x in lista_unica))
