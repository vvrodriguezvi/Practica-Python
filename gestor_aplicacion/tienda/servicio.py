# from ..tienda.cliente import Cliente
# from ..tienda.cine import Cine
# from ..personal.taquillero import Taquillero
# from ..personal.supervisor import Supervisor
from queue import Empty

# Servicio contiene toda la informacion que relaciona a un cliente y la resrva en determinado cine 
# con los empleados (el taquillero que le atendio y el supervisor encargado de la revisón de su reserva) 
# en el sistema (verifica su reserva para ver la pelicula disponible). 


class Servicio:
    servicios = list()
    def __init__(self, _supervisor, _cine, _cliente, _taquillero):
        self._supervisor = _supervisor
        self._cine = _cine
        self._cliente = _cliente
        self._taquillero = _taquillero
        self._reservado = False # reparado antes
        self._costo = 0
        self._diagnostico = None # la consulta de si se puede reservar
        self._pagado = False
        if self.servicios is Empty:
            self.identificador = 0
        else:
            self.identificador = len(self.servicios)
        self.servicios.append(self)

    # getter y setter     

    def setPagado(self, _pagado):
        self._pagado = _pagado

    def getCine(self):
        return self._cine

    def getTaquillero(self):
        return self._taquillero

    def anadirCosto(self, precio):
        self.costo+=precio

    def getCosto(self):
        return self._costo

    def getDiagnostico(self):
        return self._diagnostico

    def isPagado(self):
        return self._pagado

    def setCosto(self, costo):
        self._costo=costo

    def getIdentificador(self):
        return self.identificador

    def getCliente(self):
        return self._cliente

    def setCliente(self, cliente):
        self._cliente = cliente

    def setDiagnostico(self, diagnostico):
        self._diagnostico = diagnostico

    def getSupervisor(self):
        return self._supervisor

    def isReservado(self):
        return self._reservado

    def setReservado(self, reservado):
        self._reservado = reservado
        
    # metodos de clase
        
    @classmethod
    def getServicios(cls):
        return cls.servicios

    @classmethod
    def setServicios(cls, servicios):
        cls.servicios = servicios

    def __str__(self):
        return "Identificador del servicio: " + str(self.identificador) + "\nCliente: " + str(self._cliente) + "\nCine escogido: " + str(self._cine)+ "\nReservado: " + str(self._reservado) + "\nPagado: " + str(self._pagado) + "\n"