def calcular_desconto_combo(quantidade_itens: int, tipo_cliente: str) -> float:
    """Calcula a taxa percentual de desconto com base na quantidade e perfil"""
    if quantidade_itens <2:
        return 0.0

    perfil = tipo_cliente.strip().lower() if tipo_cliente else ""

    if perfil == 'estudande':
        if quantidade_itens >= 5:
            return 0.20
        return 0.15

    if perfil == 'professor':
        return 0.10
    return 0.0