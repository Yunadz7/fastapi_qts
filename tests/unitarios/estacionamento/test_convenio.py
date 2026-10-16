
import pytest
from app.estacionamento.convenio import calcular_desconto_convenio


def test_convenio_mercado():
    assert calcular_desconto_convenio(52.0, "MERCADO") == 10.4


def test_convenio_farmacia():
    assert calcular_desconto_convenio(42.0, "FARMACIA") == 4.2


def test_loja_nao_parceira():
    assert calcular_desconto_convenio(50.0, "PADARIA") == 0.0


def test_codigo_loja_vazio():
    assert calcular_desconto_convenio(50.0, "") == 0.0


@pytest.mark.parametrize("valor_bruto", [0.0, -10.0, -5.0])
def test_valor_bruto_menor_ou_igual_a_zero(valor_bruto):
    assert calcular_desconto_convenio(valor_bruto, "MERCADO") == 0.0
