from abc import ABC, abstractmethod
from item import Item
from cliente import Cliente
from observador_status import ObservadorStatus

class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self.status = "Novo"
        self.observador_status = ObservadorStatus()
    
    @abstractmethod
    def calcular_total(self):
        pass

    def enviar_notificacao(self, notificacao, mensagem):
        notificacao.enviar(self.cliente, mensagem)
    
    def adicionar_observador(self, observador):
        self.observador_status.adicionar_observador(observador)

    def atualizar_status(self, novo_status):
        self.status = novo_status
        self.observador_status.notificar_observadores(f"Status atualizado para: {novo_status}")
