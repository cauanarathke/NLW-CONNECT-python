from abc import ABC, abstractmethod
from src.model.entities.eventos_link import Eventos_link

class EventosLinkRepositoryInterface():

    @abstractmethod
    def insert(self, event_id: id, subscriber_id: int) -> str: pass
        
    @abstractmethod    
    def select_event_link(self, event_id: id, subscriber_id: int) -> Eventos_link: pass
       