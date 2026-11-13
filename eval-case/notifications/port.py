from abc import ABC, abstractmethod

class MessagePort(ABC):
    @abstractmethod
    def send(self, user, message):
        raise NotImplementedError
