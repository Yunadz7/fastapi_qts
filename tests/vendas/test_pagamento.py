import time

from app.vendas.pagamento import processar_pagamento
def test_tempo_processamento_pagamento():
    inicio = time.perf_counter()
    resultado = processar_pagamento(100.0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado is True
    assert tempo_decorrido <0.1