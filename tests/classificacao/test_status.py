from app.classificacao.status import calcular_status_pedidos

def teste_retorna_invalido_quando_valor_zero():
    assert calcular_status_pedidos(0, True) == "invalido"

def teste_retorna_invalido_quando_valor_negativo():
    assert calcular_status_pedidos(-10, False) == "invalido"

def teste_retorna_pendente_quando_nao_foi_pago():
    assert calcular_status_pedidos(120, False) == "pendente"

def test_retorna_confirmado_quando_pago_e_valor_valido():
    assert calcular_status_pedidos(120,True) == "confirmado"