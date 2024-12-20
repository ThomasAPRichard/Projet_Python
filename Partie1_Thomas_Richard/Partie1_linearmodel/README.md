#Projet de Modélisation Linéaire avec OLS (Ordinary Least Squares)

##Description
Ce projet implémente un modèle de régression linéaire utilisant la méthode des moindres carrés ordinaires (OLS). Il inclut également des outils pour l'analyse statistique et la visualisation des résultats.
Tous ces outils sont implémentés pour fonctionner avec le dataset vehicles.csv

##Structure du projet
Le projet est organisé ainsi :
Partie 2_Base_Carbon/
├── linearmodel/ 
│     ├── __init__.py
│     ├── ols.py                # Classe OLS // EXECTUTABLE
│     ├── my_statistics.py      # Outils d'analyse stat // EXECUTABLE
│     ├── visualization.py      # Visualation génériques  EXECUTABLE
│     └── vehicules.csv         # Dataset
│
├── tests/  
│   ├── __init__.py
│   ├── test_main.py            # Tests pour main.py
│   ├── test_my_statistics.py   # Tests pour my_statistics.py
│   └── test_visualization.py   # Tests pour visualization.py
│
├── main.py                     # Fichier d'exécution générale 
│
└── README.md                   # Documentation du projet

##Notes Pylint
-main               = 9.31
-my_statistics      = 9.09
-visualization      = 9.89
-test_main          = 6.09 (causé par les imports unitulisés selon Pylint, mais obligatoire pour pytest)
-test_my_statistics = 5.79 (causé par les imports unitulisés selon Pylint, mais obligatoire pour pytest)
-test_visualization = 4.09 (causé par les imports unitulisés selon Pylint, mais obligatoire pour pytest)

##Prérequis
Python 3.9
Librairies Python nécessaires :
numpy
pandas
matplotlib
seaborn
pytest

##Données Utilisées
Les données proviennent du gouvernement du Canada : elle enregistrent les émissions de CO2
de certains véhicules ainsi que les details de ces véhicules.

##Auteur
Thomas Richard
Master 1 DS ISUP/Sorbonne