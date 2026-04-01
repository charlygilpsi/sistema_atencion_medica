from model.incidence import Incidence
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.technician import Technician

class TicketStatus(Enum):
    PENDING = "Pendiente"
    IN_PROGRESS = "En proceso"
    CLOSED = "Cerrado"


class Ticket:
    def __init__(self, id: int, incidence: Incidence, technician: "Technician | None") -> None:
        self._id = id
        self._incidence = incidence
        self._technician = technician
        self._status = self.set_status_depending_on_technician()
    
    
    @property
    def id(self) -> int:
        return self._id
    
    
    @property
    def incidence(self) -> Incidence:
        return self._incidence
    
    
    @incidence.setter
    def incidence(self, incidence: Incidence) -> None:
        self._incidence = incidence
        
    
    @property
    def technician(self) -> "Technician":
        return self._technician
    
    
    @technician.setter
    def technician(self, technician: "Technician") -> None:
        self._technician = technician
        
    
    @property
    def status(self) -> TicketStatus:
        return self._status
    
    
    @status.setter
    def status(self, status: TicketStatus) -> None:
        self._status = status
        
    
    def set_status_depending_on_technician(self) -> TicketStatus:
        if self.technician:
            return TicketStatus.IN_PROGRESS
        else:
            return TicketStatus.PENDING