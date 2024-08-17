class DispositioElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo =modelo 

    def encender(self):
        return f"este dispositivo esta encendido"
    
class telefono(DispositioElectronico):
    
    def hacer_llamada(self, numero):
        return f"se esta llamado al numero {numero}"


class  portatil(DispositioElectronico):
   
    def abrir_programa(self, programa):
        return f"{self.marca} {self.modelo} abriendo programa {programa}"
    
Telefono = telefono("xiaomi", "11t")

Portatil = portatil("dell", "cx0")

print(Telefono.marca, Telefono.modelo)
print(Portatil.marca, Portatil.modelo)

print(Telefono.hacer_llamada(3053577738))
print(Portatil.abrir_programa("python"))


print(Telefono.encender())
print(Portatil.encender())




    