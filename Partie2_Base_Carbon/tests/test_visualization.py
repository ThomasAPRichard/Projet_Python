import pytest
from unittest.mock import patch
import carboncalc.visualization as vz
print("Module importé avec succès")

@patch("matplotlib.pyplot.show")
def test_visualiser_emissions_bar(mock_show):
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
    aliments_emission = 100
    energie_emission = 200
    equipements_emission = 50
    
    try:
        vz.visualiser_emissions_circulaire(aliments_emission, energie_emission, equipements_emission)
    except Exception as e:
        pytest.fail(f"visualiser_emissions_circulaire a échoué avec l'erreur : {e}")
    mock_show.assert_called_once()
