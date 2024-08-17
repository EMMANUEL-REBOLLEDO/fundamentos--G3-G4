#print(123)
"""
a = 5
b = 3

if a < 3 or b > 2:
    suma = a + b
    print(suma)
else:
    print("No verdadero")
"""

"""# Bool Not
mayorDeEdad = False

if not mayorDeEdad:
    print("Mayor de edad")
else:
    print("Menor de edad")
"""

#///////////////////////////////////////////////////////////////////////
"""variablex = 101

if variablex <= 100:
    if variablex <= 50:
        print("Numero menor a 50 primer if", variablex)
    else:
        print("Numero mayor a 50")
    if variablex >= 51:
        print("Mayor o igual a 51 segundo if", variablex)
    else:
        print("Numero menor a 50")
else:
    print("Numero mayor a 100")
"""

#//////////////////////////////////////////////////////////////////
"""numero = range(5) #[0, 1, 2, 3, 4]

print("Inicio")

for i in numero:
    # i = +1
    print(i, "Hola")

print("Fin")
"""


#tabla = int(input("Que tabla quieres imprimir: "))

for n in range(1, 13):
    print(f"Tabla del {n}")
    for i in range(1, 11):
     print(n, "X", i, "=", i*n)


