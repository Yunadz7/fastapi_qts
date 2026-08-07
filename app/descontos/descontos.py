def calcular_desconto(valor,cliente_vip): 
    if valor <= 0:
        return 0
    if cliente_vip == True:
        return valor * 0.80
    if cliente_vip == False:
        return valor * 0.90