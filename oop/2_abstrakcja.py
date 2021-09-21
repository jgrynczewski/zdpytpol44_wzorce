class MailService:
    def __connect(self):
        print("Connect")

    def __autheticate(self):
        print("Authenticate")

    def __disconnect(self):
        print("Disconnect")

    def __send_main(self):
        print("Send mail")

    def send_mail(self):
        self.__connect()
        self.__autheticate()
        self.__send_mail()
        self.__disconnect()


m = MailService()
m.send_mail()
