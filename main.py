from cliente import Cliente
from item import Item

# Criando cliente
cliente = Cliente("João", "Rua Exemplo, 123")
print(f"Cliente: {cliente.nome}, Endereço: {cliente.endereco}")

# Criando itens
item1 = Item("Pizza", 30.0)
item2 = Item("Refrigerante", 5.0)
print(f"Item: {item1.nome}, Preço: R${item1.preco:.2f}")
print(f"Item: {item2.nome}, Preço: R${item2.preco:.2f}")
