
import pytest
from app.estacionamento.tarifas import calcular_tarifa_base


def test_moto_por_1_hora():
    assert calcular_tarifa_base(1, "moto") == 5.0


def test_moto_por_3_horas():
    assert calcular_tarifa_base(3, "moto") == 11.0


def test_carro_por_1_hora():
    assert calcular_tarifa_base(1, "carro") == 10.0


def test_carro_por_4_horas():
    assert calcular_tarifa_base(4, "carro") == 28.0


def test_tipo_veiculo_invalido():
    assert calcular_tarifa_base(2, "bicicleta") == -1.0


@pytest.mark.parametrize("horas", [0, -1, -5])
def test_horas_menor_ou_igual_a_zero(horas):
    assert calcular_tarifa_base(horas, "moto") == 0.0
