from abc import ABC, abstractmethod

## abstract class
class NotificationalChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass