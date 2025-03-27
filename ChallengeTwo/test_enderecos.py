import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from enderecos import possiveis_enderecos


def test_exemplo_valido():
    entrada = "25525511135"
    saida_esperada = sorted(["255.255.11.135", "255.255.111.35"])
    assert possiveis_enderecos(entrada) == saida_esperada


def test_tudo_zero():
    entrada = "0000"
    assert possiveis_enderecos(entrada) == ["0.0.0.0"]


def test_com_zero_na_frente():
    entrada = "010010"
    saida_esperada = sorted(["0.10.0.10", "0.100.1.0"])
    assert possiveis_enderecos(entrada) == saida_esperada


def test_muito_curto():
    entrada = "123"
    assert possiveis_enderecos(entrada) == []


def test_muito_longo():
    entrada = "1234567890123"
    assert possiveis_enderecos(entrada) == []


def test_segmento_maior_que_255():
    entrada = "256256256256"
    assert possiveis_enderecos(entrada) == []


def test_entrada_vazia():
    entrada = ""
    assert possiveis_enderecos(entrada) == []
