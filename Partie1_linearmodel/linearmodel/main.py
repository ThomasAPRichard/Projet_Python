'''DANS CE SCRIPT JE DEFINIT LA CLASSE OrdinaryLeastSquares POUR ANALYSER LE JEU DE DONNEES'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#1 IMPLMENTATION DE LA CLASSE OLS
class OrdinaryLeastSquares:
    '''Classe pour régression linéaire avec la méthode des moindres carrés'''
    def __init__(self, intercept=True):
        self.intercept = intercept
        self.coeffs = None

    def fit(self, X, y):
        '''Entrainer le modèle'''
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        self.coeffs = np.linalg.inv(X.T @ X) @ (X.T @ y)

    def predict(self, X):
        '''Prédiction y'''
        if self.intercept:
            X = np.hstack((np.ones((X.shape[0], 1)), X))
        return X @ self.coeffs

    def determination_coefficient(self, X, y):
        '''R2'''
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y))**2)
        ss_residual = np.sum((y - y_pred)**2)
        return 1 - (ss_residual / ss_total)

    def get_coeffs(self):
        '''getter'''
        return self.coeffs

#2.PARTIE EXECUTABLE
DATA_PATH = "C:/Users/tapri/OneDrive/Bureau/Master_1/Python/Projet_Python/Partie1_linearmodel/vehicles.csv"
data = pd.read_csv(DATA_PATH)

#2.1 Variables
# Choix des variables
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nJe choisis comme variables explicatives : ~"
      "Vehicle Classe, Engine size (L), Cylinders, Transmission, "
      "Fuel type, Combined (L/100 km), City/Highway ratio")
print("Comme demandé, la variable cible est : CO2 emissions (g/km)")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("\nJignore les variables : Make, Year model, Model, City (L/100 km), "
      "Highway (L/100 km), Combined (mpg), CO2 rating et Smog rating")
print("Voici pourquoi,\n")
print(" -Make : Je l'avais utilisé dans une 1ere version, mais cela donne trop de variables "
      "explicatives pour apprendre que Bugatti fais des voitures polluantes")
print(" -Model : Comme vu dans my_stat les émissions de CO2 sont stable par année de fabrication")
print(" -Highway et City : Utiliser City , Highway et Combined (L/100 km) peut donner un poids "
      "disproportionné à la consommation par rapport aux autres variable,")
print("  car elles sont étroitement liées et représentent différents aspects d'une même mesure.")
print("  A la place j'inclue une nouvelle variable City/Highway ratio. Une voiture consommant "
      "significativement plus en ville ou sur autoroute pourrait être un indicateur "
      "pertinent pour les émissions ")
print(" -Combined (mpg) : Sensée etre 100% redondante avec Combiend (L/100 km), malgré la "
      "non absolue corrélation observée dans my_statistics")
print(" -CO2 Rating et Smog rating : Ces variables sont dérivées des émissions de CO2 "
      "et dépendent donc déjà de notre cible")

data['City/Highway ratio'] = data['City (L/100 km)'] / data['Highway (L/100 km)']
X_vehicles = data[['Vehicle class', 'Engine size (L)', 'Cylinders',
                   'Fuel type', 'Transmission', 'Combined (L/100 km)',
                   'City/Highway ratio']]
y_vehicles = data['CO2 emissions (g/km)']

# Problème des données catégorielles, avec le One-Hot Encoding (internet me dit que c'est bien)
categorical_variables = ['Vehicle class', 'Transmission', 'Fuel type']
X_encoded = pd.get_dummies(X_vehicles, columns=categorical_variables, drop_first=True)
X_encoded = X_encoded.astype(float)
# Standardisation pour mes variables numériques
numerical_variable = ['Engine size (L)', 'Cylinders', 'Combined (L/100 km)', 'City/Highway ratio']
X_nv= X_encoded[numerical_variable]
X_encoded[numerical_variable] = (X_nv - X_nv.mean()) / X_nv.std()
X_vehicles = X_encoded
# Je dois supprimer colonnes constantes ou quasi-constantes, sinon on n'inverse pas XtX
constant_columns = X_vehicles.columns[X_encoded.std() <= 0.02]
print(f"\nJe supprime les colonnes {constant_columns.to_list()} car elles sont quasi-constantes")
X_vehicles = X_vehicles.drop(columns=constant_columns)


#2.2 OLS et interprétation

# Séparation de mes données en train et test
indices = np.arange(X_vehicles.shape[0])
np.random.seed(42)
np.random.shuffle(indices)

train_size = int(0.8 * len(indices)) #80% de train est classique
train_indices = indices[:train_size]
test_indices = indices[train_size:]

X_train, X_test = X_vehicles.iloc[train_indices], X_vehicles.iloc[test_indices]
y_train, y_test = y_vehicles[train_indices], y_vehicles[test_indices]
X_train, X_test = X_train.to_numpy() , X_test.to_numpy()
y_train, y_test = y_train.to_numpy() , y_test.to_numpy()


# Lancement du modèle sur le train
ols = OrdinaryLeastSquares(intercept=True)
ols.fit(X_train, y_train)

# Évaluer le modèle
r2_train = ols.determination_coefficient(X_train, y_train)
r2_test = ols.determination_coefficient(X_test, y_test)

print("\n~~~~~~~~~~~~~Résultats~~~~~~~~~~~~~")
print("\nCoefficients estimés :\n", ols.get_coeffs())
print("\nR2 sur les données d'entraînement :", r2_train)
print("R2 sur les données de test :", r2_test)
print("Un R2 aussi élevé suggère que le modèle ajuste très bien les données, et la distribution "
      "des résidus semble suivre une normale avec une faible variance !")
print("Notre analyse nous amène à penser que le type de carburant et dans une moindre mesure "
      "la consommation sont les éléments qui influencent majoritairement les émissions")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~")

#2.3 Visualisation de nos résultats

#Visualiser l'importance des variables
coefficients = ols.get_coeffs()
sorted_indices = np.argsort(np.abs(coefficients))[::-1]
sorted_coefficients = coefficients[sorted_indices]
variable_names = ["Intercept"] + list(X_vehicles.columns)
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

#Visualiser distribution des résidus
residus_train = y_train - ols.predict(X_train)
residus_test = y_test - ols.predict(X_test)

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle("Distribution des résidus", fontsize=16)

axes[0].hist(residus_train, bins = 30, color='pink',edgecolor='black',label='Train', density =True)
axes[0].set_xlabel("Résidus")
axes[0].set_ylabel("Fréquence")
axes[0].grid(alpha=0.5)
axes[0].legend()
axes[0].set_title("Distribution train")

axes[1].hist(residus_test, bins = 30, color='orange',edgecolor='black',label='Test', density =True)
axes[1].set_xlabel("Résidus")
axes[1].set_ylabel("Fréquence")
axes[1].grid(alpha=0.5)
axes[1].legend()
axes[1].set_title("Distribution test")

plt.tight_layout()
plt.show()

# Visualiser l'ajustement du modèle
y_pred_train = ols.predict(X_train)
y_pred_test = ols.predict(X_test)

fig, axes = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle("Valeurs réelles vs prédites", fontsize=16)

axes[0].scatter(y_train, y_pred_train, alpha=0.85, edgecolor='black', color ='pink')
axes[0].plot([min(y_train), max(y_train)], [min(y_train), max(y_train)],
             color='red', linestyle='--', linewidth=2)
axes[0].set_xlabel("Valeurs réelles (CO2 emissions)")
axes[0].set_ylabel("Valeurs prédites (CO2 emissions)")
axes[0].grid(alpha=0.5)

axes[0].set_title("Ajustement (Ensemble d'entraînement)")

axes[1].scatter(y_test, y_pred_test, alpha=0.85, edgecolor='black', color='orange')
axes[1].plot([min(y_test), max(y_test)], [min(y_test), max(y_test)],
             color='red', linestyle='--', linewidth=2)
axes[1].set_xlabel("Valeurs réelles (CO2 emissions)")
axes[1].set_ylabel("Valeurs prédites (CO2 emissions)")
axes[1].grid(alpha=0.5)
axes[1].set_title("Ajustement (Ensemble de test)")

plt.tight_layout()
plt.show()

# Calcul des corrélations
correlation_matrix = X_vehicles.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, cmap='coolwarm', linewidths=0.5)
plt.title("Heatmap des corrélations entre les variables explicatives")
plt.tight_layout()
plt.show()

#End-of-file
