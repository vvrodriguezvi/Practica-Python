# Son las posibles películas que ofrece un determinado cine disponibles para ser vistas.

class Pelicula:

    #podria estar otro atributo donde este el formato ?
    peliculas = list()
    def __init__ (self, _nombre, _disponible, _precio = 0):
            self._nombre = _nombre
            self._disponible = _disponible
            self._precio = _precio
            Pelicula.peliculas.append(self)
   
    # getters y setter

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def isDisponible(self):
        return self._disponible

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self.precio = precio

    def __str__(self):
        return self._nombre

    
