#Ejercicio 1: Clasificación de números
entero = int(input("Ingrese un número entero: "))

if entero > 0:
    print(f"{entero} es un número positivo")
elif entero == 0:
    print("El número es cero")
else:
    print(f"{entero} es un número negativo")

#Ejercicio 2: Calculadora de área de figuras geométricas

print("\nMenú de cálculo de áreas:")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Triángulo")
print("4. Círculo")
print("0. Salir")

opcion = int(input("Ingrese la opción deseada: "))

if opcion == 1:
    lado = float(input("Ingrese la medida del lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area:.2f}")
elif opcion == 2:
    base = float(input("Ingrese la medida de la base del rectángulo: "))
    altura = float(input("Ingrese la medida de la altura del rectángulo: "))
    area = base * altura
    print(f"El área del rectángulo es: {area:.2f}")
elif opcion == 3:
    base = float(input("Ingrese la medida de la base del triángulo: "))
    altura = float(input("Ingrese la medida de la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area:.2f}")
elif opcion == 4:
    radio = float(input("Ingrese la medida del radio del círculo: "))
    area = 3.1416 * radio * radio
    print(f"El área del círculo es: {area:.2f}")
elif opcion == 0:
    print("Saliendo del programa")

else:
    print("No ha selecionado una opcion correcta")


# match version 3.10

#Ejercicio 3 explicando el Match
variable3 = 2
match variable3:
    case 1:
        print("uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case _:
        print("Numero no reconocido")


#Ejercicio 4

inputPar = int(input("Ingrese un numero"))
match inputPar:
    case 0:
        print("Es cero")
    case inputPar if inputPar % 2 == 0:
        print("Es par")
    case inputPar if inputPar % 2 == 1:
        print("Es impar")    
    case _:
        print("Numero no reconocido")


numero3 = int(input("Ingrese un numero"))
match numero3:
    case numero3 if numero3 < 0:
        print("Numero negativo")
    case numero3 if numero3 >=0 and numero3 <= 9:
        print("Numero de 0 a 10")
    case _:
        print("Numero Mayor o igual a 10")