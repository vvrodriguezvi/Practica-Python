# La enumeracion Precio de la pelicula asocia al fomato 
# de las peliculas con su precio unico y constante

from enum import Enum
class PrecioComponente(Enum):
    #tipo de formato
    D2 = 9000
    D3 = 18000
    D4 = 35000
    D5 = 65000
