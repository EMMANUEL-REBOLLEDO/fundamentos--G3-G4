"""class Libro:
    def __init__(self, Titulo, Autor, Genero, Año):
        self.Titulo=Titulo
        self.Autor=Autor
        self.Genero=Genero
        self.Año=Año
        self.prestado=False
    def Prestar(self):
        self.prestado=True
    def Devolver(self):
        self.prestado=False
    def __str__(self):
        return f"el libro es:, {self.Titulo}, Autor:, {self.Autor}, genero:, {self.Genero}, Año:, {self.Año}, estado:, {self.prestado}"


class Biblioteca:
    def __init__(self):
        self.libros=[]

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, Titulo):
        self.libros=[libro for libro in self.libros if libro.Titulo != Titulo]

        self.libros=[]
        for libro in self.libros:
            if libro != libro.Titulo:
                self.libros.append(libro)

    def buscar_por_Titulo(self, Titulo):
        return [libro for libro in self.libros if libro.Titulo == Titulo]

    def buscar_por_Autor(self, Autor):
        return [libro for libro in self.libros if libro.Autor == Autor]

    def buscar_por_genero(self, Genero):
        return [libro for libro in self.libros if libro.Genero == Genero]
    
    def listar_libros(self):
        return self.libros
    
    #def guardar_datos(self, Archivo):

#libro1=Libro("Ilusiones", "Richard", "Ficcion", 1992)

#modo de uso
biblioteca= Biblioteca()

#interfaz de usuario

def Menu_Biblioteca():
    print("Menu Biblioteca Encap24")
    print("1 Agregar Libro")
    print("2 Eliminar Libro4")
    print("3 Buscar Libro por Titulo")
    print("4 Buscar Libro por Autor")
    print("5 Buscar Libro por Genero")
    print("6 Buscar Libro por Genero")
    print("7 listar todos los Libros")
    print("8 Prestar Libro")
    print("9 devolver Libro")
    print("10 Guardar y Salir")




while True:

    Menu_Biblioteca()

    #Menu_Biblioteca()
    opcion=input("seleccione opcion: ")

    if opcion=="1":
        titulo=input("Titulo: ")
        autor=input("Autor: ")
        genero=input("Genero: ")
        año=input("Año: ")
        libro=Libro(titulo, autor, genero, año)
        biblioteca.agregar_libro(libro)
    
    elif opcion=="2":
        titulo=input("Titulo del libro a Eliminar: ")
        biblioteca.eliminar_libro(titulo)

    
    elif opcion=="3":
        titulo=input("titulo del Libro a Buscar: ")
        resultado=biblioteca.buscar_por_Titulo(titulo)
        for libro in resultado:
            print(libro)
    
    
    elif opcion=="4":
        titulo=input("Autor del Libro a Buscar; ")
        resultado2=biblioteca.buscar_por_Autor(autor)
        for libro in resultado2:
            print(libro)

    elif opcion=="5":
        titulo=input("Genero del Libro a Buscar; ")
        resultado3=biblioteca.buscar_por_genero(genero)
        for libro in resultado3:
            print(libro)


    elif opcion=="6":
        for libro in biblioteca.listar_libros():
            print(libro)
    
    elif opcion=="10":
        print("datos guardados...saliendo")
        break"""




class Libro:
    def _init_(self, titulo, autor, genero, año):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
        self.prestado = False

    def prestar(self):
        self.prestado = True

    def devolver(self):
        self.devolver = False

    def _str_(self): 
        return f"{self.libro} {self.estado} Prestado/Disponible "
    

class Biblioteca:
    def _init_(self):
        self.libros = []
        
    def agregar_libros(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros =[libro for libro in self.libros if libro.titulo != titulo]

    def buscar_titulo(self, titulo):
        self.libros =[libro for libro in self.libros if libro.titulo == titulo]

        
    def buscar_autor(self, autor):
        self.libros =[libro for libro in self.libros if libro.autor == autor]

    def buscar_genero(self, genero):
        self.libros =[libro for libro in self.libros if libro.genero == genero]

    def listar_libros(self):
        return self.libros



def menu ():
    print("BIBLIOTECA")
    print("1 Agregar Libro")
    print("2 Eliminar Libro")
    print("3 Buscar Libro por Titulo")
    print("4 Buscar libro por Autor")
    print("5 Buscar libro por Genero")
    print("6 Listar todos los Libros")
    print("7 Prestar Libros")
    print("8 Devolver Libros")
    print("9 Guardar y Salir")

biblioteca = Biblioteca()

while True:
    menu()
    opcion = input("\nSeleccione una opcion: ")
    if opcion == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        año = input("Año: ")
        libro = Libro(titulo, autor, genero, año)

    elif opcion == "2":
        titulo = input("Titulo del Libro a eliminar es: ")
        biblioteca.eliminar_libro(titulo)
       

    elif opcion == "3":
        titulo = input("Titulo del libro a buscar es: ")
        busqueda = biblioteca.buscar_titulo(titulo)
        for libro in busqueda:
            print(libro)

    elif opcion == "4":
        autor = input("Autor del libro a buscar es: ")
        busqueda = biblioteca.buscar_autor(autor)
        for libro in busqueda:
            print(libro)

    elif opcion == "5":
        genero = input("genero del libro a buscar es: ")
        busqueda = biblioteca.buscar_genero(genero)
        for libro in busqueda:
            print(libro)    

    elif opcion == "6":
        for libro in biblioteca.listar_libros():
            print(libro)

    elif opcion == "7":
        titulo = input("Titulo del libro a Prestar: ")
        resultado = biblioteca.buscar_titulo(titulo)
        if resultado:
            resultado[0].prestar()
            print(f"El Libro '{titulo}', ha sido prestado ")
        else:
            print("Libro no encontrado")

    elif opcion == "8":
        titulo = input("Titulo del libro a devolver: ")
        resultado = biblioteca.buscar_titulo(titulo)
        if resultado:
            resultado[0].devolver()
            print(f"El Libro '{titulo}', ha sido devuelto ")
        else:
            print("Libro no encontrado")

    elif opcion == "9":
        print("Datos guardados. Saliendo del Programa")
        break

    else:
        print("Opcion no valida, Intente Nuevamente")
        