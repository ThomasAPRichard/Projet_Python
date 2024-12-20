'''Script pour le test pytest des visualisations'''

import sys
import os
from unittest.mock import patch
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from carboncalc import visualization as vz
import pytest


@patch("matplotlib.pyplot.show")
def test_visualiser_emissions_bar(mock_show):
    '''
    Teste la fonction visualiser_emissions_bar.

    Vérifie que :
    - La fonction ne lève pas d'erreur lorsqu'elle est appelée.
    - plt.show() est bien appelé une fois.

    Paramètre :
        mock_show (Mock) : Mock de la fonction matplotlib.pyplot.show pour éviter l'affichage.

    Retourne :
        None
    '''
    aliments_emission = 100
    energie_emission = 200
    equipements_emission = 50

    try:
        vz.visualiser_emissions_bar(aliments_emission, energie_emission, equipements_emission)
    except Exception as e:
        pytest.fail(f"visualiser_emissions_bar a échoué avec l'erreur : {e}")

    mock_show.assert_called_once()


@patch("matplotlib.pyplot.show")
def test_visualiser_emissions_circulaire(mock_show):
    '''
    Teste la fonction visualiser_emissions_circulaire.

    Vérifie que :
    - La fonction ne lève pas d'erreur lorsqu'elle est appelée.
    - plt.show() est bien appelé une fois.

    Paramètre :
        mock_show (Mock) : Mock de la fonction matplotlib.pyplot.show pour éviter l'affichage.

    Retourne :
        None
    '''
    aliments_emission = 100
    energie_emission = 200
    equipements_emission = 50

    try:
        vz.visualiser_emissions_circulaire(aliments_emission, energie_emission, equipements_emission)
    except Exception as e:
        pytest.fail(f"visualiser_emissions_circulaire a échoué avec l'erreur : {e}")

    mock_show.assert_called_once()

# End-of-file
