# Introducción a las Estructuras Condicionales

"""Las estructuras condicionales en Python permiten controlar el flujo de ejecución de un programa en base a la evaluación de una o más condiciones. Estas condiciones pueden ser valores booleanos, comparaciones entre variables o expresiones matemáticas.
**Sintaxis:**
La estructura condicional básica en Python es la sentencia `if`. Su sintaxis es la siguiente:"""


#///////////////////////////////////////////////////////////////////////////////////////

variable = 6

if variable <= 5:
    print(f"El numero {variable}, es menor")
else:
    #Bloque si no hay ejecutar
    print(f"el numero {variable}, es mayor")




#///////////////////////////////////////////////////////////////////////////////////////

variable2 = 4

if variable2 == 1:
    print(1)
elif variable2 == 2:
    print("Dos")
elif variable2 == 3:
    print("Tres")
else:
    print("Seleccione un rango acorde")


#///////////////////////////////////////////////////////////////////////////////////////

numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: "))

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero2} es mayor que {numero1}")
else:
    print("Los numero son iguales")


#///////////////////////////////////////////////////////////////////////////////////////

"""
Rango de IMC Clasificación
Menos de 18.5     --> Bajo peso
Entre 18.5 y 24.9 --> Peso normal
Entre 25 y 29.9	  --> Sobrepeso
30 o más	      --> Obesidad
"""

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

if imc < 18.5:
    clasificacion = "Bajo peso"
elif imc < 25:
    clasificacion = "Peso normal"
elif imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print(f"Su IMC es: {imc:.2f}")
print(f"Su clasificación es: {clasificacion}")