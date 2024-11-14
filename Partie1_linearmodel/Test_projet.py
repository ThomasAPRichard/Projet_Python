#FICHIER QUI NE DEVRA PAS ETRE DANS LE RENDU FINALE
#CE FICHIER SERT A TESTER DES TRUCS ET DECOUVRIR UN PEU LE TRUC

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)

# Histogramme pour la variable 'Emission de CO2'
plt.hist(data['CO2 emissions (g/km)'], bins=30, edgecolor='black')
plt.title("Distribution des émissions de CO2")
plt.xlabel("Emission de CO2 (g/km)")
plt.ylabel("Fréquence")
plt.show()

sns.boxplot(x=data['CO2 emissions (g/km)'])
plt.title("Boxplot des émissions de CO2")
plt.show()