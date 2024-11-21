# DANS CE MODULE JE RASSEMBLE LES OUTILS STATISTIQUES POUR ANALYSER LE JEU DE DONNEES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1. MA LISTE DE FONCTIONS
def data_presentation (data) : #Cette fonction doit print les infos essentielles sur le dataset
    print(f"Le dataset présenté ici concerne les émissions de CO2 de {len(data['Model'])} différents véhicules, et provient du gouvernement du Canada.")    
    print(f"Il y a {len(data['Model'].unique())} modèles construis par {len(data['Make'].unique())} marques différentes entre l'année {sorted(data['Model year'].unique().tolist())[0]} et l'année {sorted(data['Model year'].unique().tolist())[-1]}.")
    print(f"Il est à noter que les données de <Smog rating> ne sont renseingées qu'àpartir de 2017, il manque donc {data['Smog rating'].isna().sum()} données sur {len(data['Model'])} pour cette variable.")
    print(f"De la même façon, la variable <CO2 rating> n'est renseignée qu'à partir de 2016, laissant donc {data['CO2 rating'].isna().sum()} véhicules sans valeur dans cette colonne")
    return 0

#1.1FONCTIONS ANALYSE PAR TYPE DE VARIABLE (variable = une colonne)
def co2_emisions_mean_by_variable(data, variable): # Calcule les moyennes des émissions de CO2 parr type de variable
    return data.groupby(variable)['CO2 emissions (g/km)'].mean().sort_values()
def co2_rating_mean_by_variable(data, variable): # Calcule les moyennes des notes de CO2 par type de variable.
    return data.dropna(subset=['CO2 rating']).groupby(variable)['CO2 rating'].mean().sort_values()
def smog_rating_mean_by_variable(data, variable): # Calcule les moyennes des note de pollutions parr type de variable.
    return data.dropna(subset=['Smog rating']).groupby(variable)['Smog rating'].mean().sort_values()
def consumption_mean_by_variable(data, variable): # Calcule des moyennes de consommation en ville, sur autoroute et combinée 
    return data.groupby(variable)[['City (L/100 km)', 'Highway (L/100 km)', 'Combined (L/100 km)']].mean()
def variable1_distribution_by_variable2(data, variable1, variable2): #Analyse la distribution de la variable 2 pour chaque éléments unique de la variable1
    return data.groupby(variable1)[variable2].describe()




# 2. PARTIE EXECUTABLE
if __name__ == "__main__":

    data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
    data = pd.read_csv(data_path)

    data_presentation(data)

    #CREATION DE NOUVELLES VARIABLES
    '''Pour l'instant elles sont un peu intules'''
    #data['City/Highway ratio'] = data['City (L/100 km)'] / data['Highway (L/100 km)'] #Conso ville / autoroute
    #data['CO2/Smog ratio'] = data['CO2 emissions (g/km)'] / data['Smog rating'] #Emissions CO2 / Smog

    print("Voici une liste de tableaux qui donnent de bonnes premières indications sur le dataset")

    print("\nConsommations moyenne en ville, sur autoroute et en combinée, par type de véhicules :\n", consumption_mean_by_variable(data,'Vehicle class'))
    print("\nEmissions moyenne de CO2 par type de véhicules :\n", co2_emisions_mean_by_variable(data,'Vehicle class'))
    print("\nNote environmentale sur le CO2 par type de véhicules (après 2016) :\n", co2_rating_mean_by_variable(data,'Vehicle class'))
    print("\nNote environmentale sur la pollution par type de véhicules (après 2017) :\n", smog_rating_mean_by_variable(data,'Vehicle class'))

    print("\nConsommations moyenne en ville, sur autoroute et en combinée, par type de carburant :\n", consumption_mean_by_variable(data,'Fuel type'))
    print("\nEmissions moyenne de CO2 par type de carburant :\n", co2_emisions_mean_by_variable(data,'Fuel type'))
    print("\nNote environmentale sur le CO2 par type de carburant (après 2016) :\n", co2_rating_mean_by_variable(data,'Fuel type'))
    print("\nNote environmentale sur la pollution par type de carburant (après 2017) :\n", smog_rating_mean_by_variable(data,'Fuel type'))

    '''
    print("\nConsommations moyenne en ville, sur autoroute et en combinée, par nombre de cylindres :\n", consumption_mean_by_variable(data, 'Cylinders'))
    print("\nEmissions moyenne de CO2 par nombre de cylindres :\n", co2_emisions_mean_by_variable(data, 'Cylinders'))
    print("\nNote environmentale sur le CO2 par nombre de cylindres (après 2016) :\n", co2_rating_mean_by_variable(data, 'Cylinders'))
    print("\nNote environmentale sur la pollution par nombre de cylindres (après 2017) :\n", smog_rating_mean_by_variable(data, 'Cylinders'))
    '''

    
