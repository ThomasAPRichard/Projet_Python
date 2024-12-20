'''Script d'execution du calculateur'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import calculators as cs
import visualization as vz
import pandas as pd

aliments = pd.read_csv("aliments.csv")
energie = pd.read_csv("energie.csv")
equipements = pd.read_csv("equipements.csv")
equipements['french_name'] = equipements['french_name'].replace('Réfrigétateur', 'Réfrigérateur')
equipements['french_name'] = equipements['french_name'].replace('Séche linge', 'Sèche-linge')

energie = energie[['french_name', 'CO2', 'unit']]
energie['unit'] = energie['unit'].str.replace("kgCO2e/", "")

#1. Calcul des émissions
print("\nBienvenue sur notre calcultateur d'empreinte carbonne !")
facteur, periode = cs.choisir_periode()
print("\nNotre outil existe en 2 versions.")
print(" 1. Une 1ere version simplifiée, qui vous prendra moins de 2 minutes à remplir.")
print(" 2. Une 2eme version, plus longue mais avec une bien meilleure précision dans son résultat")

while True:
    choix_version = input("Quelle version souhaitez-vous utiliser (1 / 2) ? ").strip()
    if choix_version == "1":
        #1.1Calculateur simple

        print("\nVous avez choisi la version simplifiée.")
        aliments = aliments.groupby('main_type').agg({'CO2': 'mean'}).reset_index()
        aliments['unit']='kg'
        equipements= equipements.groupby('french_name').agg({'CO2': 'mean'}).reset_index()
        equipements['unit'] = 'unité'
        total, total_aliments, total_energie, total_equipements = cs.calculer_empreinte_simple(aliments, energie, equipements, facteur)
        break
    elif choix_version == "2":
        #1.2 Calculateur avancé

        print("\nVous avez choisi la version avancée.")
        aliments = aliments.groupby('french_name').agg({'CO2': 'mean', 'main_type': 'first', 'sous_type': 'first'}).reset_index()
        aliments = aliments[['main_type', 'sous_type', 'french_name', 'CO2']]
        aliments['unit']='kg'
        equipements['main_type'] = 'Electroménager'
        equipements = equipements[['main_type', 'french_name', 'complete_name', 'CO2']]
        equipements['unit'] = 'unité'
        total, total_aliments, total_energie, total_equipements = cs.calculer_empreinte_avance(aliments, energie, equipements, facteur)
        break
    else:
        print("Erreur : Entrez '1' pour la version simplifiée ou '2' pour la version avancée")

print("\n~~~~~~~~ Résumé de vos émissions ~~~~~~~~\n")
print(f" - Aliments ({periode}) : {total_aliments/1000:.2f} tonneCO2")
print(f" - Énergie ({periode}) : {total_energie/1000:.2f} tonneCO2")
print(f" - Équipements ({periode}) : {total_equipements/1000:.2f} tonneCO2")
print(f"\nVotre empreinte carbone totale estimée sur une période {periode} est de : {total/1000:.2f} tonneCO2")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


#2. Visualisations
vz.visualiser_emissions_2(total_aliments, total_energie, total_equipements)

# End-of-file
