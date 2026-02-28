import enum

class Opciones(enum.Enum):
    """Enum que define las opciones disponibles en la calculadora"""

    SUMA = 's'
    RESTA = 'r'
    MULTIPLICACION = 'm'
    DIVISION = 'd'
    POTENCIA = 'p'
    HISTORIAL = 'h'
    SALIR = 'e'

    @classmethod
    def values(opciones_enum):
        return [opcion.value for opcion in opciones_enum]
    
    @classmethod
    def math_operations_values(opciones_enum):
        return [opcion.value for opcion in opciones_enum if opcion.value in ['s', 'r', 'm', 'd', 'p']]
