#CE SCRIPT RASSEMBLE LES DEUX VERISONS DU CALCULATEUR

import pandas as pd

#Une fonction pour que notre utilisateur choisisse sa période d'estimation
def choisir_periode():
    while True:
        print("\nPour votre évaluation, merci de saisir vos quantités consommée ANNUELLES.")
        print("Souhaitez-vous obtenir une estimation sur une période :")
        print("1. Annuelle")
        print("2. Mensuelle")
        print("3. Hebdomadaire")
        
        choix = input("Entrez le numéro de votre choix (1/2/3) : ").strip()
        if choix == "1":
            return 1, "annuelle"
        elif choix == "2":
            return 12, "mensuelle"
        elif choix == "3":
            return 52, "hebdomadaire"
        else:
            print("Entrée invalide. Veuillez choisir entre 1, 2 ou 3.")

#Une fonction pour adapter les calculateurs au choix de période du restaurateur
def ajuster_emissions(facteur, total_aliments, total_energie, total_equipements):
    total_aliments /= facteur
    total_energie /= facteur
    total_equipements /= facteur
    total = total_aliments + total_energie + total_equipements
    return total, total_aliments, total_energie, total_equipements


#Un calculateur qui demande peu d'entrées au restaurateur.
def collecte_donnees_simple(dataframe):
    total_emission = 0
    for _, row in dataframe.iterrows():
        while True:
            try:
                quantite = float(input(f"Entrez la quantité pour {row.iloc[0]} (en {row.iloc[2]}): "))
                if quantite < 0:
                    print("La quantité ne peut pas être négative. Réessayez.")
                    continue
                emission = quantite * row.iloc[1]
                total_emission += emission
                print(f"Votre empreinte carbone annuelle pour cette entrée est {emission:.2f} kgCO2e")
                break
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre valide.")
    return total_emission

def calculer_empreinte_simple(aliments, energie, equipements, facteur):
    print("\n-------------")
    print("Commencez par rentrez vos quantités achetées pour la catégorie Aliments")
    total_aliments = collecte_donnees_simple(aliments)
    print("\n-------------")
    print("Puis rentrez vos quantités consommées pour la catégorie Énergie")
    total_energie = collecte_donnees_simple(energie)
    print("\n-------------")
    print("Et enfin rentrez le nombre de matériel utilisé pour la catégorie Équipements")
    total_equipements = collecte_donnees_simple(equipements)
    print("\nMerci d'avoir rempli ce questionnaire !")

    total, total_aliments, total_energie, total_equipements = ajuster_emissions(facteur, total_aliments, total_energie, total_equipements)
    
    return total, total_aliments, total_energie, total_equipements


#Un calcultateur avancé, qui demande + de temps à remplir
def collecte_donnees_avance(dataframe):
    total_emission = 0
    main_types = dataframe.iloc[:,0].unique()
    for main_type in main_types:
        while True:
            choix_main_type = input(f"Avez-vous acheté des produits dans '{main_type}' ? (O/N) : ").strip().upper()
            if choix_main_type in ['O', 'N']:
                break
            print("    Réponse invalide. Veuillez répondre par 'O' pour oui ou 'N' pour non.")
        if choix_main_type == 'N':
            continue
        
        sous_types = dataframe[dataframe.iloc[:, 0] == main_type].iloc[:, 1].unique()
        for sous_type in sous_types:
            while True:
                choix_sous_type = input(f"  Parmi les {main_type}, avez-vous acheté des produits dans '{sous_type}' ? (O/N) : ").strip().upper()
                if choix_sous_type in ['O', 'N']:
                    break
                print("    Réponse invalide. Veuillez répondre par 'O' pour oui ou 'N' pour non.")
            if choix_sous_type == 'N':
                continue
            french_names = dataframe[(dataframe.iloc[:, 0] == main_type) &
                                     (dataframe.iloc[:, 1] == sous_type)]
            for _, row in french_names.iterrows():
                while True:
                    try:
                        quantite = float(input(f"    Entrez la quantité pour {row.iloc[2]} (en {row.iloc[4]}) : "))
                        if quantite < 0:
                            print("    La quantité ne peut pas être négative. Réessayez.")
                            continue
                        emission = quantite * row['CO2']
                        total_emission += emission
                        print(f"    Votre empreinte carbone annuelle pour cette entrée est {emission:.2f} kgCO2e")
                        break
                    except ValueError:
                        print("    Entrée invalide. Veuillez entrer un nombre valide.")
    return total_emission

def calculer_empreinte_avance(aliments, energie, equipements, facteur):
    print("\n-------------")
    print("Commencez par rentrez vos quantités d'aliment achetées.")
    total_aliments = collecte_donnees_avance(aliments)
    print("\n-------------")
    print("Puis rentrez vos quantités d'énergie consommées.")
    total_energie = collecte_donnees_simple(energie)
    print("\n-------------")
    print("Et enfin rentrez le nombre d'équipements que vous utilisez.")
    total_equipements = collecte_donnees_avance(equipements)
    print("\nMerci d'avoir rempli ce questionnaire !")

    total, total_aliments, total_energie, total_equipements = ajuster_emissions(facteur, total_aliments, total_energie, total_equipements)
    
    return total, total_aliments, total_energie, total_equipements