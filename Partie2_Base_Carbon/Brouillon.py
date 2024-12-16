#PARTIE BROUILLON A NE PAS RENDRE

import pandas as pd
import matplotlib.pyplot as plt

def collecte_donnees(dataframe, categorie):
    total_emission = 0
    for _, row in dataframe.iterrows():
        while True:
            try:
                quantite = float(input(f"Entrez la quantité pour {row.iloc[0]} ({row.iloc[2]}): "))
                if quantite < 0:
                    print("La quantité ne peut pas être négative. Réessayez.")
                    continue
                emission = quantite * row.iloc[1]
                total_emission += emission
                break
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre valide.")
    return total_emission

def calculer_empreinte(aliments, energie, equipements):
    print("Bienvenu sur notre outil pour calculer votre empreinte carbone annuelle :\n")
    
    print("Commencez par rentrer vos quantités achetées pour la catégorie Aliments")
    total_aliments = collecte_donnees(aliments, "Aliments")
    print("\nPuis rentrer vos quantités consommées pour la catégorie Énergie")
    total_energie = collecte_donnees(energie, "Énergie")
    print("\nEt enfin rentrer vos quantités achetées pour la catégorie Équipements")
    total_equipements = collecte_donnees(equipements, "Équipements")
    
    total = total_aliments + total_energie + total_equipements
    print("\nMerci d'avoir rempli ce questionnaire !")
    return total, total_aliments, total_energie, total_equipements

def visualiser_emissions(aliments_emission, energie_emission, equipements_emission):
    categories = ['Aliments', 'Énergie', 'Équipements']
    emissions = [aliments_emission, energie_emission, equipements_emission]
    
    plt.bar(categories, emissions)
    plt.title("Répartition des émissions de CO₂")
    plt.ylabel("Émissions (kgCO₂)")
    plt.show()

if __name__ == "__main__":
    aliments_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie2_Base_Carbon/aliments.csv"
    energie_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie2_Base_Carbon/energie.csv"
    equipements_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie2_Base_Carbon/equipements.csv"

    aliments = pd.read_csv(aliments_path)
    energie = pd.read_csv(energie_path)
    equipements = pd.read_csv(equipements_path)
    equipements['french_name'] = equipements['french_name'].replace('Réfrigétateur', 'Réfrigérateur')
    equipements['french_name'] = equipements['french_name'].replace('Séche linge', 'Sèche-linge')

    aliments = aliments.groupby('main_type').agg({'CO2': 'mean'}).reset_index()
    aliments['unit']='kg'
    energie = energie[['french_name', 'CO2', 'unit']]
    energie['unit'] = energie['unit'].str.replace("kgCO2e/", "")
    equipements= equipements.groupby('french_name').agg({'CO2': 'mean'}).reset_index()
    equipements['unit'] = 'par unité'
    
    total, t_a, t_en, t_eq =calculer_empreinte(aliments, energie, equipements)
    print(f"Votre empreinte carbone totale est : {total:.2f} kgCO2e")
    visualiser_emissions(t_a, t_en, t_eq)