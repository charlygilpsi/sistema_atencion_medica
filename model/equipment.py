from enum import Enum

class EquipmentType(Enum):
    DEKSTOP_PC = "Ordenador de sobremesa"
    LAPTOP = "Ordenador Portátil"
    MOUSE = "Ratón"
    KEYBOARD = "Teclado"
    HEADPHONES = "Auriculares"
    SCREEN = "Pantalla"


class Equipment:
    def __init__(self, id_equipment: int, type: EquipmentType) -> None:
        self._id_equipment = id_equipment
        self._type = type