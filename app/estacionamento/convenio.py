def calcular_desconto_convenio(valor_bruto: float, codigo_loja: str) -> float:
    """Calcula o desconto da estadia mediante comprovação de compra parceira."""
    if valor_bruto <= 0:
        return 0.0

    codigo = codigo_loja.strip().upper() if codigo_loja else ""

    if codigo == "MERCADO":
        return round(valor_bruto * 0.20, 2)

    if codigo == "FARMACIA":
        return round(valor_bruto * 0.10, 2)

    return 0.0