'''DANS CE SCRIPT JE RASSEMBLE LES OUTILS DE VISUALISATION POUR ANALYSER LE JEU DE DONNEES'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#1. Mes fonctions de visualisations
def plot_correlation_heatmap(data):
    '''Doit construire une heat map de corrélation entre mes variables numériques'''
    plt.figure(figsize=(9, 9))
    num_values = data.select_dtypes(include=[float, int])
    correlation_matrix = num_values.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", \
                fmt=".2f", linewidths=0.7, linecolor='black')
    plt.title("Matrice de corrélation entre variables numériques")
    plt.tight_layout()
    plt.show()

def plot_multiple_histograms(data, variables):
    '''
    9 histogrammes pour 9 variables données

    Paramètres :
        variables : liste de 9 variables (colonne du dataset)
    '''
    if len(variables) != 9:
        raise ValueError("Cette fonction nécessite exactement 9 variables.")

    fig, axes = plt.subplots(3, 3, figsize=(16, 8))
    fig.suptitle("Histogrammes", fontsize=16)

    for i, variable in enumerate(variables):
        row = i // 3
        col = i % 3

        if pd.api.types.is_numeric_dtype(data[variable]):
            nb_bins = 30
        else:
            nb_bins = len(data[variable].unique())

        axes[row, col].hist(
            data[variable],
            bins=nb_bins,
            edgecolor='b',
            color='skyblue')
        axes[row, col].set_title(f"Distribution de {variable}")
        axes[row, col].set_xlabel(variable)
        axes[row, col].set_ylabel("Fréquence")
        axes[row, col].grid(axis='y', linestyle='--', alpha=0.7)
        axes[row, col].tick_params(axis='x', rotation=70)


    plt.tight_layout()
    plt.show()


def plot_multiple_scatters(data, variables_pairs):
    '''
    Doit afficher plusieurs scatter de 2 variables numériques

    Paramètres :
        variables (list of tuple) : Liste des paires de variables (x, y)
    '''
    if len(variables_pairs) != 6:
        raise ValueError("Cette fonction nécessite exactement 4 paires de variables.")

    fig, axes = plt.subplots(2, 3, figsize=(16 , 8))
    fig.suptitle("Scatterplots", fontsize=16)

    for i, (variable1, variable2) in enumerate(variables_pairs):
        row = i // 3
        col = i % 3
        sns.scatterplot(
            x=variable1,
            y=variable2,
            data=data,
            alpha=0.7,
            color='skyblue',
            edgecolor='black',
            ax=axes[row, col]
        )
        axes[row, col].set_title(f"{variable2} en fonction de {variable1}")
        axes[row, col].set_xlabel(variable1)
        axes[row, col].set_ylabel(variable2)
        axes[row, col].grid(alpha=0.5)

    plt.tight_layout()
    plt.show()

def plot_multiple_mean_bars(data, variable_pairs):
    '''
    Montre 6 graphiques en barres de la moyenne de variable 2(=numérique) par catégorie (variable 1)

    Paramètres :
        variable_pairs (list of tuple) : Liste des paires de variables (catégorielle, numérique)
    '''
    if len(variable_pairs) != 6:
        raise ValueError("Cette fonction nécessite exactement 4 paires de variables.")

    fig, axes = plt.subplots(2, 3, figsize=(16, 8))
    fig.suptitle("Moyenne en bars", fontsize=16)
    for i, (variable1, variable2) in enumerate(variable_pairs):
        row = i // 3
        col = i % 3
        mean_values = data.groupby(variable1)[variable2].mean().sort_values(ascending=False)

        mean_values.plot(
            kind='bar',
            ax=axes[row, col],
            color='skyblue',
            edgecolor='black'
        )
        axes[row, col].set_title(f"Moyenne de {variable2} par {variable1}")
        axes[row, col].set_xlabel(variable1)
        axes[row, col].set_ylabel(f"Moyenne de {variable2}")
        axes[row, col].tick_params(axis='x', rotation=70)

    plt.tight_layout()
    plt.show()

def plot_multiple_boxplots(data, variable_pairs):
    '''
    Affiche 4 boxplots 

    Paramètres :
        variable_pairs (list of tuple) : Liste des paires de variables (numérique, catégorielle)
    '''
    if len(variable_pairs) != 4:
        raise ValueError("Cette fonction nécessite exactement 4 paires de variables.")

    fig, axes = plt.subplots(2, 2, figsize=(16, 8))
    fig.suptitle("Boxplots", fontsize=16)

    for i, (variable1, variable2) in enumerate(variable_pairs):
        row = i // 2
        col = i % 2

        sns.boxplot(
            x=variable2,
            y=variable1,
            data=data,
            palette="Set1",
            ax=axes[row, col])

        axes[row, col].set_title(f"{variable1} par {variable2}")
        axes[row, col].set_xlabel(variable2)
        axes[row, col].set_ylabel(variable1)
        axes[row, col].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()


#2. Partie executable
DATA_PATH = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
vehicles = pd.read_csv(DATA_PATH)

#La heatmap
plot_correlation_heatmap(vehicles)

#Les histogrammes
histogram_variables= [
    'Model year', 'CO2 rating', 'Engine size (L)',
    'Cylinders', 'Transmission', 'Fuel type',
    'CO2 emissions (g/km)', 'Combined (L/100 km)', 'Combined (mpg)',]
plot_multiple_histograms(vehicles, histogram_variables)

#Les scatters
scatter_variables = [
    ('Combined (L/100 km)', 'Highway (L/100 km)'),
    ('Combined (L/100 km)', 'CO2 emissions (g/km)'),
    ('Combined (L/100 km)', 'Combined (mpg)'),
    ('CO2 emissions (g/km)', 'Engine size (L)'),
    ('Highway (L/100 km)', 'CO2 emissions (g/km)'),
    ('City (L/100 km)', 'CO2 emissions (g/km)')]
plot_multiple_scatters(vehicles, scatter_variables)

#Graphiques bar pour les moyennes
bar_mean_variables = [
    ('Vehicle class', 'CO2 emissions (g/km)'),
    ('Transmission', 'CO2 rating'),
    ('Transmission', 'CO2 emissions (g/km)'),
    ('Cylinders', 'Smog rating'),
    ('Model year', 'Combined (L/100 km)'),
    ('Fuel type', 'CO2 emissions (g/km)')]
plot_multiple_mean_bars(vehicles, bar_mean_variables)

#Les boxplots
boxplot_variables = [
    ('CO2 emissions (g/km)', 'Vehicle class'),
    ('CO2 rating', 'Fuel type'),
    ('CO2 emissions (g/km)', 'Model year'),
    ('Combined (L/100 km)', 'Transmission')]
plot_multiple_boxplots(vehicles, boxplot_variables)

#End-of-file
