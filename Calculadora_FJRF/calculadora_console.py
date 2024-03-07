def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b

def main():
    print("Bienvenido a la calculadora.")
    a = float(input("Ingrese el primer número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    b = float(input("Ingrese el segundo número: "))

    if operacion == '+':
        resultado = suma(a, b)
    elif operacion == '-':
        resultado = resta(a, b)
    elif operacion == '*':
        resultado = multiplicacion(a, b)
    elif operacion == '/':
        resultado = division(a, b)
    else:
        resultado = "Operación no válida"
    print("El resultado es:", resultado)

if __name__ == "__main__":
    main()
