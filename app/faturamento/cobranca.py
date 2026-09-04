import time


def processar_cobranca(
    valor_base: float, plano: str, dias_atraso: int
) -> float:
    """Processa cobrança aplicando descontos, encargos e simulação de latência."""
    if valor_base <= 0 or dias_atraso < 0:
        return -1.0

    plano_normalizado = plano.strip().upper() if plano else ""

    descontos = {
        "BRONZE": 0.0,
        "PRATA": 0.15,
        "OURO": 0.25,
    }

    if plano_normalizado not in descontos:
        return -2.0

    # Simulação de latência de rede com serviço financeiro externo
    time.sleep(0.03)

    desconto_aplicado = descontos[plano_normalizado]
    valor_com_desconto = valor_base * (1.0 - desconto_aplicado)

    if dias_atraso == 0:
        valor_final = valor_com_desconto
    elif dias_atraso <= 20:
        multa_fixa = 8.0
        juros_diarios = valor_com_desconto * (dias_atraso * 0.004)
        valor_final = valor_com_desconto + multa_fixa + juros_diarios
    else:
        multa_fixa = 30.0
        juros_diarios = valor_com_desconto * (dias_atraso * 0.008)
        valor_final = valor_com_desconto + multa_fixa + juros_diarios

    return round(valor_final, 2)