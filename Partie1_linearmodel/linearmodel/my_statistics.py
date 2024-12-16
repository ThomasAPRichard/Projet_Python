# DANS CE SCRIPT JE RASSEMBLE LES OUTILS STATISTIQUES POUR ANALYSER LE JEU DE DONNEES

import pandas as pd
import numpy as np

data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)

#1. MA LISTE DE FONCTIONS
def data_presentation (data) : #Cette fonction doit print les infos essentielles sur le dataset
    print(f"Le dataset présenté ici concerne les émissions de CO2 de {len(data['Model'])} différents véhicules, et provient du gouvernement du Canada.")    
    print(f"Il y a {len(data['Model'].unique())} modèles construis par {len(data['Make'].unique())} marques différentes entre l'année {sorted(data['Model year'].unique().tolist())[0]} et l'année {sorted(data['Model year'].unique().tolist())[-1]}.")
    print(f"Il est à noter que les données de <Smog rating> ne sont renseingées qu'àpartir de 2017, il manque donc {data['Smog rating'].isna().sum()} données sur {len(data['Model'])} pour cette variable.")
    print(f"De la même façon, la variable <CO2 rating> n'est renseignée qu'à partir de 2016, laissant donc {data['CO2 rating'].isna().sum()} véhicules sans valeur dans cette colonne")
    return 0

def variable1_mean_by_variable2(data, variable1, variable2): # Calcule les moyennes de variable 1 pour chaque éléments unique de variable 2
    return data.dropna(subset=[variable1]).groupby(variable2)[variable1].mean().sort_values()
def consumption_mean_by_variable(data, variable): # Calcule des moyennes de consommation en ville, sur autoroute et combinée 
    return data.groupby(variable)[['City (L/100 km)', 'Highway (L/100 km)', 'Combined (L/100 km)']].mean()
def variable1_distribution_by_variable2(data, variable1, variable2): #Analyse la distribution de la variable 2 pour chaque éléments unique de la variable1
    return data.dropna(subset=[variable1]).groupby(variable2)[variable1].describe()

#2. PARTIE EXECUTABLE
data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)

data_presentation(data)

#PROBLEME DE CORRELATION 'Combined (L/100 km)' et 'Combined (mpg)'
print('\nIl y a un problème avec les variables Combined (L/100 km) et Combined (mpg)')
correlation_conso = data['Combined (L/100 km)'].corr(data['Combined (mpg)'])
print(f"En effet, nous devrions observer une corrélation de -1 entre elles, alors qu'avec notre dataset nous obtenons une corrélation de {correlation_conso}")
data['Calculated mpg'] = 235.21 / data['Combined (L/100 km)']
data['mpg_difference'] = abs(data['Combined (mpg)'] - data['Calculated mpg'])
print(f"Il y a en moyenne une différence de {round(data['mpg_difference'].mean(),2)} entre la consommation en mpg observée dans la dataset et celle que nous devrions obtenir si cette derniere été corrélée exactement à la consommation en L/100 km")
print("A titre d'exemple :")
print(f"La plus grosse conso au L/km est {data.loc[data['Combined (L/100 km)'].idxmax(), 'Model']} avec une conso de {data.loc[data['Combined (L/100 km)'].idxmax(), 'Combined (L/100 km)']}" )
print(f"LA plus grosse conso en mpg est {data.loc[data['Combined (mpg)'].idxmin(), 'Model']} avec une conso de {data.loc[data['Combined (mpg)'].idxmin() , 'Combined (mpg)']}")
print("Malgré plusieurs essais, je ne suis pas parvenu à déterminer d'où pouvait provenir ce problème, mais il est à garder en tête pour la suite")

#CREATION et SUPPRESSION DE VARIABLES
data['City/Highway ratio'] = data['City (L/100 km)'] / data['Highway (L/100 km)'] #ratio de la conso de carburant ville / autoroute
data['Fuel/cylinders efficiency'] = data['Combined (L/100 km)'] / data['Cylinders'] # Ratio Consommation de carburant / nombre de cylindre
data['Emissions/cylinders efficiency'] = data['CO2 emissions (g/km)'] / data['Cylinders'] #Émissions de CO2 par cylindre.
data['Eco-efficiency index'] = data['Combined (L/100 km)'] * data['CO2 emissions (g/km)'] #Indicateur global d'efficacité écologique des véhicules

#QUELQUES DONNEES SUR LE DATASET
print("Nous avons créé 4 nouvelles variables : 'City/Highway ratio' ratio de la conso de carburant ville / autoroute,\n'Fuel/Cylinders efficiency', Ratio Consommation de carburant / nombre de cylindre\n")
print("'Emissions/cylinders efficiency', Émissions de CO2 par cylindre \nEt enfin 'Eco-efficiency index', qui est un indicateur global d'efficacité écologique des véhicules calculé comme suit : Consomation combinée x Emissions de CO2")
print("Voici quelqes informations qui donnent de bonnes premières indications sur le dataset")
print("\nConsommations moyenne en ville, sur autoroute et en combinée, par type de véhicules :\n", consumption_mean_by_variable(data,'Vehicle class'))
print("\nEmissions moyenne de CO2 par type de carburant :\n", variable1_mean_by_variable2(data,'CO2 emissions (g/km)','Fuel type'))
print("\nNote environmentale moyenne sur la pollution (smog) par Constructeur automobile (après 2017) :\n", variable1_mean_by_variable2(data,'Smog rating','Make'))
print("\nDistribution de la note environmentale sur le CO2 par nombre de cylindres (après 2016) :\n", variable1_distribution_by_variable2(data,'CO2 rating' , 'Cylinders'))
ratio_by_class = data.groupby('Vehicle class')['City/Highway ratio'].mean().sort_values(ascending=False)
print(f"La classe de véhicules qui est la moins optimisée à la conduite en ville par rapport à l'autoroute est {ratio_by_class.idxmax()}, avec un City/Highway ratio de {round(ratio_by_class.max(),2)}")
best_emissions_cylinder = data.loc[data['Emissions/cylinders efficiency'].idxmin()]
print(f"Le véhicules qui émet le moins de CO par cylindre est {best_emissions_cylinder['Model']} de {best_emissions_cylinder['Make']}, avec {round(best_emissions_cylinder['Emissions/cylinders efficiency'],2)} g de CO2 par km et par cylindre")
best_conso_cylinder = data.loc[data['Fuel/cylinders efficiency'].idxmax()]
print(f"Le véhicules qui consomme le plus de carburant au km par cylindre est {best_conso_cylinder['Model']} de {best_conso_cylinder['Make']}, avec {round(best_conso_cylinder['Emissions/cylinders efficiency'],2)} g de CO2 par km et par cylindre")
best_make_ecoefficiency= data.groupby('Make')['Eco-efficiency index'].mean()
print(f"Le constructeur qui obtient la meilleure note pour notre Eco-efficiency index est {best_make_ecoefficiency.idxmin()} avec une note de {round(best_make_ecoefficiency.min(),0)}")