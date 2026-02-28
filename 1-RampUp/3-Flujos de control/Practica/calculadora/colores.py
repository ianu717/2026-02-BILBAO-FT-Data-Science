import enum

class ColoresTexto(enum.Enum):
    """Enum para manejar colores en consola usando ANSI escape codes"""
    
    # Códigos de color
    ROJO = '\033[91m'
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BLANCO = '\033[97m'
    
    # Estilos
    NEGRITA = '\033[1m'
    SUBRAYADO = '\033[4m'
    
    # Reset
    RESET = '\033[0m'
    
    @classmethod
    def aplicar_color(cls, color, texto):
        """Aplica un color a un texto"""
        return f"{color.value}{texto}{cls.RESET.value}"
    
    @classmethod
    def rojo(cls, texto):
        return cls.aplicar_color(cls.ROJO, texto)
    
    @classmethod
    def verde(cls, texto):
        return cls.aplicar_color(cls.VERDE, texto)
    
    @classmethod
    def amarillo(cls, texto):
        return cls.aplicar_color(cls.AMARILLO, texto)
    
    @classmethod
    def azul(cls, texto):
        return cls.aplicar_color(cls.AZUL, texto)
    
    @classmethod
    def magenta(cls, texto):
        return cls.aplicar_color(cls.MAGENTA, texto)
    
    @classmethod
    def cyan(cls, texto):
        return cls.aplicar_color(cls.CYAN, texto)
    
    @classmethod
    def negrita(cls, texto):
        return cls.aplicar_color(cls.NEGRITA, texto)
