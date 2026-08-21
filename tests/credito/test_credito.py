import pytest
from app.credito.credito import classificar_credito

@pytest.mark.parametrize(
    "renda_mensal, score_credito, restrito"
    [
        (0, 1, True, "renda invalida"),
        (1, -1, True, "renda invalida"),
        (1, -1, False, "score invalido"),
        (1, 1001, False, "score invalido"),
        (1, 1, True, "reprovado"),
        (1, 1, False, "reprovado"),
        (1, 401, False, "aprovado padrao"),
        (1, 701, False, "aprovado premium"),

    ]
)
def test_classificar_frete_caixa_preta(peso_kg, regiao, premium, retorno_esperado):
    assert classificar_credito(peso_kg, regiao, premium) == retorno_esperado