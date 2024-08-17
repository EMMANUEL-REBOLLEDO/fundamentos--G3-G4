#Esta linea de comentario


"""Esto es un parrafor 
Esto me permite escribir de esta manera"""

nombre = "Jesus"  #variable tipo texto (str)
edad = 26         #Variable tipo numero  (int)
altura = 1.76     #Variables tipo flotante (float)
activo = True     #Variables tipo Booleana (bool)


"""print(type(nombre))
print(type(edad))
print(type(altura))
print(type(activo))
"""

variable1 = variable2 = variable3 = "Marco"

"""print(variable1)
print(variable2)
print(variable3)
"""

variable4, variable5, variable6 = "Marcos", "Pablo", "Maria"

"""print(variable4)
print(variable5)
print(variable6)"""


"""print("Hola mi nombre es", nombre)
print(f"Hola Mi nombre es {nombre} y tengo {edad} años")""" #Interpolacion o texto dinamico


"""cadenaInput = input("Ingrese su nombre: ")
print(cadenaInput)
numeroInput = int(input("Ingrese su edad: "))
print(numeroInput)
decimalInput = float(input("Ingrese su altura: "))
print(decimalInput)"""



#Operadores aritmeticos

a = 10
b = 5


suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
resto = a % b
potencia = a ** b

"""print(suma)
print(resta)
print(multiplicacion)
print(division)
print(resto)
print(potencia)
"""

#Operadores comparativos
a = 10
b = 5

igual = (a == b)
desigualdad = (a != b)
mayor_que = (a > b)
menor_que = (a < b)

print("Igualdad", igual)
print("Desigualdad", desigualdad)
print("Mayor que", mayor_que)
print("Menor que", menor_que)


#Operadores Logicos

# Tabla de verdad del operador 'and' (y lógico):
"""
Operando A | Operando B | A and B
-----------------------------------
    True   |    True    |  True
    True   |   False    |  False
    False  |    True    |  False
    False  |   False    |  False
"""


# Tabla de verdad del operador 'or' (o lógico):
"""
Operando A | Operando B | A or B
----------------------------------
    True   |    True    |  True
    True   |   False    |  True
    False  |    True    |  True
    False  |   False    |  False
"""


# Tabla de verdad del operador 'not' (negación):
"""
Operando |  not Operando
-------------------------
    True  |     False
    False |     True
"""



"""numero = 8

if numero % 3 == 0:
    print("el numero es par")

else:
    print("el numero es impar")"""








peso = float(input("ingrese su peso en Kg: "))
altura = float(input("ingrese su altura: "))

imc = peso / (altura*altura)

if imc < 18.5:
    print("peso bajo")

elif imc >= 18.5 and  imc <= 24.9:
    print("peso normal")

elif imc >= 25 and imc <= 29.9:
    print("sobrepeso")

else:
    print("obesidad")