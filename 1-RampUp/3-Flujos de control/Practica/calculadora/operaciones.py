from abc import ABC, abstractmethod

class OperacionMatematica(ABC):
    def __init__(self, n1, n2, s):
        self.n1 = n1
        self.n2 = n2
        self.s = s

    @abstractmethod
    def calcular(self):
        pass

    def __str__(self):
        return f"{self.n1} {self.s} {self.n2} = {self.calcular()}"

class Suma(OperacionMatematica):
    def __init__(self, n1, n2):
        super().__init__(n1, n2, '+')
        
    def calcular(self):
        return self.n1 + self.n2

class Resta(OperacionMatematica):
    def __init__(self, n1, n2):
        super().__init__(n1, n2, '-')

    def calcular(self):
        return self.n1 - self.n2

class Multiplicacion(OperacionMatematica):
    def __init__(self, n1, n2):
        super().__init__(n1, n2, 'x')

    def calcular(self):
        return self.n1 * self.n2

class Division(OperacionMatematica):
    def __init__(self, n1, n2):
        super().__init__(n1, n2, '/')

    def calcular(self):
        if self.n2 == 0:
            raise ZeroDivisionError("No se puede dividir entre 0")
        return self.n1 / self.n2

class Potencia(OperacionMatematica):
    def __init__(self, n1, n2):
        super().__init__(n1, n2, '^')

    def calcular(self):
        return self.n1 ** self.n2

class HistorialOperaciones:
    def __init__(self):
        self.historial = []
    
    def agregar(self, operacion):
        self.historial.append(operacion)
    
    def mostrar(self):
        from colores import ColoresTexto
        print()
        if len(self.historial) == 0:
            print(ColoresTexto.amarillo("No hay operaciones en el historial"))
        else:
            print(ColoresTexto.negrita(f"Historial de operaciones (Total: {len(self.historial)})"))
            print("\n".join(ColoresTexto.cyan(f"- {operacion.__str__()}") for i, operacion in enumerate(self.historial)))
