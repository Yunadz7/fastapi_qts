def calcular_tarifa_base(horas: int, tipo_veiculo: str) -> float:
    """Calcula o valor da estadia de acordo com a quantidade de horas e o veículo."""
    if horas <= 0:
        return 0.0

    tipo = tipo_veiculo.strip().lower() if tipo_veiculo else ""

    if tipo == "moto":
        primeira_hora = 5.0
        horas_adicionais = (horas - 1) * 3.0
        return primeira_hora + horas_adicionais

    if tipo == "carro":
        primeira_hora = 10.0
        horas_adicionais = (horas - 1) * 6.0
        return primeira_hora + horas_adicionais

    return -1.0