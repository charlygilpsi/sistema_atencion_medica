from model.incidence import Incidence
from model.technician import Technician
from enum import Enum
import uuid

class TicketStatus(Enum):
    PENDING = "Pendiente"
    IN_PROCESS = "En proceso"
    CLOSED = "Cerrado"


class Ticket:
    def __init__(self, incidence: Incidence, technician: Technician, status: TicketStatus = TicketStatus.PENDING) -> None:
        self._incidence = incidence
        self._technician = technician
        self._status = status
        self._id_incidence = uuid.uuid4()
        
    
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