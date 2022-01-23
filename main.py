import time
from gi.repository import GLib, Notify
from YFinance import getFinanceData, NAMES
import webbrowser

class Notifier():
    def __init__(self):
        Notify.init('Yahoo Finance')
        self.old_data = getFinanceData()
        self.create_notify()
        self.verify()

    def create_notify(self):
        self.notify = Notify.Notification.new("","")
        self.notify.set_timeout(15000)
        self.notify.add_action('clicked', 'Conocer más', self.onClick, None)

    def verify(self):
        msj = ""
        news = "ha subido"
        icon = "face-surprise"

        new_data = getFinanceData()
        
        for i in self.old_data:
            diff = abs(new_data[i] - self.old_data[i])
            if diff >= 0.5:
                if new_data[i] < self.old_data[i]:
                    news = "ha bajado"

                msj += (
                    f"<i>{NAMES[i]} {news} {round(diff,3)}</i>\n"
                    f"De: {self.old_data[i]} a <b>{new_data[i]}</b>\n{('_'*34)}\n"
                )
                self.old_data[i] = new_data[i]
        if msj != "":
            if "bajado" in msj and "subido" in msj:
                icon = "face-uncertain"
            elif "subido" not in msj:
                icon = "face-sad"
            self.notify.update("Noticias", msj, icon=icon)
            self.notify.show()

        GLib.timeout_add_seconds(60*5, self.verify)
        
    def onClick(self, notification, action_name, data):
        webbrowser.open('www.smartrader.io')

if __name__ == "__main__":
    n = Notifier()
    GLib.MainLoop().run()