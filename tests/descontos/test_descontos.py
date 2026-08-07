from app.descontos.descontos import calcular_desconto

def test_calcular_valor_negativo():
    assert calcular_desconto (-10, False) == 0

def test_calcular_desconto_cliente_vip_com_valor_valido():
    assert calcular_desconto(50, True) == 40 

def test_calcular_desconto_cliente_nao_vip_com_valor_valido():
    assert calcular_desconto(60, False) == 54

def test_calcular_valor_exatamente_0():
    assert calcular_desconto(0, True) == 0 

def test_calcular_valor_pequeno():
    resultado = calcular_desconto(0.01, False)
    assert round(resultado, 3) == 0.009

def test_calcular_valor_maior():
    assert calcular_desconto(500, True) == 400
