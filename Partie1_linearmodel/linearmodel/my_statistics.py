''' DANS CE SCRIPT JE RASSEMBLE LES OUTILS STATISTIQUES POUR ANALYSER LE JEU DE DONNEES'''

import pandas as pd

#1. MA LISTE DE FONCTIONS
def data_presentation (data) :
    '''Cette fonction doit print les infos essentielles sur le dataset'''
    print(f"Le dataset présenté ici concerne les émissions de CO2 de {len(data['Model'])} "
          "différents véhicules, et provient du gouvernement du Canada.")    
    print(f"Il y a {len(data['Model'].unique())} modèles construis par {len(data['Make'].unique())}"
          f"marques différentes entre l'année {sorted(data['Model year'].unique().tolist())[0]} "
          f"et l'année {sorted(data['Model year'].unique().tolist())[-1]}.")
    print(f"Il est à noter que les données de <Smog rating> ne sont renseignées qu'à partir de "
          f"2017,il manque donc {data['Smog rating'].isna().sum()} données "
          f"sur {len(data['Model'])} pour cette variable.")
    print(f"De la même façon, la variable <CO2 rating> n'est renseignée qu'à partir de 2016, "
          f"laissant donc {data['CO2 rating'].isna().sum()} véhicules sans valeur "
          "dans cette colonne")
    print("\nEnfin, voici les données essentielles du dataset :")
    print(data.describe())
    print("\n~~~~~~~~~~~~~~~~~~~~~~~")
    return 0

def variable1_mean_by_variable2(data, variable1, variable2):
    '''Calcule les moyennes de variable 1 pour chaque éléments unique de variable 2'''
    return data.dropna(subset=[variable1]).groupby(variable2)[variable1].mean().sort_values()
def consumption_mean_by_variable(data, variable):
    '''Calcule des moyennes de consommation en ville, sur autoroute et combinée''' 
    return data.groupby(variable)\
        [['City (L/100 km)', 'Highway (L/100 km)', 'Combined (L/100 km)']].mean()
def variable1_distribution_by_variable2(data, variable1, variable2):
    '''Analyse la distribution de la variable 2 pour chaque éléments unique de la variable1'''
    return data.dropna(subset=[variable1]).groupby(variable2)[variable1].describe()

#2. PARTIE EXECUTABLE
DATA_PATH = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
vehicles = pd.read_csv(DATA_PATH)

data_presentation(vehicles)

#PROBLEME DE CORRELATION 'Combined (L/100 km)' et 'Combined (mpg)'
print('\nIl y a un problème avec les variables Combined (L/100 km) et Combined (mpg)')
correlation_conso = vehicles['Combined (L/100 km)'].corr(vehicles['Combined (mpg)'])
print("En effet, nous devrions observer une corrélation de -1 entre elles, alors qu'avec"
      f" notre dataset nous obtenons une corrélation de {correlation_conso}")
vehicles['Calculated mpg'] = 235.21 / vehicles['Combined (L/100 km)']
vehicles['mpg_difference'] = abs(vehicles['Combined (mpg)'] - vehicles['Calculated mpg'])
print(f"Il y a en moyenne une différence de {round(vehicles['mpg_difference'].mean(),2)} "
      "entre la consommation en mpg observée dans la dataset et celle que nous devrions "
      "obtenir si cette derniere était exactement corrélée à la consommation en L/100 km")
print("A titre d'exemple :")
print(f"La plus grosse conso au L/km est "
      f"{vehicles.loc[vehicles['Combined (L/100 km)'].idxmax(), 'Model']} avec une conso de "
      f"{vehicles.loc[vehicles['Combined (L/100 km)'].idxmax(), 'Combined (L/100 km)']}")
print(f"La plus grosse conso en mpg est "
      f"{vehicles.loc[vehicles['Combined (mpg)'].idxmin(), 'Model']} avec "
      f"une conso de {vehicles.loc[vehicles['Combined (mpg)'].idxmin() , 'Combined (mpg)']}")
