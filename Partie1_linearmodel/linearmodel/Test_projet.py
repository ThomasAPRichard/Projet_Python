#FICHIER QUI NE DEVRA PAS ETRE DANS LE RENDU FINALE
#CE FICHIER SERT A TESTER DES TRUCS ET DECOUVRIR UN PEU LE TRUC

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)


import my_statistics

import matplotlib.pyplot as plt
import seaborn as sns



def plot_scatter(data, variable1, variable2): #Scatter de 2 variables numériques
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=variable1, y=variable2, data=data, alpha=0.7,color='skyblue', edgecolor='black')
    plt.title(f"{variable2} en fonction de {variable1}")
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.show()
plot_scatter(data,'CO2 emissions (g/km)', 'Combined (L/100 km)')