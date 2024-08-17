"""i = 1

while i <= 10:
    print(i)
    i = i + 1   
"""

# Escribir un programa que solicite al usuario números hasta que introduzca un 0, y luego imprima la suma de todos los números introducidos.



"""numero = int(input("Introduce un numero (0 para terminar)"))
suma = 0

while numero != 0:
    suma = suma  + numero
    numero = int(input("Introduce un numero (0 para terminar): "))

print("La suma es :", suma)

"""


"""def saludar():
    print("Hola")

saludar()
"""

"""def sumar(n1, n2):
    print(n1 + n2)

sumar(1, 2)"""


"""def multiplicar(m1):
    print(m1*1000)

multiplicar(13)"""


# Cuando se usa el elemento max(), devuelve un elemento mas grande
# Crear una funcion que reciba una lista [1, 2, 3, 4, 5] y devuelva el valor maximo

lista = ["Banano", "Manzana", "Kiwi", 4, 5, "Manzana"]
#            0         1         2    3  4

"""def maximo(Lista):
    print(max(Lista))

maximo(lista)

"""

print(lista)
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[0])

lista.append(6)
print(lista)


lista.remove("Manzana")
print(lista)


lista2 = [1, 11, 10, 7, 8, 3]
lista2.sort()
print(lista2)



lista3 = [3, -1, 5, -7, 2, 3]


