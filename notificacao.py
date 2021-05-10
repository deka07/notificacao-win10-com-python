from win10toast import ToastNotifier
import time

notificacao = ToastNotifier()

notificacao.show_toast('Nome da Aplicação', 'Qualquer mensagem relevante', icon_path=None, duration=10, threaded=True)

while notificacao.notification_active():
    time.sleep(5)
