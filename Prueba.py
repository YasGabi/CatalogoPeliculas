from CatalogoPeliculas import *

resp = None

nombre_catalogo = input("Ingrese el nombre del catalogo que desea crear: ")
catalogo = CatalogoPeliculas(nombre_catalogo)

while resp != 4:
    try:
        print("-----MENU-----")
        print("1 - Agregar Pelicula")
        print("2 - Listar Peliculas")
        print("3 - Eliminar catalogo")
        print("4 - Salir")

        resp = int(input("Seleccione la opcion deseada: "))

        if resp==1:
            nombre_pelicula = input("Ingrese el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            catalogo.agregar_pelicula(pelicula)
        elif resp==2:
            catalogo.listar_pelicula()
        elif resp==3:
            catalogo.eliminar_pelicula()
    except Exception as e:
        print("La opcion ingresada es incorrecta")
        resp = 4
else:
    print("---Sistema finalizado---")
    print("Nos vemos!")