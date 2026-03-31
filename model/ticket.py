from model.incidence import Incidence
from model.technician import Technician
import uuid

class Ticket:
    def __init__(self, incidence: Incidence, technician: Technician, status: str = "Pendiente") -> None:
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
    def status(self, status: str) -> None:
        self._status = status