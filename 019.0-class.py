variable = "hola chicos como estan el dia de hoy"


conte_letras = {}

for x in variable:
    if x in conte_letras:
        conte_letras[x] += 1
    else:
        conte_letras[x] = 1 

print(conte_letras)








