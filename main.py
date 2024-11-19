from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_email import NotificacaoEmail
from notificacao.notificacao_sms import NotificacaoSMS

# Cliente e pedido
cliente = Cliente("Maria", "Rua Exemplo, 456")
itens = [Item("Hambúrguer", 25.0), Item("Batata", 10.0)]
pedido = PedidoDelivery(cliente, itens, taxa_entrega=5.0)

# # Pagamento
# pagamento = PagamentoCartao()
# pagamento.processar(pedido.calcular_total())


tipo_pagamento = 'boleto'  # Pode ser 'cartao' ou 'boleto'
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento)
pagamento.processar(pedido.calcular_total())  # Valor exemplo

notificacao_email = NotificacaoEmail()
notificacao_email.enviar(cliente, "Seu pedido foi enviado!")

notificacao_sms = NotificacaoSMS()
notificacao_sms.enviar(cliente, "Seu pedido está a caminho!")
