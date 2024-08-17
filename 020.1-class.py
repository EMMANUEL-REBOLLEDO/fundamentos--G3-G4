class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        return (f"{self.marca}{self.modelo} esta en marcha")
    
    def detener(self):
        return (f"{self.marca}{self.modelo}  se ha detenido")
    
class Carro(Vehiculo):
    def abrir_maletero(self):
        return (f"el maletero de {self.marca}{self.modelo} esta abierto")
    
class Moto(Vehiculo):
    def hacer_caballito(self):
        return (f"{self.marca}{self.modelo} esta haciendo caballito")

carro = Carro("toyota","prado")
moto = Moto("yamaha","mt-07")

print(carro.arrancar())
print(moto.arrancar())
print(carro.detener())
print(moto.detener())
print(carro.abrir_maletero())
print(moto.hacer_caballito())