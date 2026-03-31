class Employee:
    def __init__(self, id_employee: int, employee_code: int) -> None:
        self._id_employee = id_employee
        self._employee_code = employee_code
        
        
    @property
    def id_employee(self) -> int:
        return self._id_employee
    
    
    @property
    def employee_code(self) -> int:
        return self._employee_code
    
    
    @employee_code.setter
    def employee_code(self, employee_code: int) -> None:
        self._employee_code = employee_code

    
    def report_incidence(self, description: str, priority: int) -> tuple[str, int, int]:
        return [description, priority, self.employee_code]