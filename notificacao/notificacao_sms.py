from notificacao.notificacao import Notificacao

class NotificacaoSMS(Notificacao):
    def enviar(self, cliente, mensagem):
        print(f"Enviando SMS para {cliente.nome}: {mensagem}")
