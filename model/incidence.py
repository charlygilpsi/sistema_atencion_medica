from model.equipment import Equipment

class Incidence:
    def __init__(self, id: int, employee_code: int, equipment: Equipment, employee_description: str, priority: int) -> None:
        self._id = id
        self._employee_code = employee_code
        self._equipment = equipment
        self._employee_description = employee_description
        self._priority = priority
        self._technician_description = None
        
    
    @property
    def id(self) -> int:
        return self._id
    
    
    @property
    def employee_code(self) -> int:
        return self._employee_code
    
    
    @employee_code.setter
    def employee_code(self, employee_code: int) -> None:
        self._employee_code = employee_code
        
    
    @property
    def equipment(self) -> Equipment:
        return self._equipment
    
    
    @equipment.setter
    def equipment(self, equipment: Equipment) -> None:
        self._equipment = equipment
    
    
    @property
    def employee_description(self) -> str:
        return self._employee_description
    
    
    @employee_description.setter
    def employee_description(self, employee_description: str) -> None:
        self._employee_description = employee_description
    
    
    @property
    def technician_description(self) -> str:
        return self._technician_description
    
    
    @technician_description.setter
    def technician_description(self, technician_description: str) -> None:
        self._technician_description = technician_description
    
    
    @property
    def priority(self) -> int:
        return self._priority
        
    
    @property
    def priority(self, priority) -> None:
        self._priority = priority