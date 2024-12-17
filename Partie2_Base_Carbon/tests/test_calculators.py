#Script pour le test pytest des calculateurs
import pytest
import pandas as pd
import carboncalc.calculators as cs


def test_choisir_periode(monkeypatch):
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
    total, aliments, energie, equipements = cs.ajuster_emissions(12, 1200, 600, 300)
    assert total == 175, "L'ajustement des émissions mensuelles est incorrect"
    assert aliments == 100, "L'émission ajustée pour aliments est incorrecte"
    assert energie == 50, "L'émission ajustée pour énergie est incorrecte"
    assert equipements == 25, "L'émission ajustée pour équipements est incorrecte"

