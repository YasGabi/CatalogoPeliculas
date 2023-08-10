import os 
class Pelicula:
    def __init__(self,nombre):
        self.__nombre = nombre

    def __str__(self):
        return f"Pelicula: {self.nombre}"
    
    def met_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre

class CatalogoPeliculas:
    def __init__(self,nombre):
        self.nombre = nombre
        self.ruta_archivo = f"{self.nombre}.txt"

    def agregar_pelicula(self,pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(f"{pelicula.nombre}")

    def listar_pelicula(self,pelicula):
         with open(self.ruta_archivo,"a") as archivo:
             archivo.read(pelicula.nombre)
             print(f"Listado: \n{pelicula.nombre}\n")

    def eliminar_pelicula(self):
        os.remove(self.ruta_archivo)
        print ("El catalogo ha sido eliminado")

        