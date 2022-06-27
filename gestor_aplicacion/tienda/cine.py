# Esta clase busca representar la disponibilidad de una pelicula en determinado cine (son varios) 
# el cual se espera ser reservado (la pelicula) por el usuario.
# Estructuras relevantes: peliculas corresponde a la lista de todas
# los peliculas que ofrece el cine que pueden estar disponibles o no.

class Cine:
    cines = list() #la empresa tiene diferentes cines en la misma ciudad
    
    # pensaba meter como atributo la ubicacion y luego meter un metodo con eso...

    def __init__(self, nombre, peliculas):
        self._nombre = nombre
        self._peliculas = peliculas
        self.cines.append(self)
    
    # El metodo agregarPelicula recibe como parametro una pelicula 
    # y lo agrega a la lista de peliculas de la taquilla del determinado cine.
	
    def agregarPelicula(self, pelicula):
        self._peliculas.append(pelicula)
        
    # El metodo quitarComponente recibe como parametro una pelicula
    #  y la quita de la lista de peliculas del cine (sale de la taquilla).
   
    def quitarPelicula(self, pelicula):
        self._peliculas.remove(pelicula)
        
    # getter and setter
        
    def getComponentes(self):
        return self._componentes

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    #toString

    def __str__(self):
        return self._nombre