import uuid

class Incidence:
    def __init__(self, employee_code: int, description: str, priority: int) -> None:
        self._employee_code = employee_code
        self._description = description
        self._priority = priority
        self._id_incidence = uuid.uuid4()
        # uuid.UUID
        
    
    @property
    def employee_code(self) -> int:
        return self._employee_code
    
    
    @employee_code.setter
    def employee_code(self, employee_code: int) -> None:
        self._employee_code = employee_code
        
    
    @property
    def description(self) -> str:
        return self.description
    
    
    @description.setter
    def description(self, description: str) -> None:
        self._description = description
    
    
    @property
    def priority(self) -> int:
        return self._priority
        
    
    @property
    def priority(self, priority) -> None:
        self._priority = priority