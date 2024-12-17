'''Script pour le test pytest des calculateurs'''

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from carboncalc import calculators as cs
import pytest


def test_choisir_periode(monkeypatch):
    '''
    Teste la fonction choisir_periode pour s'assurer que le facteur et la période retournés sont corrects.

    Utilise `monkeypatch` pour simuler les entrées utilisateur.

    Vérifie :
        - Que la sélection "1" retourne (1, "annuelle").
        - Que la sélection "2" retourne (12, "mensuelle").
        - Que la sélection "3" retourne (52, "hebdomadaire").

    Paramètre :
        monkeypatch (pytest.MonkeyPatch) : Permet de simuler l'entrée utilisateur.

    Retourne :
        None
    '''
    monkeypatch.setattr('builtins.input', lambda _: "1")
    facteur, periode = cs.choisir_periode()
    assert facteur == 1
    assert periode == "annuelle"

    monkeypatch.setattr('builtins.input', lambda _: "2")
    facteur, periode = cs.choisir_periode()
    assert facteur == 12
    assert periode == "mensuelle"

    monkeypatch.setattr('builtins.input', lambda _: "3")
    facteur, periode = cs.choisir_periode()
    assert facteur == 52
    assert periode == "hebdomadaire"


def test_ajuster_emissions():
    '''
    Teste la fonction ajuster_emissions pour vérifier l'ajustement correct des émissions.

    Données de test :
        - Facteur : 12 (mensuel)
        - Émissions initiales : aliments = 1200, énergie = 600, équipements = 300

    Vérifie :
        - Que les émissions totales sont correctement ajustées.
        - Que les émissions pour chaque catégorie sont ajustées selon le facteur.

    Retourne :
        None
    '''
    total, aliments, energie, equipements = cs.ajuster_emissions(12, 1200, 600, 300)

    assert total == 175
    assert aliments == 100
    assert energie == 50
    assert equipements == 25

# End-of-file
