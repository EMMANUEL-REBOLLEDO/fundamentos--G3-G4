class calculadora:
    def __init__(self, numero):
        self.resultado = numero

    def suma(self, numero):
        self.resultado += numero

    def resta(self, numero):
        self.resultado -= numero

    def multi(self, numero):
        self.resultado *= numero

    def divi(self, numero):
        if numero != 0:
            self.resultado /= numero
        else:
            "error!: divisio por cero"

    def obt_resultado(self):
        return self.resultado

calculo = calculadora(0)

calculo.suma(5)
calculo.resta(4)
calculo.multi(5)
calculo.divi(2)

resOperaciones = calculo.obt_resultado()
print(resOperaciones)


class calculadora2:
    def suma(self, x, y):
        return x + y 
    def resta(self, x, y):
        return x - y
    def multi(self, x, y):
        return x * y 
    def divi(self, x, y):
        if x == 0:
            return "no se puede dividir por cero "
        else:
            return x / y
        
calculadora = calculadora2()

numero1 = float(input("ingrese numero1: "))
numero2 = float(input("ingrese numero2: "))

print(calculadora.suma(numero1, numero2))
print(calculadora.resta(numero1, numero2))
print(calculadora.multi(numero1, numero2))
print(calculadora.divi(numero1, numero2))

