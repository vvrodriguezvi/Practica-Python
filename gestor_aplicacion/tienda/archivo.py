# El archivo se encarga de almacenar las peliculas de los cuales
# dispone la empresa de cinemas, que puede usar el supervisor para modificar la taquilla.


class Archivo:
    _peliculas = []

    @classmethod
    def agregarPelicula(cls, pelicula):
        cls._peliculas.append(pelicula)

    # El metodo sacar pelicula: eliminar determinada pelicula de la taquilla del archivo disponible del cine ??

    @classmethod
    def sacarPelicula(cls, nombre):
        if type(nombre) is str:
            for pelicula in cls._peliculas:
                if pelicula.getNombre() == nombre:
                    return pelicula
            return None
        else:
            cls._peliculas.remove(nombre)
            return nombre

    @classmethod
    def getPeliculas(cls):
        return cls._peliculas

    @classmethod
    def setPeliculas(cls, peliculas):
        cls._peliculas = peliculas
