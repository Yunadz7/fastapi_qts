def classificar_nota(nota: float) -> str:
    if nota < 0 or nota > 10:
        return "nota invalida"
    if nota >= 7:
        return "aprovado"
    if nota >= 5:
        return "recuperacao"
    return "reprovado"