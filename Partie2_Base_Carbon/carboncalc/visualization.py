'''Mon script pour les visualisations des émissions du restaurateur'''

import matplotlib.pyplot as plt

def visualiser_emissions_bar(aliments_emission, energie_emission, equipements_emission):
    '''
    Affiche un graphique à barres représentant la répartition des émissions de CO₂.

    Paramètres :
        aliments_emission (float) : Émissions de CO₂ pour la catégorie Aliments.
        energie_emission (float) : Émissions de CO₂ pour la catégorie Énergie.
        equipements_emission (float) : Émissions de CO₂ pour la catégorie Équipements.

    Retourne :
        None
    '''
    categories = ['Aliments', 'Énergie', 'Équipements']
    emissions = [aliments_emission, energie_emission, equipements_emission]

    plt.bar(categories, emissions)
    plt.title("Répartition des émissions de CO₂")
    plt.ylabel("Émissions (kgCO₂)")
    plt.show()


def visualiser_emissions_circulaire(aliments_emission, energie_emission, equipements_emission):
    '''
    Affiche un graphique circulaire représentant la répartition des émissions de CO₂ par catégorie.

    Paramètres :
        aliments_emission (float) : Émissions de CO₂ pour la catégorie Aliments.
        energie_emission (float) : Émissions de CO₂ pour la catégorie Énergie.
        equipements_emission (float) : Émissions de CO₂ pour la catégorie Équipements.

    Retourne :
        None
    '''
    categories = ['Aliments', 'Énergie', 'Équipements']
    emissions = [aliments_emission, energie_emission, equipements_emission]

    plt.figure(figsize=(8, 6))
    plt.pie(emissions, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des émissions de CO₂ par catégorie")
    plt.show()

# End-of-file (EOF)
