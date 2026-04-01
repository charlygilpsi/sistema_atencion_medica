from model.ticket import Ticket, TicketStatus
from model.incidence import Incidence
from model.employee import Employee

class Technician(Employee):
    def __init__(self, id_employee: int, employee_name: str, employee_code: int, id_technician: int, available: bool = True, ticket_linked: Ticket = None) -> None:
        super().__init__(id_employee, employee_name, employee_code)
        self._id_technician = id_technician
        self._available = available
        self._ticket_linked = ticket_linked
        
    
    @property
    def id_tecnician(self) -> int:
        return self._id_technician
    
    
    @property
    def available(self) -> bool:
        return self._available
    
    
    @available.setter
    def available(self, available: bool) -> None:
        self._available = available
        
    
    @property
    def ticket_linked(self):
        return self._ticket_linked
    
    
    @ticket_linked.setter
    def ticket_linked(self, ticket_linked) -> None:
        self._ticket_linked = ticket_linked
        
    
    def update_ticket_status(self, status: str) -> None:
        self.ticket_linked.status = status
        
    
    def set_incidence_technician_description(self, description: str, incidence: Incidence) -> None:
        incidence.technician_description = description
        
    
    def close_ticket(self, ticket: Ticket) -> None:
        ticket.status = TicketStatus.CLOSED
        self.available = True