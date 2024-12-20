'''Tests de l'OLS'''
import sys
import os
import pytest
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Partie1_linearmodel.linearmodel.main import OrdinaryLeastSquares

def test_ols_fit_and_predict():
    '''Test de la classe OLS'''
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8])

    ols = OrdinaryLeastSquares(intercept=True)
    ols.fit(X, y)

    assert pytest.approx(ols.coeffs[0], 0.01) == 0
    assert pytest.approx(ols.coeffs[1], 0.01) == 2
    y_pred = ols.predict(X)
    assert all(pytest.approx(y_pred[i], 0.01) == y[i] for i in range(len(y)))

def test_ols_r2():
    '''Test R2'''
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8])

    ols = OrdinaryLeastSquares(intercept=True)
    ols.fit(X, y)

    r2 = ols.determination_coefficient(X, y)
    assert pytest.approx(r2, 0.01) == 1.0

#End-of-file
