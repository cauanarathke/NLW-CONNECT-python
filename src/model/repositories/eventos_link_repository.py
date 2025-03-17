import random
from src.model.configs.connection import DBConnectionHandler
from src.model.entities.eventos_link import Eventos_link
from .interfaces.eventos_link_repository import EventosLinkRepositoryInterface

class EventosLinkRepository(EventosLinkRepositoryInterface):
    def insert(self, event_id: id, subscriber_id: int) -> str:
        with DBConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices('0123456789', k=7))
                formatted_link = f'evento-{event_id}-{subscriber_id}-{link_final}'

                new_event_link = Eventos_link(
                    evento_id=event_id, 
                    inscrito_id=subscriber_id,
                    link=formatted_link
                )
                db.session.add(new_event_link)
                db.session.commit()

                return formatted_link
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_event_link(self, event_id: id, subscriber_id: int) -> Eventos_link:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Eventos_link)
                .filter (
                    Eventos_link.evento_id == event_id,
                    Eventos_link.inscrito_id == subscriber_id
                )
                .one_or_none()
            )
            return data