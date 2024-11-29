#FICHIER QUI NE DEVRA PAS ETRE DANS LE RENDU FINALE
#CE FICHIER SERT A TESTER DES TRUCS ET DECOUVRIR UN PEU LE TRUC
import numpy as np
import pandas as pd

#1 IMPLMENTATION DE LA CLASSE OLS
class OrdinaryLeastSquares:
    def __init__(self, intercept=True):
        self.intercept = intercept
        self.coeffs = None
    
    def fit(self, X, y):
        """
        Ajuste le modèle OLS aux données.
        
        Parameters:
            X (numpy.ndarray): Matrice des covariables.
            y (numpy.ndarray): Vecteur cible.
        """
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))  # Ajout de la colonne pour l'intercept
        
        # Calcul des coefficients OLS
        self.coeffs = np.linalg.inv(X.T @ X) @ (X.T @ y)
    
    def predict(self, X):
        """
        Prédit les valeurs de y pour une matrice X donnée.
        """
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        
        return X @ self.coeffs
    
    def determination_coefficient(self, X, y):
        """
        Calcule le coefficient de détermination R².
        """
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y))**2)  # Somme des carrés totaux
        ss_residual = np.sum((y - y_pred)**2)  # Somme des carrés résiduels
        return 1 - (ss_residual / ss_total)

#2.PARTIE EXECUTABLE
data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)

#2.1 Variables
# Choix des variables 
print("Je choisis comme variables explicatives : Make, Vehicle Classe, Engine size (L), Cylinders, Transmission, Fuel type, Combined (L/100 km), City/Highway ratio")
print("\nComme demandé, la variable cible est : CO2 emissions (g/km)")
print("\nJignore les variables : Year model, Model, City (L/100 km), Highway (L/100 km), Combined (mpg), CO2 rating et Smog rating")
print("Voici pourquoi,\nModel : Comme vu dans my_stat les émissions de CO2 sont stable par année de fabrication")
print("Highway et City : Utiliser City , Highway et Combined (L/100 km) peut donner un poids disproportionné à la consommation par rapport aux autres variable,")
print("car elles sont étroitement liées et représentent différents aspects d'une même mesure.") 
print("A la place j'inclue une nouvelle variable City/Highway ratio. Une voiture consommant significativement plus en ville pourrait être un indicateur pertinent pour les émissions ")
print("Combined (mpg) : Sensée etre 100% redondante avec Combiend (L/100 km), malgré la non absolue corrélation observée dans my_statistics")
print("CO2 Rating et Smog rating : Ces variables sont dérivées des émissions de CO2 et dépendent donc déjà de notre cible")

data['City/Highway ratio'] = data['City (L/100 km)'] / data['Highway (L/100 km)']
X = data[['Make', 'Vehicle class', 'Engine size (L)', 'Cylinders', 'Fuel type', 'Transmission', 'Combined (L/100 km)', 'City/Highway ratio']]
y = data['CO2 emissions (g/km)']

# Problème des données catégorielle, avec le One-Hot Encoding (internet me dit que c'est une bonne solution)
categorical_variables = ['Make', 'Vehicle class', 'Transmission', 'Fuel type']
X_encoded = pd.get_dummies(X, columns=categorical_variables, drop_first=True)
X_encoded = X_encoded.astype(float)

# Standardisation pour mes variables numériques
numerical_variable = ['Engine size (L)', 'Cylinders', 'Combined (L/100 km)', 'City/Highway ratio']
X_encoded[numerical_variable] = (X_encoded[numerical_variable] - X_encoded[numerical_variable].mean()) / X_encoded[numerical_variable].std()


#2.2 Lancement du modèle
X= X_encoded.to_numpy()
y = y.to_numpy()
ols = OrdinaryLeastSquares(intercept=True)
ols.fit(X, y)

# Résultats
print("Coefficients estimés :", ols.coeffs)
print("R^2 :", ols.determination_coefficient(X, y))