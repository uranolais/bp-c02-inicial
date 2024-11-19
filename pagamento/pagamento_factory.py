from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_boleto import PagamentoBoleto

class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo):
        if tipo == 'cartao':
            return PagamentoCartao()
        elif tipo == 'boleto':
            return PagamentoBoleto()
        else:
            raise ValueError("Tipo de pagamento não suportado.")
