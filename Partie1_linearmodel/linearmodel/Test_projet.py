#FICHIER QUI NE DEVRA PAS ETRE DANS LE RENDU FINALE
#CE FICHIER SERT A TESTER DES TRUCS ET DECOUVRIR UN PEU LE TRUC

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)


import my_statistics

data['Eco-efficiency index'] = data['Combined (L/100 km)'] * data['CO2 emissions (g/km)'] #Indicateur global d'efficacité écologique des véhicules
best_make_ecoefficiency= data.groupby('Make')['Eco-efficiency index'].mean()
print(f"Le constructeur qui obtient la meilleure note pour notre Eco-efficiency index est {best_make_ecoefficiency.idxmin()} avec une note de {round(best_make_ecoefficiency.min(),0)}")