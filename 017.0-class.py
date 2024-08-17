# modulos

#importacion de modulo completo
"""import math
print(math.sqrt(9))"""

#importacion especifica de un modulo
"""from math import sqrt, pi
print(sqrt(16))
print(pi)"""


#importacion de modulo con alias
"""import math as m
print(m.sqrt(16))"""



import random
numero_aleatorio = random.randint(1, 10)

from mimodulo import es_par, es_inpar

print(f"{numero_aleatorio} es par: {es_par(numero_aleatorio)}")
print(f"{numero_aleatorio} es impar: {es_inpar(numero_aleatorio)}")

