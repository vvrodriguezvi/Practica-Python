from ..personal.empleado import Empleado
from ..tienda.servicio import Servicio
from ..tienda.archivo import Archivo

# Esta clase busca representar el comportamiento de un empleado tipo Supervisor
# Funcionalidades: servicios es una lista de servicios que se va modificando a 
# medida que el supervisor toma o finaliza sus servicios

class Supervisor(Empleado):
    supervisores = list()
    def __init__(self, nombre, cedula, servicios = None):
            super().__init__(nombre, cedula)
            self.supervisores.append(self)
            
    # El metodo verificarPelicula es un metodo auxiliar de la clase, el cual recibe un 
    # servicio y devuelve una lista con las peliculas disponibles en el cine
    # correspondiente a ese servicio.
    
    def verificarPelicula(self, servicio):
        cine = servicio.getCine()
        disponibles = list()
        for pelicula in cine.getPeliculas():
            if pelicula.isDisponible():
                disponibles.append(pelicula)
        return disponibles
    
    # El metodo buscarPelicula es un metodo auxiliar de la clase, el cual recibe 
    # una pelicula y devuelve booleano dependiendo de si esa pelicula
    # con el mismo nombre se encuentra en Archivo o no.
    
    def deletePelicula(self, pelicula): 
        #elimina la pelicula del archivo de todas las peliculas(sale del eire)
        return Archivo.sacarPelicula(pelicula.getNombre())
    
    # El metodo diagnosticar recibe como paremetro un servicio y modifica en este su 
    # atributo diagostico, brindando informacion 
    # sobre los disponibilidad de la peliculas del cine correspondiente.
    
    def diagnosticar(self, servicio):
        servicio.setDiagnostico("Se encontraron disponibles las siguientes peliculas en el cine: "+ str([pelicula.__str__() for pelicula in self.verificarPelicula(servicio)]))
        
    # El metodo verificar recibe como parametro un servicio. Luego, revisa si las peliculas borradas estan 
    # disponibles en el archivo y, a aquellos que estan disponibles, los remueve de la lista de archivo
    # y los reemplaza en la lista de peliculas del cine. Tambien, va sumando
    # el precio de las boletas vendidas en el atributo costo de servicio. (las boletas que vendió esa movie)
    
    def verificar(self, servicio):
        cine = servicio.getCine()
        disponibles = self.verificarPelicula(servicio)
        for pelicula in disponibles:
            remplazo = self.deletePelicula(pelicula)
            if remplazo != None:
                peliculaCine = Archivo.sacarPelicula(remplazo)
                cine.quitarPelicula(pelicula)
                cine.agregarPelicula(peliculaCine)
                servicio.setCosto(servicio.getCosto()+peliculaCine.getPrecio())
        servicio.setReservado(True)
        self.quitarServicio(servicio)
            
    # El metodo asignarServicio recibe como parametro un servicio y lo agrega a la lista de servicios
    # del supervisor
    
    def asignarServicio(self, servicio):
        self.getServicios().append(servicio)
        
    # El metodo quitarServicio recibe como parametro un servicio y lo remueve 
    # de la lista de servicios del supervisor
        
    def quitarServicio(self, servicio):
        self.getServicios().remove(servicio)
        
    # cobrarSalario utiliza el porcentaje que se le debe pagar a los supervisores para calcular 
    # cuanto cobrar por su trabajo y descontar de la caja registradora.
    
    def cobrarSalario(self, cajaRegistradora):
        porcentaje = 0.015
        self._cartera += cajaRegistradora.descontar(porcentaje)
        
    def __str__(self):
        return "Supervisor: " + self.getNombre()    