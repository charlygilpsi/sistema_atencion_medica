# TODO class System
# TODO attributes: inventary: list[Equipment], employees: list[Employee], technicians: list[Technicians], incidences: list[Incidence], tickets: list[Ticket]
# TODO methods: check_technicians_availability(), create_ticket()

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