from abc import ABC, abstractmethod
from item import Item
from cliente import Cliente

class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self.status = "Novo"
    
    @abstractmethod
    def calcular_total(self):
        pass
