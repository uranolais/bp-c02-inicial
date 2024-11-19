from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pedido.pedido_retirada import PedidoRetirada

# Cliente e itens
cliente = Cliente("João", "Rua Exemplo, 123")
itens = [Item("Pizza", 30.0), Item("Refrigerante", 5.0)]

# Pedido Delivery
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega=10.0)
print(f"Total do Pedido Delivery: R${pedido_delivery.calcular_total():.2f}")

# Pedido Retirada
pedido_retirada = PedidoRetirada(cliente, itens)
print(f"Total do Pedido Retirada: R${pedido_retirada.calcular_total():.2f}")
