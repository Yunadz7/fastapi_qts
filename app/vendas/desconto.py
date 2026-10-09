def calcular_desconto(valor_compra: float, cupom: str) -> float:
    if valor_compra <= 0:
        return 0.0

    cupom_limpo = cupom.strip().upper()
    if cupom_limpo == "VALE10":
        return valor_compra * 0.10
    if cupom_limpo == "VALE20":
        return valor_compra * 0.20

    return 0.0