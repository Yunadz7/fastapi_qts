from app.estacionamento.convenio import calcular_desconto_convenio
from app.estacionamento.tarifas import calcular_tarifa_base


def emitir_ticket_saida(
    placa: str,
    horas: int,
    tipo_veiculo: str,
    codigo_loja: str,
) -> dict:
    """Emite o ticket consolidado integrando cálculo de horas e convênio parceiro."""
    if not placa or horas <= 0:
        return {
            "valido": False,
            "motivo": "dados invalidos para checkout",
            "valor_a_pagar": 0.0,
        }

    tarifa = calcular_tarifa_base(horas, tipo_veiculo)
    if tarifa < 0:
        return {
            "valido": False,
            "motivo": "tipo de veiculo nao suportado",
            "valor_a_pagar": 0.0,
        }

    desconto = calcular_desconto_convenio(tarifa, codigo_loja)
    valor_a_pagar = round(tarifa - desconto, 2)

    return {
        "valido": True,
        "placa": placa.strip().upper(),
        "tarifa_base": round(tarifa, 2),
        "desconto_convenio": round(desconto, 2),
        "valor_a_pagar": valor_a_pagar,
    }