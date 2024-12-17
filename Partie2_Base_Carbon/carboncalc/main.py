import pandas as pd
import matplotlib.pyplot as plt
import calculators as Cs

ALIMENTS_PATH = (
    "C:/Users/tapri/OneDrive/Bureau/Master_1/"
    "Python/Projet_Python/Partie2_Base_Carbon/aliments.csv"
)
ENERGIE_PATH = (
    "C:/Users/tapri/OneDrive/Bureau/Master_1/"
    "Python/Projet_Python/Partie2_Base_Carbon/energie.csv"
)
EQUIPEMENTS_PATH = (
    "C:/Users/tapri/OneDrive/Bureau/Master_1/"
    "Python/Projet_Python/Partie2_Base_Carbon/equipements.csv"
)

aliments = pd.read_csv(ALIMENTS_PATH)
energie = pd.read_csv(ENERGIE_PATH)
equipements = pd.read_csv(EQUIPEMENTS_PATH)
equipements['french_name'] = equipements['french_name'].replace('Réfrigétateur', 'Réfrigérateur')
equipements['french_name'] = equipements['french_name'].replace('Séche linge', 'Sèche-linge')

energie = energie[['french_name', 'CO2', 'unit']]
energie['unit'] = energie['unit'].str.replace("kgCO2e/", "")

#1. Calcul des émissions

print("\nBienvenue sur notre calcultateur d'empreinte carbonne !") 
facteur, periode = Cs.choisir_periode()
print("\nNotre outil existe en 2 versions.")
print(" 1. Une 1ere version simplifiée, qui vous prendra moins de 2 minutes à remplir.")
print(" 2. Et une 2eme version, plus longue mais avec une bien meilleure précision dans son résultat")

while True:
    choix_version = input("Quelle version souhaitez-vous utiliser (1 / 2) ? ").strip()
    if choix_version == "1":
        #1.1Calculateur simple
        print("\nVous avez choisi la version simplifiée.")
        aliments = aliments.groupby('main_type').agg({'CO2': 'mean'}).reset_index()
        aliments['unit']='kg'
        equipements= equipements.groupby('french_name').agg({'CO2': 'mean'}).reset_index()
        equipements['unit'] = 'unité'
        
        total, total_aliments, total_energie, total_equipements = Cs.calculer_empreinte_simple(aliments, energie, equipements, facteur)
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
        
        total, total_aliments, total_energie, total_equipements = Cs.calculer_empreinte_avance(aliments, energie, equipements, facteur)
        break
    else:
        print("Erreur : veuillez entrer '1' pour la version simplifiée ou '2' pour la version détaillée.")

print("\n~~~~~~~~ Résumé de vos émissions ~~~~~~~~")
print(f" - Aliments ({periode}) : {total_aliments:.2f} kgCO2e")
print(f" - Énergie ({periode}) : {total_energie:.2f} kgCO2e")
print(f" - Équipements ({periode}) : {total_equipements:.2f} kgCO2e")
print(f"\nVotre empreinte carbone totale estimée sur une période {periode} est de : {total:.2f} kgCO2e")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#CRER GRAPHIQUE CIRCULAIRE POURCENTAGE DES EMISSIONS
#PEUT ETRE FAIRE UNE VISUALISATION COMMUMNE AUX DEUX VERISONS
#2. Visualisations
import visualization as vz

vz.visualiser_emissions_bar(total_aliments, total_energie, total_equipements)
vz.visualiser_emissions_circulaire(total_aliments, total_energie, total_equipements)