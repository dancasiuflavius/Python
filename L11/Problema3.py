import numpy as np
import pandas as pd
from Problema2 import df

df['Data'] = pd.to_datetime(df['Data'])

vanzari_pe_zi = df.groupby('Data')['TotalVanzari'].sum()
profit_pe_zi = df.groupby('Data')['Profit'].sum()

print("Venit total pe zile:")
print(vanzari_pe_zi.head())
print("\nProfit total pe zile:")
print(profit_pe_zi.head())

distributie_preturi = df['Pret'].value_counts().sort_index()
distributie_cantitati = df['Cantitate'].value_counts().sort_index()

print("\nDistribuția preturilor:")
print(distributie_preturi.head(10))
print("\nDistribuția cantitatilor:")
print(distributie_cantitati.head(10))

df['Promotie'] = df['Pret'] < (df['TotalVanzari'] / df['Cantitate'])
zile_cu_promotii = df[df['Promotie']].groupby('Data').size()
impact_promotii = df[df['Promotie']].groupby('Data')['TotalVanzari'].sum()

print("\nZile cu promotii (numar produse promo):")
print(zile_cu_promotii.head())
print("\nImpactul promotilor asupra veniturilor:")
print(impact_promotii.head())
