import numpy as np
import pandas as pd

np.random.seed(42)

produse = ['Produs A', 'Produs B', 'Produs C', 'Produs D', 'Produs E', 'Produs F', 'Produs G', 'Produs H']

zile = pd.date_range(start='2024-01-01', periods=60)
date_list = []

for zi in zile:
    nr_produse_vandute = np.random.randint(5, 16)
    produse_vandute = np.random.choice(produse, nr_produse_vandute)
    preturi = np.random.normal(loc=40, scale=8, size=nr_produse_vandute)
    preturi = np.maximum(preturi, 1)
    cantitati = np.random.randint(1, 11, size=nr_produse_vandute)
    promotii = np.random.rand(nr_produse_vandute) < 0.3
    preturi[promotii] *= 0.8
    for p, q, pr in zip(produse_vandute, cantitati, preturi):
        total_vanzari = pr * q
        profit = total_vanzari * 0.3
        date_list.append([zi, p, q, pr, total_vanzari, profit])

df = pd.DataFrame(date_list, columns=['Data', 'Produs', 'Cantitate', 'Pret', 'TotalVanzari', 'Profit'])

print("Primele 10 linii din dataset:")
print(df.head(10))

print("\nStatistici generale:")
print("Preturi: media =", round(df['Pret'].mean(),2), ", max =", round(df['Pret'].max(),2), ", min =", round(df['Pret'].min(),2))
print("Cantitati: media =", round(df['Cantitate'].mean(),2), ", max =", df['Cantitate'].max(), ", min =", df['Cantitate'].min())
print("Profituri: media =", round(df['Profit'].mean(),2), ", max =", round(df['Profit'].max(),2), ", min =", round(df['Profit'].min(),2))

total_vanzari = df['TotalVanzari'].sum()
total_profit = df['Profit'].sum()

print("\nTotal vanzari pe 60 de zile:", round(total_vanzari,2))
print("Profit total pe 60 de zile:", round(total_profit,2))
