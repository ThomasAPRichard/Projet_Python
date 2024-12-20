'''Test pytest des visualisations'''

import sys
import os
import pytest
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Partie1_linearmodel.linearmodel.my_statistics import variable1_mean_by_variable2, data_presentation

def test_variable1_mean_by_variable2():
    '''Test des statistiques'''
    data = pd.DataFrame({
        'Fuel type': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Electric'],
        'CO2 emissions (g/km)': [150, 120, 180, 100, 0]
    })
    result = variable1_mean_by_variable2(data, 'CO2 emissions (g/km)', 'Fuel type')

    expected_means = {'Diesel': 110, 'Electric': 0, 'Petrol': 165}
    for fuel, mean in expected_means.items():
        assert pytest.approx(result[fuel], 0.01) == mean

def test_data_presentation(capsys):
    '''Test de la fonction de présentation'''
    data = pd.DataFrame({
        'Model': ['A', 'B', 'C'],
        'Make': ['X', 'Y', 'Z'],
        'Model year': [2015, 2016, 2017],
        'CO2 rating': [1, None, 3],
        'Smog rating': [None, 2, 3]
    })
    data_presentation(data)

    captured = capsys.readouterr()
    assert "différents véhicules" in captured.out
    assert "CO2 rating" in captured.out

    #End-of-file
