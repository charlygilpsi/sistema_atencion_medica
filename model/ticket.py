from model.incidence import Incidence
from model.technician import Technician
from enum import Enum

class TicketStatus(Enum):
    PENDING = "Pendiente"
    IN_PROCESS = "En proceso"
    CLOSED = "Cerrado"


class Ticket:
    def __init__(self, id: int, incidence: Incidence, technician: Technician, status: TicketStatus = TicketStatus.PENDING) -> None:
        self._id_ticket = id
        self._incidence = incidence
        self._technician = technician
        self._status = status
    
    
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
    def technician(self) -> Technician:
        return self._technician
    
    
    @technician.setter
    def technician(self, technician: Technician) -> None:
        self._technician = technician
        
    
    @property
    def status(self) -> str:
        return self._status
    
    
    @status.setter
    def status(self, status: TicketStatus) -> None:
        self._status = status