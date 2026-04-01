from enum import Enum

class EquipmentType(Enum):
    DEKSTOP_PC = "Ordenador de sobremesa"
    LAPTOP = "Ordenador Portátil"
    MOUSE = "Ratón"
    KEYBOARD = "Teclado"
    HEADPHONES = "Auriculares"
    SCREEN = "Pantalla"


class Equipment:
    def __init__(self, id: int, type: EquipmentType) -> None:
        self._id = id
        self._type = type