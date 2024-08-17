numero = [1, 2, 3, 4, 5, 6]

for numeros in numero:
    cuadrado = numeros**2
    print(f"El cuadrado de {numeros} es {cuadrado}")



# 1. Iterar sobre una lista de números
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)

# 2. Iterar sobre una cadena de caracteres
cadena = "Hola"
for caracter in cadena:
    print(caracter)


# 3. Sumar los elementos de una lista
numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero
print(f"La suma de los números es: {suma}")


# 4. Encontrar el número máximo en una lista
numeros = [0, 1, 2, 3, 4, 0, 5]
maximo = 0
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(f"El número máximo es: {maximo}")



# Funciones básicas de entrada y salida

# Imprimir un mensaje en la consola
print("Hola, Mundo!")


# Leer una entrada desde el usuario
nombre = input("¿Cómo te llamas?")
print(f"Encantado de conocerte, {nombre}")



# Manipulación de cadenas (strings)

# Obtener la longitud de una cadena
cadena = "Hola"
longitud = len(cadena)
print(f"La longitud de la cadena '{cadena}' es {longitud}")


# Convertir una cadena a mayúsculas
mayusculas = cadena.upper()
print(f"La cadena en mayúsculas es: {mayusculas}")


# Convertir una cadena a minúsculas
minusculas = "HOLA".lower()
print(f"La cadena en minúsculas es: {minusculas}")


# Dividir una cadena en una lista
palabras = "Hola mundo".split()
print(f"Dividir la cadena en palabras: {palabras}")


# Eliminar los espacios en blanco al inicio y al final de una cadena
limpia = "  Hola  ".strip()
print(f"Cadena sin espacios en blanco: '{limpia}'")


# Reemplazar una parte de la cadena por otra
nueva_cadena = "Hola mundo".replace("mundo", "Python")
print(f"Cadena modificada: {nueva_cadena}")


# Operaciones con listas

# Crear una lista
lista = [1, 2, 3]

# Obtener la longitud de una lista
longitud_lista = len(lista)
print(f"La longitud de la lista es: {longitud_lista}")

# Añadir un elemento al final de la lista
lista.append(4)
print(f"Lista después de añadir un elemento: {lista}")

# Insertar un elemento en una posición específica
lista.insert(1, 1.5)
print(f"Lista después de insertar un elemento: {lista}")

# Eliminar el primer elemento con el valor especificado
lista.remove(2)
print(f"Lista después de eliminar el elemento '2': {lista}")

# Eliminar y devolver el último elemento de la lista
ultimo_elemento = lista.pop()
print(f"Último elemento eliminado: {ultimo_elemento}")
print(f"Lista después de eliminar el último elemento: {lista}")

# Ordenar la lista en orden ascendente
lista = [3, 1, 2]
lista.sort()
print(f"Lista ordenada: {lista}")

# Invertir el orden de los elementos de la lista
lista.reverse()
print(f"Lista invertida: {lista}")


# Funciones matemáticas

# Sumar todos los elementos de una lista
total = sum([1, 2, 3, 4])
print(f"La suma de los elementos de la lista es: {total}")



