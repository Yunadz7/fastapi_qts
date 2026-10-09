from app.cantina.caixa import calcular_desconto_combo
from app.cantina.embalagem import calcular_taxa_embalagem

def processar_venda(
        valor_bruto:float,
        quantidade_itens: int,
        tipo_cliente:str,
        levar_viagem:bool,
) -> dict:
    """Processa a venda da cantina integrando regras de desconto e embalagem"""
    if valor_bruto <= 0 or quantidade_itens <=0:
        return{
            "sucesso":False,
            "motivo":"dados de venda invalidos",
            "total_final": 0.0
        }

    taxa_desconto = calcular_desconto_combo(quantidade_itens, tipo_cliente)
    valor_desconto = round(valor_bruto * taxa_desconto, 2)
    sub_total = valor_bruto - valor_desconto

    taxa_embalagem = calcular_taxa_embalagem(levar_viagem, quantidade_itens)
    total_final = round(sub_total + taxa_embalagem, 2)

    return {
        "sucesso": True,
        "valor_bruto": round(valor_bruto, 2),
        "desconto_aplicado": valor_desconto,
        "taxa_embalagem": taxa_embalagem,
        "total_final": total_final
    }