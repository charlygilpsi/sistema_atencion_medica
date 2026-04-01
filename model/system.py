from model.equipment import Equipment
from model.employee import Employee
from model.incidence import Incidence
from model.technician import Technician
from model.ticket import Ticket

class System:
    def __init__(self, inventory: list[Equipment], employees: list[Employee], technicians: list[Technician], incidences: list[Incidence] = [], tickets: list[Ticket] = []):
        self._inventory = inventory
        self._employees = employees
        self._technicians = technicians
        self._incidences = incidences
        self._tickets = tickets
        
    
    @property
    def inventory(self) -> list[Equipment]:
        return self._inventory
    
    
    @inventory.setter
    def inventory(self, inventory: list[Equipment]) -> None:
        self._inventory = inventory
        
    
    @property
    def employees(self) -> list[Employee]:
        return self._employees
    
    
    @employees.setter
    def employees(self, employees: list[Employee]) -> None:
        self._employees = employees
        
    
    @property
    def technicians(self) -> list[Technician]:
        return self._technicians
    
    
    @technicians.setter
    def technicians(self, technicians: list[Technician]) -> None:
        self._technicians = technicians
        
    
    @property
    def incidences(self) -> list[Incidence]:
        return self._incidences
    
    
    @incidences.setter
    def incidences(self, incidences) -> None:
        self._incidences = incidences
        
    
    @property
    def tickets(self) -> list[Ticket]:
        return self._tickets
    
    
    @tickets.setter
    def tickets(self, tickets: list[Ticket]) -> None:
        self._tickets = tickets
        
    
    def auto_increment_id(self, items: list) -> int:
        max_id = 0
        
        for item in items:
            if item.id > max_id:
                max_id = item.id
                
        return max_id + 1
    
    
    def create_incidence(self, employee_code: int, equipment: Equipment, employee_description: str, priority: int) -> None:
        id = self.auto_increment_id(self.incidences)
        incidence = Incidence(id, employee_code, equipment, employee_description, priority)
        self._incidences.append(incidence)
    
    
    def create_ticket(self, incidence: Incidence, technician: Technician | None) -> None:
        id = self.auto_increment_id(self.tickets)
        ticket = Ticket(id, incidence, technician)
        self._tickets.append(ticket)
    
    
    def check_for_an_available_technician(self) -> Technician | None:
        for technician in self.technicians:
            if technician.available:
                technician.available = False
                
                return technician
            
        return None