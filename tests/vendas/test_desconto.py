import pytest
from app.vendas.desconto import calcular_desconto
@pytest.mark.parametrize(
    "valor_compra, cupom, desconto_esperado",
    [
        (100.0, "VALE10", 10.0),
        (200.0, "VALE20", 40.0),
        (150.0, "INVALIDO", 0.0),
        (0.0, "VALE10", 0.0),
        (-50.0, "VALE20", 0.0),
        (100.0, "   vale10 ", 10.0),
        

    ] 
)
def test_calcular_desconto_funciona(valor_compra, cupom, desconto_esperado):
    assert calcular_desconto(valor_compra, cupom) == desconto_esperado 