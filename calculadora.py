# calculadora.py

def solicitar_numero(mensaje):
    """Solicita un número al usuario y valida la entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Entrada inválida. Por favor, introduce un número válido.")

def solicitar_operacion():
    """Solicita una operación válida al usuario."""
    operaciones_validas = ('+', '-', '*', '/')
    while True:
        op = input("Introduce la operación a realizar (+, -, *, /): ")
        if op in operaciones_validas:
            return op
        print("❌ Operación inválida. Intenta de nuevo.")

def calcular(numero1, numero2, operador):
    """Realiza el cálculo según la operación solicitada."""
    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        return numero1 * numero2
    elif operador == '/':
        if numero2 == 0:
            return "❌ Error: división entre cero"
        return numero1 / numero2

def mostrar_resultado(resultado):
    """Muestra el resultado al usuario."""
    print(f"✅ Resultado: {resultado}")

def desea_continuar():
    """Pregunta al usuario si desea realizar otra operación."""
    respuesta = input("¿Deseas hacer otra operación? (s/n): ").strip().lower()
    return respuesta == 's'

def main():
    """Función principal del programa."""
    print("🧮 Bienvenido a la Calculadora en Consola")

    while True:
        numero1 = solicitar_numero("Introduce el primer número: ")
        numero2 = solicitar_numero("Introduce el segundo número: ")
        operador = solicitar_operacion()
        resultado = calcular(numero1, numero2, operador)
        mostrar_resultado(resultado)

        if not desea_continuar():
            print("👋 ¡Gracias por usar la calculadora!")
            break

if __name__ == "__main__":
    main()
