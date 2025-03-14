from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos

class SubscribersRepositoryInsterface(ABC):

    @abstractmethod
    def insert(self, subscriber_infos: dict) -> None:
       pass

    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
        pass