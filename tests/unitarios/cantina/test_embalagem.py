import pytest
from app.cantina.embalagem import calcular_taxa_embalagem

@pytest.mark.parametrize(
    "levar_viagem, quantidade_itens, taxa_esperada",
    [
        (False, 4, 0.0),
        (True, 3, 3.50),
        (True, 0, 0.0),
        (True, -1, 0.0),
    ]
)
def test_calcular_taxa_embalagem_cenarios(levar_viagem, quantidade_itens, taxa_esperada):
    resultado = calcular_taxa_embalagem(levar_viagem, quantidade_itens)
    assert resultado == taxa_esperada