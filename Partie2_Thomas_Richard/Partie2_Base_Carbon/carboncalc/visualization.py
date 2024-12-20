'''Mon script pour les visualisations des émissions du restaurateur'''

import matplotlib.pyplot as plt

def visualiser_emissions_2(total_aliments, total_energie, total_equipements):
    '''
    Affiche les visualisations des émissions (barres et circulaire) sur le même graphique.

    Paramètres :
        total_aliments (float) : Émissions de CO₂ pour les aliments.
        total_energie (float) : Émissions de CO₂ pour l'énergie.
        total_equipements (float) : Émissions de CO₂ pour les équipements.

    Retourne :
        None
    '''
    categories = ['Aliments', 'Énergie', 'Équipements']
    emissions = [total_aliments, total_energie, total_equipements]

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].bar(categories, emissions, color=['blue', 'red', 'green'])
    axes[0].set_title("Répartition des émissions de CO2")
    axes[0].set_ylabel("Émissions (kgCO₂)")

    axes[1].pie(emissions, labels=categories, autopct='%1.1f%%', colors=['blue', 'red', 'green'])
    axes[1].set_title("Répartition des émissions de CO2")

    plt.tight_layout()
    plt.show()

#End-of-file
