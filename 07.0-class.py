def mostrar_menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multip")
    print("4. Divi")

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2


def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion 1 2 3 4 5: ")

        if opcion == '5':
            print("Saliendo de la calculadora...")
            break

        if opcion in ['1', '2', '3', '4']:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            
                if opcion == '1':
                    print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")      
                elif opcion == '2':
                    print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {num1} X {num2} = {multiplicacion(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado: {num1} % {num2} = {division(num1, num2)}")
        else:
            print("Opcion no valida")


calculadora()
