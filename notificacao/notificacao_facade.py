class NotificacaoFacade:
    def enviar_notificacao(self, cliente, mensagem):
        print(f"Enviando notificação para {cliente.nome}: {mensagem}")
