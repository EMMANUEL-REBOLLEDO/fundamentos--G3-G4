"""class pikachu:
    tipo = "Elecntrico"

    def __init__(self, nombre, nivel, sal):
        self.nombre = nombre
        self.nivel = nivel
        self,salud = sal"""



"""class Dog:
    especie = "canino"

    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad =  Edad


dog_1 = Dog("Tony", 3)
dog_2 = Dog("firulays", 5)

print(dog_1.especie, dog_1.Nombre, dog_1.Edad)
print(dog_2.especie, dog_2.Nombre, dog_2.Edad)"""

class Dog:
    especie = "canino"
    
    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad = Edad

    def  ladrido(self):
        print(f"{self.Nombre}, dice woof! woof!")

    def descripcion(self):
        return f"{self.Nombre}, y tiene {self.Edad} años"
    
    def celebracion(self):
        return self.Edad + 1

dog_1 = Dog("Tony", 3)
dog_2 = Dog("firulays", 5)

print(dog_1.especie, dog_1.Nombre, dog_1.Edad)
print(dog_2.especie, dog_2.Nombre, dog_2.Edad)

dog_1.ladrido()
dog_2.ladrido()

print(dog_1.descripcion())
print(dog_2.descripcion())

dog_1.celebracion()
print(dog_1.celebracion())
dog_2.celebracion()
print(dog_2.celebracion())

