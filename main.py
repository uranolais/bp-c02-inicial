from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pedido.pedido_retirada import PedidoRetirada
from notificacao.notificacao_email import NotificacaoEmail
from notificacao.notificacao_sms import NotificacaoSMS

# Exemplo de uso do Factory Method e verificação do LSP
cliente = Cliente("João", "Rua Exemplo, 123")
itens = [Item("Pizza", 30), Item("Refrigerante", 10)]

pedido1 = PedidoDelivery(cliente, itens, taxa_entrega=5)
pedido2 = PedidoRetirada(cliente, itens)

# print("Total Pedido Delivery:", pedido1.calcular_total())
# print("Total Pedido Retirada:", pedido2.calcular_total())

# Injeção de uma implementação de notificação
notificacao = NotificacaoEmail()
pedido1.enviar_notificacao(notificacao, "Seu pedido foi criado com sucesso.")