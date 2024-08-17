class Libro:
    def __init__(self, titulo, autor, genero, año, ):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año 
        self.prestado = False

    def prestar(self):
        self.prestado = True
    def devolver(self):
        self.prestado = False

    def __str__(self):
        return f"el libro con titulo {self.titulo} y de autor {self.autor} con genero{self.genero} y del año {self.año}esta en el estado {self.prestado} "
    
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    
    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def buscar_por_titulo(self, titulo):
        return  [libro for libro in self.libros if libro.titulo == titulo]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if libro.autor == autor ]

    def buscar_por_genero(self, genero):
        return [libro for libro in self.libros if libro.genero == genero ]

    def listar_libros(self):
        return self.libros

"""print(---------------------------------)"""

biblioteca = Biblioteca()

def menu():
    print("biblioteca")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Buscar libro por titulo")
    print("4. Buscar lirbo por autor")
    print("5. Buscar libro por genero")
    print("6. Listar todos lo libros")
    print("7. Pretar libro ")
    print("8. Devolver libro")
    print("9. Guardar y salir")

while True:
    menu()
    opcion = input("selecione una opcion: ")   

    if opcion == "1":
        Titulo = input("Titulo ")
        Autor = input("Autor ")
        Genero = input("Genero ")
        Año = input("Año ")
        libro = Libro(Titulo, Autor, Genero, Año)
        biblioteca.agregar_libro(libro)
    
    elif opcion == "2":
        titulo = input("titulo del libro a eliminar: ")
        biblioteca.eliminar_libro(titulo)

    elif opcion == "3":
        titulo = input("titulo del libro a buscar ")
        resultado = biblioteca.buscar_por_titulo(titulo)
        for libro in resultado:
            print(libro)

    elif opcion == "4":
        Autor = input("autor del libro a buscar ")
        resultado = biblioteca.buscar_por_autor(Autor)
        for libro in resultado:
            print(libro)

    elif opcion == "5":
        Genero = input("Genero del libro a buscar")
        resultado = biblioteca.buscar_por_genero(Genero)
        for libro in resultado:
            print(libro)



    elif opcion == "6":
        for libro in biblioteca.listar_libros():
            print(libro)

    elif opcion == "9":
        print("Datos guardados. saliendo del sistema")
        break

    

