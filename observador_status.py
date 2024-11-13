class ObservadorStatus:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, mensagem):
        for observador in self.observadores:
            observador.enviar(mensagem)
