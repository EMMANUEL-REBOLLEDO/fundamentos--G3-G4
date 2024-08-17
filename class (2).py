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
        self.prestado = False

    def __str__(self):
        if self.prestado:
            estado = "Prestado"
        else:
            estado = "Disponible"
        return f"{self.titulo} de {self.autor} ({self.año}) - Género: {self.genero} - Estado: {estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        nueva_lista_libros = []
        for libro in self.libros:
            if libro.titulo != titulo:
                nueva_lista_libros.append(libro)
        self.libros = nueva_lista_libros

    def buscar_por_titulo(self, titulo):
        libros_encontrados = []
        for libro in self.libros:
            if titulo == libro.titulo:
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_por_autor(self, autor):
        libros_encontrados = []
        for libro in self.libros:
            if autor == libro.autor:
                libros_encontrados.append(libro)
        return libros_encontrados

    def buscar_por_genero(self, genero):
        libros_encontrados = []
        for libro in self.libros:
            if genero == libro.genero:
                libros_encontrados.append(libro)
        return libros_encontrados

    def listar_libros(self):
        return self.libros

    def guardar_datos(self, archivo):
        with open(archivo, "w") as f:
            for libro in self.libros:
                f.write(f"{libro.titulo}, {libro.autor}, {libro.genero}, {libro.año}, {libro.prestado}")



def mostrar_menu():
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Buscar libro por título")
    print("4. Buscar libro por autor")
    print("5. Buscar libro por género")
    print("6. Listar todos los libros")
    print("7. Prestar libro")
    print("8. Devolver libro")
    print("9. Guardar y salir")




biblioteca = Biblioteca()
while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        año = int(input("Año: "))
        libro = Libro(titulo, autor, genero, año)
        biblioteca.agregar_libro(libro)
    
    elif opcion == "2":
        titulo = input("Titulo del lubro a eliminar: ")
        biblioteca.eliminar_libro(titulo)

    elif opcion == "3":
        titulo = input("Titulo: ")
        libros = biblioteca.buscar_por_titulo(titulo)
        for libro in libros:
            print(libro)

    elif opcion == "6":
        libros = biblioteca.listar_libros()
        for libro in libros:
            print(libro)
    
    elif opcion == "7":
        titulo = input("Titulo del libro a Prestar: ")
        resultado = biblioteca.buscar_por_titulo(titulo)
        if resultado:
            resultado[0].prestar()
            print(f"El Libro '{titulo}', ha sido prestado ")
        else:
            print("Libro no encontrado")

    elif opcion == "8":
        titulo = input("Titulo del libro a devolver: ")
        resultado = biblioteca.buscar_por_titulo(titulo)
        if resultado:
            resultado[0].devolver()
            print(f"El Libro '{titulo}', ha sido devuelto ")
        else:
            print("Libro no encontrado")
