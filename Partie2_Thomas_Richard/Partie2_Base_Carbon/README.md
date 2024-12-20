#Calculateur d'Empreinte Carbone pour Restaurateurs

##Description
Ce projet implémente un calculateur d'empreinte carbone destiné aux restaurateurs. Il permet d'estimer les émissions de CO₂ en fonction des quantités consommées dans trois catégories :

-Aliments
-Énergie
-Équipements

L'utilisateur peut choisir entre deux versions du calculateur :

-Version simplifiée : Saisie rapide pour une estimation approximative.
-Version avancée : Saisie détaillée pour une estimation précise.
Les résultats sont ajustables selon la période sélectionnée (annuelle, mensuelle ou hebdomadaire) et visualisés grâce à des graphiques.


##Structure du Projet
Le projet est organisé ainsi :

Partie 2_Base_Carbon/
│
├── carboncalc/                 # Package principal
│   ├── __init__.py             # Rend le package importable
│   ├── main.py                 # Programme principal \\ EXECUTABLE
│   ├── calculators.py          # Fonctions pour les calculs des émissions
│   ├── visualization.py        # Fonctions pour la visualisation des résultats
│   ├── aliments.csv            #Dataset1
│   ├── energie.csv             #Dataset2
│   └── equipements.csv         #Dataset3
│
├── tests/                      # Tests unitaires avec pytest
│   ├── __init__.py
│   ├── test_calculators.py     # Tests pour calculators.py
│   └── test_visualization.py   # Tests pour visualization.py
│
└── README.md                   # Documentation du projet

##Note pylint :
main = 9,2
calculators = 9,29
visualization = 10
test_visualization = 8,33
test_calculators = 8,75

##Prérequis
Python 3.8+
Librairies Python nécessaires :
numpy
pandas
matplotlib
pytest

##Données Utilisées
Les données proviennent de la Base Carbone ADEME et sont organisées en trois fichiers :

-aliments.csv : Facteurs d'émissions pour les aliments.
-energie.csv : Facteurs d'émissions pour les sources d'énergie.
-equipements.csv : Facteurs d'émissions pour les équipements.

##Auteur
Thomas Richard
Master 1 DS ISUP/Sorbonne