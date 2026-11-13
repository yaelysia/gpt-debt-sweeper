from .port import MessagePort

class TextProvider(MessagePort):
    def send(self, user, message):
        return f"TO:{user}|{message}"
