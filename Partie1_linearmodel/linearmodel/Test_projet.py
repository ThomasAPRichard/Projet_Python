#FICHIER QUI NE DEVRA PAS ETRE DANS LE RENDU FINALE
#CE FICHIER SERT A TESTER DES TRUCS ET DECOUVRIR UN PEU LE TRUC

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)

import my_statistics

print(my_statistics.variable1_distribution_by_variable2(data,'Vehicle class', 'Make'))
