import time
import pytest

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, esperado",
    [
        # ENTRADAS INVÁLIDAS (-1.0) 

        (0.0, "BRONZE", 0, -1.0),
        (100.0, "BRONZE", -1, -1.0),

        # PLANOS INVÁLIDOS (-2.0) 
        (100.0, "INVALIDO", 0, -2.0),
        (100.0, "", 0, -2.0),

        # NORMALIZAÇÃO E DESCONTOS EM DIA (dias_atraso = 0) 

        (100.0, " BRONZE ", 0, 100.00),  
        (100.0, "PrAtA", 0, 85.00),     # Prata 
        (100.0, "OURO", 0, 75.00),     

        # FRONTEIRAS: ATRASO MODERADO (1 a 20 dias

        (100.0, "BRONZE", 1, 108.40),  
        (100.0, "BRONZE", 20, 116.00),

        #  FRONTEIRAS: ATRASO SEVERO (> 20 dias) 

        (100.0, "BRONZE", 21, 146.80),  
        (100.0, "PRATA", 30, 135.40),  
        (100.0, "OURO", 25, 120.00),   
    ],
)
def test_processar_cobranca_funcional(valor_base, plano, dias_atraso, esperado):
    resultado = processar_cobranca(valor_base, plano, dias_atraso)
    assert resultado == esperado


def test_processar_cobranca_desempenho_nao_funcional():
    inicio = time.perf_counter()
    processar_cobranca(100.0, "BRONZE", 0)
    fim = time.perf_counter()

    tempo_decorrido = fim - inicio
    assert tempo_decorrido < 0.08, f"Tempo excedido: {tempo_decorrido:.4f}s"