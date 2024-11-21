#FICHIER QUI NE DEVRA PAS ETRE DANS LE RENDU FINALE
#CE FICHIER SERT A TESTER DES TRUCS ET DECOUVRIR UN PEU LE TRUC

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)

import my_statistics

print(data['Combined (L/100 km)'].describe())
print(data['Combined (mpg)'].describe())
print(f"La plus grosse conso au L/km est {data.loc[data['Combined (L/100 km)'].idxmax(), 'Model']} avec une conso de {data.loc[data['Combined (L/100 km)'].idxmax(), 'Combined (L/100 km)']}" )
print(f"LA plus grosse conso en mpg est {data.loc[data['Combined (mpg)'].idxmin(), 'Model']} avec une conso de {data.loc[data['Combined (mpg)'].idxmin() , 'Combined (mpg)']}")
#BREFFFFFF ICI ON CONSTATE DEJA QUE LA VOITURE QUI CONSOMME LE PLUS EN L/KM N'EST PAS CELLE QUI A LA MPG LA PLUS BASSE ====> PROBL7ME
'''
# Vérifier si la conversion entre mpg et L/100 km est cohérente
data['Calculated mpg'] = 235.21 / data['Combined (L/100 km)']

# Comparer la variable existante 'Combined (mpg)' avec la calculée
data['mpg_difference'] = abs(data['Combined (mpg)'] - data['Calculated mpg'])

# Résumer la différence
print(data['mpg_difference'].describe())

# Calculer la corrélation entre L/100 km et mpg
correlation = data['Combined (L/100 km)'].corr(data['Combined (mpg)'])
print(f"Corrélation entre Combined (L/100 km) et Combined (mpg) : {correlation}")

print(data.groupby('Fuel type')['mpg_difference'].mean())
print(data.groupby('Vehicle class')['mpg_difference'].mean())

import matplotlib.pyplot as plt

plt.hist(data['mpg_difference'], bins=30, edgecolor='black')
plt.title("Distribution des écarts entre mpg calculés et présents")
plt.xlabel("Différence (mpg)")
plt.ylabel("Fréquence")
plt.show()
'''
