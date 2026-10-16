from app.cantina.caixa import processar_venda


def test_integracao_venda_estudande_para_viagem():
    resultado = processar_venda(
        valor_bruto=50.0,
        quantidade_itens=3,
        tipo_cliente="estudante",
        levar_viagem=True
    )

    assert resultado["sucesso"] is True
    assert resultado["desconto_aplicado"] == 7.50
    assert resultado["taxa_embalagem"] == 3.50
    assert resultado["total_final"] == 46.00   

def test_integracao_venda_professor_consumo_local():
    resultado = processar_venda(
        valor_bruto=40.0,
        quantidade_itens=2,
        tipo_cliente="professor",
        levar_viagem=False
    )

    assert resultado["sucesso"] is True
    assert resultado["desconto_aplicado"] == 4.00
    assert resultado["taxa_embalagem"] == 0.0
    assert resultado["total_final"] == 36.0

def test_integracao_venda_com_dados_invalidos():
    resultado = processar_venda(
        valor_bruto=0.0,
        quantidade_itens=0,
        tipo_cliente="estudante",
        levar_viagem=False
    )

    assert resultado["sucesso"] is False
    assert resultado["total_final"] == 0.0