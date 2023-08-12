import os 
class Pelicula:
    def __init__(self,nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"Pelicula: {self.nombre}"
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

class CatalogoPeliculas:
    def __init__(self,nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{self.nombre}.txt"

    def agregar_pelicula(self,pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f"-{pelicula.nombre}\n")

    def listar_pelicula(self):
         print("\n---CATALOGO DE PELICULAS---")
         with open(self.ruta_archivo, 'r') as archivo:
            print(archivo.read())

    def eliminar_pelicula(self):
        os.remove(self.ruta_archivo)
        print (f"El catalogo {self.ruta_archivo} ha sido eliminado\n")