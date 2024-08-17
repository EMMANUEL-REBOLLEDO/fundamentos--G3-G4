"""lista = [25, 26, 27, 28, 29]

print(lista[-2])

lista.append(5)
print(lista)

lista.remove(28)
lista.insert(3,9)
print(lista)

lista[3] = 8
print(lista)

del lista[0]
print(lista)

print(sum(lista))"""

"""frutas = ("mazana", "pera", "mango", "kiwi")
print(frutas[1])
print(frutas[-1])

lista_frutas = list(frutas)
print(frutas)
print(lista_frutas)

lista_frutas.append("papaya")
print(lista_frutas)
print(tuple(lista_frutas))


lista_frutas = list[frutas]
for i in lista_frutas:
    print(i)

for i in frutas:
    print(i)"""

contacto = {"juan": "123456", 
            "juana": "876543", 
            "pedro": "567098" }

print(contacto["juan"])

contacto["ana"] = "787878"
print(contacto)

del contacto["pedro"]
print(contacto)

for i, m in contacto.items():
    print(f"{i}: {m}")
