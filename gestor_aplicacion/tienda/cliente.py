# El cliente tiene tres funcionalidades. solicitar una reserv para ver una pelicula,
# pagar el servicio que se le presto (reserva) y recibir su boleta.

class Cliente():
    clientes = []

    def __init__(
            self,
            nombre,
            cedula,
            cines,
            taquillero,
            saldo,
            direccion=None # (dirección de envio si desea dolmicilio)
    ):
        if direccion is not None:
            self._direccion = direccion
        self._nombre = nombre
        self._cedula = cedula
        self._cines = cines
        self._taquillero = taquillero
        self._saldo = saldo
        self._recibos = []
        Cliente.clientes.append(self)

    #def solicitarReparacion(self, producto):
     #   self._dependiente.atenderCliente(self, producto)
      #  self._productos.append(producto)
    
    def solicitarReserva(self, cine):
        self._taquillero.atenderCliente(self, cine)
        self._cines.append(cine) #reserva en determinado cine ? revisar esto...



    def pagarServicio(self, servicio, cobro):
        if(not servicio.isPagado() and self._cartera >= cobro):
            self._saldo -= cobro

    def recibirBoleta(self, cine):
        self._cines.append(cine)


    #getter y setter

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getCedula(self):
        return self._cedula

    def getCines(self):
        return self._cines

    def setCines(self, cines):
        self._cines = cines

    def getTaquillero(self):
        return self._taquillero

    def setTaquillero(self, taquillero):
        self._taquillero = taquillero

    def recibirRecibo(self, recibo):
        self._recibos.append(recibo)

    def getRecibos(self):
        return self._recibos

    def getSaldo(self):
        return self._saldo

    #metodos de clase

    @classmethod
    def getClientes(cls):
        return cls.clientes

    @classmethod
    def setClientes(cls, clientes):
        cls.clientes = clientes

    #toString    

    def __str__(self):
        return "Nombre: " + str(self._nombre) + " CC: " + str(self._cedula) + " Saldo: " + str(self._saldo)# + " Direccion: " + str(self._direccion)
