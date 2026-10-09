import pytest
from app.cantina.combo import calcular_desconto_combo

@pytest.mark.parametrize(
    "quantidade, perfil, desconto_esperado",
    [
        (1,"estudante", 0.0),
        (2,"estudante", 0.15),
        (5,"estudante", 0.20),
        (3,"professor", 0.10),
        (4,"visitante", 0.0),
        (0,"estudante", 0.0),
    ]
)

def test_calcular_desconto_combo_cenarios(quantidade, perfil, desconto_esperado):
    resultado = calcular_desconto_combo(quantidade, perfil)
    assert resultado == desconto_esperado