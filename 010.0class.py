class car:
    
    def __init__(self, marca, modelo, velocidad_max, precio):
        self.marca = marca
        self.modelo = modelo
        self.__veloxidad_max = velocidad_max
        self.__precio = precio

    def acelerar(self):
        
        print(f"El carro acelera a {self. __veloxidad_max}")

carro = car("mazda", "cx30", "150km/h" , 130000000)

carro.acelerar()


