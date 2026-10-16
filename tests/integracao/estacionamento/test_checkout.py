import pytest
from app.estacionamento.checkout import emitir_ticket_saida


def test_checkout_carro_com_convenio_mercado():

    resultado = emitir_ticket_saida(
        placa="abc-1234",
        horas=5,
        tipo_veiculo="carro",
        codigo_loja="MERCADO"
    )

    assert resultado["valido"] is True
    assert resultado["placa"] == "ABC-1234"
    assert resultado["tarifa_base"] == 34.00
    assert resultado["desconto_convenio"] == 6.80
    assert resultado["valor_a_pagar"] == 27.20


def test_checkout_moto_com_convenio_farmacia():
   
    resultado = emitir_ticket_saida(
        placa="xyz-9876",
        horas=4,
        tipo_veiculo="moto",
        codigo_loja="FARMACIA"
    )

    assert resultado["valido"] is True
    assert resultado["placa"] == "XYZ-9876"
    assert resultado["tarifa_base"] == 14.00
    assert resultado["desconto_convenio"] == 1.40
    assert resultado["valor_a_pagar"] == 12.60


def test_checkout_veiculo_tipo_nao_suportado():
   
    resultado = emitir_ticket_saida(
        placa="klm-5678",
        horas=2,
        tipo_veiculo="caminhao",
        codigo_loja="MERCADO"
    )

    assert resultado["valido"] is False
    assert resultado["motivo"] == "tipo de veiculo nao suportado"
    assert resultado["valor_a_pagar"] == 0.0


def test_checkout_horas_zeradas_rejeicao():

    resultado = emitir_ticket_saida(
        placa="abc-1234",
        horas=0,
        tipo_veiculo="carro",
        codigo_loja="MERCADO"
    )

    assert resultado["valido"] is False
    assert resultado["motivo"] == "dados invalidos para checkout"
    assert resultado["valor_a_pagar"] == 0.0
