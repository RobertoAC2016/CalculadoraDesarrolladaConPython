import os
while True:
    print("Bienvenido a la calculadora\n")
    print("Option 1: Suma")
    print("Option 2: Resta")
    print("Option 3: Divicion")
    print("Option 4: Multiplicacion")
    operacion = 0
    try:
        operacion = int(input("Dime q operacion desesas realizar:"))
    except:
        pass
    if operacion >= 1 and operacion <= 4:
        print(f"Tu operacion se la opcion: {operacion}")
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        if operacion == 1:
            resultado = num1 + num2
            print(f"El resultado es: {resultado}")
        elif operacion == 2:
            resultado = num1 - num2
            print(f"El resultado es: {resultado}")
        elif operacion == 3:
            resultado = num1 / num2
            print(f"El resultado es: {resultado}")
        elif operacion == 4:
            resultado = num1 * num2
            print(f"El resultado es: {resultado}")
        else:
            print("Operacion invalida")
    else:
        print(f"Tu operacion es invalida: {operacion}")
    pausa = input("Presiona cualquier tecla para continua")
    os.system("cls")