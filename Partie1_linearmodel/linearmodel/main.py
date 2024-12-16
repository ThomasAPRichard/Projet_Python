# DANS CE SCRIPT JE DEFINIT LA CLASSE OrdinaryLeastSquares POUR ANALYSER LE JEU DE DONNEES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#1 IMPLMENTATION DE LA CLASSE OLS
class OrdinaryLeastSquares:
    def __init__(self, intercept=True):
        self.intercept = intercept
        self.coeffs = None
    
    def fit(self, X, y):
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        self.coeffs = np.linalg.inv(X.T @ X) @ (X.T @ y)
    
    def predict(self, X):
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        return X @ self.coeffs
    
    def determination_coefficient(self, X, y):
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y))**2)  # Somme des carrés totaux
        ss_residual = np.sum((y - y_pred)**2)  # Somme des carrés résiduels
        return 1 - (ss_residual / ss_total)
    
    def get_coeffs(self):
        return self.coeffs

#2.PARTIE EXECUTABLE
data_path = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(data_path)

#2.1 Variables
# Choix des variables 
print("Je choisis comme variables explicatives : Vehicle Classe, Engine size (L), Cylinders, Transmission, Fuel type, Combined (L/100 km), City/Highway ratio")
print("\nComme demandé, la variable cible est : CO2 emissions (g/km)")
print("\nJignore les variables : Make, Year model, Model, City (L/100 km), Highway (L/100 km), Combined (mpg), CO2 rating et Smog rating")
print("Voici pourquoi,\nMake : Je l'avais utilisé dans une 1ere version, mais cela donne trop de variables explicatives pour apprendre que Bugatti fais des voitures polluantes")
print("Model : Comme vu dans my_stat les émissions de CO2 sont stable par année de fabrication")
print("Highway et City : Utiliser City , Highway et Combined (L/100 km) peut donner un poids disproportionné à la consommation par rapport aux autres variable,")
print("car elles sont étroitement liées et représentent différents aspects d'une même mesure.") 
print("A la place j'inclue une nouvelle variable City/Highway ratio. Une voiture consommant significativement plus en ville ou sur autoroute pourrait être un indicateur pertinent pour les émissions ")
print("Combined (mpg) : Sensée etre 100% redondante avec Combiend (L/100 km), malgré la non absolue corrélation observée dans my_statistics")
print("CO2 Rating et Smog rating : Ces variables sont dérivées des émissions de CO2 et dépendent donc déjà de notre cible")

data['City/Highway ratio'] = data['City (L/100 km)'] / data['Highway (L/100 km)']
X = data[['Vehicle class', 'Engine size (L)', 'Cylinders', 'Fuel type', 'Transmission', 'Combined (L/100 km)', 'City/Highway ratio']]
y = data['CO2 emissions (g/km)']

# Problème des données catégorielle, avec le One-Hot Encoding (internet me dit que c'est une bonne solution)
categorical_variables = ['Vehicle class', 'Transmission', 'Fuel type']
X_encoded = pd.get_dummies(X, columns=categorical_variables, drop_first=True)
X_encoded = X_encoded.astype(float)

# Standardisation pour mes variables numériques
numerical_variable = ['Engine size (L)', 'Cylinders', 'Combined (L/100 km)', 'City/Highway ratio']
X_encoded[numerical_variable] = (X_encoded[numerical_variable] - X_encoded[numerical_variable].mean()) / X_encoded[numerical_variable].std()


#2.2 Lancement du modèle et interprétation
variable_names = ["Intercept"] + list(X_encoded.columns)
X= X_encoded.to_numpy()
y = y.to_numpy()
ols = OrdinaryLeastSquares(intercept=True)
ols.fit(X, y)

print("\nCoefficients estimés :", ols.get_coeffs())
print("\nR^2 :", ols.determination_coefficient(X, y))
print("Un R^2 aussi élevé suggère que le modèle ajuste très bien les données, et la distribution des résidus semble suivre une normale avec une faible variance !")
print("Notre analyse nous amène à penser que le type de carburant et dans une moindre mesure la consommation sont les éléments qui influencent majoritairement les émissions")


#2.3 Visualisation de nos résultats
# Calcul des résidus
residuals = y - ols.predict(X)

plt.figure(figsize=(8, 6))
plt.hist(residuals, bins=30, color='skyblue', edgecolor='black')
plt.axvline(0, color='red', linestyle='--', linewidth=1)
plt.title("Distribution des résidus")
plt.xlabel("Résidus (y réel - y prédit)")
plt.ylabel("Fréquence")
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

#Visualiser l'importance des variables
coefficients = ols.get_coeffs()
sorted_indices = np.argsort(np.abs(coefficients))[::-1]
sorted_coefficients = coefficients[sorted_indices]
sorted_variable_names = [variable_names[i] for i in sorted_indices]

plt.figure(figsize=(12, 8))
plt.bar(sorted_variable_names, sorted_coefficients, color='skyblue', edgecolor='black')
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.title("Importance des coefficients estimés")
plt.ylabel("Valeur des coefficients")
plt.xlabel("Variables explicatives")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#Visualiser l'ajustement du modèle
y_pred = ols.predict(X)

plt.figure(figsize=(8, 6))
plt.scatter(y, y_pred, alpha=0.7, edgecolor='black')
plt.plot([min(y), max(y)], [min(y), max(y)], color='red', linestyle='--', linewidth=2)
plt.title("Valeurs réelles vs prédites")
plt.xlabel("Valeurs réelles (CO2 emissions)")
plt.ylabel("Valeurs prédites (CO2 emissions)")
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()

# Calcul des corrélations
correlation_matrix = X_encoded.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap des corrélations entre les variables explicatives")
plt.tight_layout()
plt.show()