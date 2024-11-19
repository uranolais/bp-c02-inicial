from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_cartao import PagamentoCartao

# Cliente e pedido
cliente = Cliente("Maria", "Rua Exemplo, 456")
itens = [Item("Hambúrguer", 25.0), Item("Batata", 10.0)]
pedido = PedidoDelivery(cliente, itens, taxa_entrega=5.0)

# Pagamento
pagamento = PagamentoCartao()
pagamento.processar(pedido.calcular_total())
