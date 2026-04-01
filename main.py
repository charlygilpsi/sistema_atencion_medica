from model.employee import Employee
from model.equipment import Equipment, EquipmentType
from model.incidence import  Priority
from model.system import System
from model.technician import Technician

employee_1 = Employee(1, "José María Aznar", 1)
equipment_1 = Equipment(1, EquipmentType.DEKSTOP_PC)
technician_1 = Technician(2, "George W. Bush", 2, 1, True)
system_1 = System([equipment_1], [employee_1], [technician_1])

report = employee_1.report_incidence(equipment_1, "Hace mucho ruido", Priority.ALTA)
incidence_1 = system_1.create_incidence(employee_1.employee_code, report[0], report[1], report[2])
available_technician_1 = system_1.check_for_an_available_technician()
ticket_1 = system_1.create_ticket(incidence_1, available_technician_1)

print(ticket_1.id)