import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from inovacao import calcular_nivel_de_inovacao

def test_exemplo1():
    entrada = {
        "historico": [100, 200, 300, 100, 400],
        "impulsionadores": {100, 500},
        "barreiras": {200, 600}
    }
    assert calcular_nivel_de_inovacao(**entrada) == 1

def test_so_impulsionadores():
    entrada = {
        "historico": [1, 2, 3],
        "impulsionadores": {1, 2, 3},
        "barreiras": {4, 5}
    }
    assert calcular_nivel_de_inovacao(**entrada) == 3

def test_so_barreiras():
    entrada = {
        "historico": [4, 5, 4],
        "impulsionadores": {1, 2},
        "barreiras": {4, 5}
    }
    assert calcular_nivel_de_inovacao(**entrada) == -3

def test_eventos_que_nao_afetam():
    entrada = {
        "historico": [10, 20, 30],
        "impulsionadores": {40, 50},
        "barreiras": {60, 70}
    }
    assert calcular_nivel_de_inovacao(**entrada) == 0
