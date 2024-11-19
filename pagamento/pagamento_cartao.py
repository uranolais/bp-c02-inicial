from pagamento.pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor} via Cartão de Crédito")
