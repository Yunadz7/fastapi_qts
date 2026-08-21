def classificar_credito(
    renda_mensal: float, score_credito: int, restrito: bool
) -> str:
    """Classifica a solicitação de crédito com base na renda, score e restrição cadastral."""
    if renda_mensal <= 0:
        return "renda invalida"

    if score_credito < 0 or score_credito > 1000:
        return "score invalido"

    if restrito:
        return "reprovado"

    if score_credito >= 700:
        return "aprovado premium"

    if score_credito >= 400:
        return "aprovado padrao"

    return "reprovado"