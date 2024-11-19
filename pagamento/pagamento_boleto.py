from pagamento.pagamento import Pagamento

class PagamentoBoleto(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento de R${valor} via Boleto")
