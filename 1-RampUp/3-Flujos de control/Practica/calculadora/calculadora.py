from operaciones import Suma, Resta, Multiplicacion, Division, Potencia, HistorialOperaciones
from opciones import Opciones
from excepciones import CalculadoraException
from colores import ColoresTexto

TITULO = """
 $$$$$$\            $$\                     $$\                 $$\                              
$$  __$$\           $$ |                    $$ |                $$ |                             
$$ /  \__| $$$$$$\  $$ | $$$$$$$\ $$\   $$\ $$ | $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  $$$$$$\  
$$ |       \____$$\ $$ |$$  _____|$$ |  $$ |$$ | \____$$\ $$  __$$ |$$  __$$\ $$  __$$\ \____$$\ 
$$ |       $$$$$$$ |$$ |$$ /      $$ |  $$ |$$ | $$$$$$$ |$$ /  $$ |$$ /  $$ |$$ |  \__|$$$$$$$ |
$$ |  $$\ $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ |     $$  __$$ |
\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$ |     \$$$$$$$ |
 \______/  \_______|\__| \_______| \______/ \__| \_______| \_______| \______/ \__|      \_______|    
 
 """

def main():
    print(ColoresTexto.cyan(TITULO))
    historial = HistorialOperaciones()
    while True:
        try:
            mostrar_menu()
            procesar_opcion(input("Selecciona una opcion: ").lower(), historial)
        except CalculadoraException as e:
            print(ColoresTexto.rojo(f"Error: {e}"))
        print()

def procesar_opcion(op, historial):
    if is_operacion_matematica(op):
        try:
            operacion = crear_operacion(op)
            resultado = ColoresTexto.verde(f"El resultado de la {Opciones(op).name.lower()} es: {operacion.__str__()}")
            print(resultado)
            historial.agregar(operacion)
        except ZeroDivisionError as e:
            raise CalculadoraException(ColoresTexto.rojo(str(e)))
    elif op == Opciones.HISTORIAL.value:
        historial.mostrar()
    elif op == Opciones.SALIR.value:
        print(ColoresTexto.magenta("Apagando calculadora..."))
        exit()
    else:
        raise CalculadoraException(ColoresTexto.rojo("Opcion invalida"))

def is_operacion_matematica(op):
    return op in Opciones.math_operations_values()

def mostrar_menu():
    print(ColoresTexto.negrita("Menu:"))
    for opcion in Opciones:
        print(ColoresTexto.cyan(opcion.value) + " -> " + ColoresTexto.azul(opcion.name.title()))
    print()

def crear_operacion(op):
    try:
        print()
        print(ColoresTexto.negrita(f"Operacion '{Opciones(op).name.title()}'"))
        n1 = float(input("Introduce el primer operando: "))
        n2 = float(input("Introduce el segundo operando: "))
        print()
        match op:
            case Opciones.SUMA.value:
                return Suma(n1, n2)
            case Opciones.RESTA.value:
                return Resta(n1, n2)
            case Opciones.MULTIPLICACION.value:
                return Multiplicacion(n1, n2)
            case Opciones.DIVISION.value:
                return Division(n1, n2)
            case Opciones.POTENCIA.value:
                return Potencia(n1, n2)
    except ValueError:
        raise CalculadoraException(ColoresTexto.rojo("Los valores de las operaciones tienen que ser numericos"))

if __name__ == "__main__":
    main()