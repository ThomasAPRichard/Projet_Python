'''Test pytest des visualisations'''
import sys
import os
import pytest
import numpy as np
import pandas as pd
import matplotlib
import seaborn

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Partie1_linearmodel.linearmodel.visualization import plot_multiple_histograms, plot_multiple_scatters


def test_plot_multiple_histograms():
    '''Test mutiple histo'''
    data = pd.DataFrame({
        'Var1': [1, 2, 3, 4, 5],
        'Var2': [2, 4, 6, 8, 10],
        'Var3': [5, 4, 3, 2, 1],
        'Var4': [10, 20, 30, 40, 50],
        'Var5': [1, 3, 5, 7, 9],
        'Var6': [9, 8, 7, 6, 5],
        'Var7': [15, 25, 35, 45, 55],
        'Var8': [0, 1, 0, 1, 0],
        'Var9': [100, 200, 300, 400, 500]
    })

    try:
        plot_multiple_histograms(data, ['Var1', 'Var2', 'Var3', 'Var4', 'Var5', 'Var6', 'Var7', 'Var8', 'Var9'])
    except Exception as e:
        pytest.fail(f"Plotting histograms failed: {e}")

def test_plot_multiple_scatters():
    '''Test scatters'''
    data = pd.DataFrame({
        'Var1': [1, 2, 3, 4, 5],
        'Var2': [5, 4, 3, 2, 1],
        'Var3': [10, 20, 30, 40, 50],
        'Var4': [50, 40, 30, 20, 10]})

    scatter_pairs = [
        ('Var1', 'Var2'),
        ('Var3', 'Var4'),
        ('Var1', 'Var3'),
        ('Var2', 'Var4'),
        ('Var1', 'Var4'),
        ('Var2', 'Var4')]

    try:
        plot_multiple_scatters(data, scatter_pairs)
    except Exception as e:
        pytest.fail(f"Plotting scatter plots failed: {e}")

#End-of-file
