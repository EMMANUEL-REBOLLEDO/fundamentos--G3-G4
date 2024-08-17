class Libro:
    def __init__(self, titulo, autor, genero, año):
         self.titulo = titulo
         self.autor = autor
         self.genero = genero
         self.año = año
         self.prestado = False

    def prestar(self):
         self.prestado = True
    def devolver(self):
         self.devolver = False

    def __str__(self):
         return f"{self.titulo} {self.autor} {self.genero} {self.año} {self.prestado} el libro con autor con genero y con año"
     
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def buscar_por_titulo(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo == titulo]

    def buscar_por_autor(self, autor):
        self.libros = [libro for libro in self.libros if libro.autor == autor]  

    def buscar_por_genero(self, genero):
        self.libros = [libro for libro in self.libros if libro.genero == genero]  
    
    def listar_libros(self):
        self.libros
    

def menu():
    print("Biblioteca")
    print("1 Agregar Libro")
    print("2 Eliminar Libro")
    print("3 Buscar Libro Por Titulo")
    print("4 Buscar Libro Por Autor")
    print("5 Buscar Libro Por Genero")
    print("6 Listar Todos Los Libros")
    print("7 Prestar Libros")
    print("8 Devolver Libro")
    print("9 Guardar Y Salir")

biblioteca = Biblioteca()

while True:

    menu()
    Opcion = input("Seleccione Una Opcion")
    
    if Opcion == "1":
        titulo = input("Titulo")
        autor = input("autor")
        genero = input("genero")
        año = input("año")
        libro = Libro(titulo, autor, genero, año)
        biblioteca.agregar_libro(libro)

    
    elif Opcion == "6":
        for libro in biblioteca.listar_libros():
            print(libro)
            
    elif Opcion == "9":
        print("datos guardados, saliendo del sistema")
        break