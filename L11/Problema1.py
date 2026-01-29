import pandas as pd

df = pd.read_csv("vanzari_companie - vanzari_companie.csv")
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
df['Venit'] = df['Cantitate'] * df['Pret']

df['An-Luna'] = df['Data'].dt.to_period('M')
vandute_pe_luna = df.groupby(['An-Luna', 'Produs'])['Cantitate'].sum()
cele_mai_vandute = vandute_pe_luna.groupby(level=0).idxmax()
print("Cele mai vandute produse pe luna:")
for luna, produs in cele_mai_vandute.items():
    cant = vandute_pe_luna[produs]
    print(f"{luna}: {produs[1]} ({cant} buc)")

venit_total = df.groupby('Produs')['Venit'].sum()
print("\nVenitul total pe fiecare produs:")
print(venit_total)

start_date = '2024-01-01'
end_date = '2024-03-31'
filtrat = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]
print(f"\nVanzari intre {start_date} si {end_date}:")
print(filtrat)

venit_lunar = df.groupby('An-Luna')['Venit'].mean()
print("\nVenitul mediu lunar:")
print(venit_lunar)
