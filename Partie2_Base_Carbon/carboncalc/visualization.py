#Mon script pour les visualisations des émissions du restaurateur
import pandas as pd
import matplotlib.pyplot as plt

def visualiser_emissions_bar(aliments_emission, energie_emission, equipements_emission):
    categories = ['Aliments', 'Énergie', 'Équipements']
    emissions = [aliments_emission, energie_emission, equipements_emission]
    
    plt.bar(categories, emissions)
    plt.title("Répartition des émissions de CO₂")
    plt.ylabel("Émissions (kgCO₂)")
    plt.show()

def visualiser_emissions_circulaire(aliments_emission, energie_emission, equipements_emission):
    categories = ['Aliments', 'Énergie', 'Équipements']
    emissions = [aliments_emission, energie_emission, equipements_emission]
    
    plt.figure(figsize=(8, 6))
    plt.pie(emissions, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Répartition des émissions de CO₂ par catégorie")
    plt.show()