print("Malgré plusieurs essais, je ne suis pas parvenu à déterminer d'où pouvait provenir ce "
      "problème, mais il est à garder en tête pour la suite")
print("\n~~~~~~~~~~~~~~~~~~~~~~~")

#CREATION et SUPPRESSION DE VARIABLES
vehicles['City/Highway ratio'] = \
    vehicles['City (L/100 km)'] / vehicles['Highway (L/100 km)']
vehicles['Fuel/cylinders efficiency'] = vehicles['Combined (L/100 km)'] / vehicles['Cylinders']
vehicles['Emissions/cylinders efficiency'] = vehicles['CO2 emissions (g/km)']/vehicles['Cylinders']
vehicles['Eco-efficiency index'] = vehicles['Combined (L/100 km)']*vehicles['CO2 emissions (g/km)']

#QUELQUES DONNEES SUR LE DATASET
print("\nNous avons créé 4 nouvelles variables :")
print("-'City/Highway ratio' ratio de la conso de carburant ville / ")
print("-'Fuel/Cylinders efficiency', Ratio Consommation de carburant / nombre de cylindre")
print("-'Emissions/cylinders efficiency', Émissions de CO2 par cylindre")
print("-'Eco-efficiency index', qui est un indicateur global d'efficacité écologique des "
      "véhicules calculé comme suit : Consomation combinée x Emissions de CO2")
print("\n~~~~~~~~~~~~~~~~~~~~~~~")

print("\nVoici quelqes informations qui donnent de bonnes premières indications sur le dataset")
print("\nConsommations moyenne en ville, sur autoroute et en combinée, par type de véhicules "
      ":\n", consumption_mean_by_variable(vehicles,'Vehicle class'))
print("\nEmissions moyenne de CO2 par type de carburant :\n"
      , variable1_mean_by_variable2(vehicles,'CO2 emissions (g/km)','Fuel type'))
print("\nNote environmentale moyenne sur la pollution (smog) par Constructeur automobile "
      "(après 2017):\n", variable1_mean_by_variable2(vehicles,'Smog rating','Make'))
print("\nDistribution de la note environmentale sur le CO2 par nombre de cylindres "
      "(après 2016) :\n", variable1_distribution_by_variable2(vehicles,'CO2 rating' , 'Cylinders'))
print("\n~~~~~~~~~~~~~~~~~~~~~~~")

ratio_by_class = vehicles.groupby('Vehicle class')\
    ['City/Highway ratio'].mean().sort_values(ascending=False)
print(f"\nLa classe de véhicules qui est la moins optimisée à la conduite en ville par rapport "
      f"à l'autoroute est {ratio_by_class.idxmax()}, avec un City/Highway ratio "
      f"de {round(ratio_by_class.max(),2)}")
best_emissions_cylinder = vehicles.loc[vehicles['Emissions/cylinders efficiency'].idxmin()]
print(f"Le véhicule qui émet le moins de CO2 par cylindre est {best_emissions_cylinder['Model']} "
      f"de {best_emissions_cylinder['Make']}, avec "
      f"{round(best_emissions_cylinder['Emissions/cylinders efficiency'],2)} "
      "g de CO2 par km et par cylindre")
best_conso_cylinder = vehicles.loc[vehicles['Fuel/cylinders efficiency'].idxmax()]
print(f"Le véhicule qui consomme le plus de carburant au km par cylindre est "
      f"{best_conso_cylinder['Model']} "
      f"de {best_conso_cylinder['Make']}, avec "
      f"{round(best_conso_cylinder['Emissions/cylinders efficiency'],2)} "
      "g de CO2 par km et par cylindre")
best_make_ecoefficiency= vehicles.groupby('Make')['Eco-efficiency index'].mean()
print(f"Le constructeur qui obtient la meilleure note pour notre Eco-efficiency index "
      f"est {best_make_ecoefficiency.idxmin()} avec une note de "
      f"{round(best_make_ecoefficiency.min(),0)}")

#End-of-file
