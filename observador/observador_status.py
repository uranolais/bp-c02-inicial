class ObservadorStatus:
    def __init__(self, notificacao):
        self.notificacao = notificacao

    def atualizar(self, pedido):
        mensagem = f"Status do pedido atualizado para: {pedido.status}"
        self.notificacao.enviar_notificacao(pedido.cliente, mensagem)
