# DANS CE SCRIPT JE RASSEMBLE LES OUTILS DE VISUALISATION POUR ANALYSER LE JEU DE DONNEES

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#1. MES FONCTIONS DE VISUALISATIONS

def plot_histogram(data, variable): #Créer un histogramme pour une variable donnée
    if pd.api.types.is_numeric_dtype(data[variable]):
        nb_bins = 30
    else:
        nb_bins = len(data[variable].unique())
    plt.figure(figsize=(8, 6))
    plt.hist(data[variable], bins=nb_bins, edgecolor='b', color='skyblue')
    plt.title(f"Distribution de {variable}")
    plt.xlabel(variable)
    plt.ylabel("Fréquence")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_boxplot(data, variable1, variable2): #Boxplot de la variable1 par la variable 2 // ATTENTION : variable1 = numérique, var2 = catégorielle
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=variable2, y=variable1, data=data, palette="Set1")
    plt.title(f"{variable1} par {variable2}")
    plt.xlabel(variable2)
    plt.ylabel(variable1)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(data): #Doit construire une heat map de corrélation entre mes variables numériques
    plt.figure(figsize=(12, 10))
    num_values = data.select_dtypes(include=[float, int])
    correlation_matrix = num_values.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.7, linecolor='black')
    plt.title("Matrice de corrélation entre variables numériques")
    plt.tight_layout()
    plt.show()

def plot_bar(data, variable1, variable2): #Graphique en bar de la moyenne de variable 2(=numérique) par catégorie (variable 1)
    mean_values = data.groupby(variable1)[variable2].mean().sort_values(ascending=False)
    mean_values.plot(kind='bar', figsize=(10, 6), color='skyblue', edgecolor='black')
    plt.title(f"Moyenne de {variable2} par {variable1}")
    plt.xlabel(variable1)
    plt.ylabel(f"Moyenne de {variable2}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_scatter(data, variable1, variable2): #Scatter de 2 variables numériques
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=variable1, y=variable2, data=data, alpha=0.7,color='skyblue', edgecolor='black')
    plt.title(f"{variable2} en fonction de {variable1}")
    plt.xlabel(variable1)
    plt.ylabel(variable2)
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.show()

#2. PARTIE EXECUTABLE
data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)
#La heatmap
plot_correlation_heatmap(data)
#Histogramme
plot_histogram(data,'CO2 emissions (g/km)')
plot_histogram(data,'Combined (L/100 km)')
plot_histogram(data,'Fuel type')
#Boxplot
plot_bar(data, 'Model year', 'CO2 emissions (g/km)')
plot_boxplot(data, 'CO2 emissions (g/km)', 'Vehicle class')
plot_boxplot(data, 'CO2 rating', 'Make')
#Graphique bar des moyennes
plot_bar(data, variable1='Vehicle class', variable2='CO2 emissions (g/km)')
plot_bar(data, variable1='Engine size (L)', variable2='CO2 rating')
plot_bar(data, 'Make', 'Smog rating')
#Scatter
plot_scatter(data, variable1='City (L/100 km)', variable2='Highway (L/100 km)') #changer
plot_scatter(data, variable1='Combined (L/100 km)', variable2='CO2 emissions (g/km)')
plot_scatter(data, 'Combined (L/100 km)', 'Combined (mpg)')


