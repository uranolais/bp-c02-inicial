from notificacao import Notificacao

class NotificacaoEmail(Notificacao):
    def enviar(self, cliente, mensagem):
        print(f"Enviando e-mail para {cliente.nome}: {mensagem}")
