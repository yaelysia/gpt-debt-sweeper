class Forwarder:
    def __init__(self, provider):
        self.provider = provider

    def send(self, user, message):
        return self.provider.send(user, message)
