import random
from ..personal.empleado import Empleado
from ..tienda.servicio import Servicio
from ..personal.supervisor import Supervisor

class Taquillero(Empleado):
    taquilleros = []
    _MARGEN_GANANCIA = 1.5

    def __init__(self, nombre, cedula, caja, servicios = None):
        if servicios == None:
            super().__init__(nombre,cedula)
            self._cajaRegistradora = caja
            Taquillero.taquilleros.append(self)
        else:
            super().__init__(nombre,cedula)
            self._cajaRegistradora = caja
            Empleado.servicios = servicios
            Taquillero.taquilleros.append(self)


    def getCajaRegistradora(self):
        return self._cajaRegistradora
    
    def setCajaRegistradora(self, caja):
        self._cajaRegistradora = caja
    
    def __str__(self):
        return "Taquillero: " + super().getNombre()
    
    @classmethod
    def getTaquilleros(cls):
        return cls.taquilleros
    
    @classmethod
    def setTaquilleros(cls, taquilleros):
        cls.taquilleros = taquilleros
    
    @classmethod
    def getMargenGanancia(cls):
        return cls._MARGEN_GANANCIA

    def quitarServicio(self, servicio):
        self.getServicios().remove(servicio)

    def asignarServicio(self, servicio):
        self.getServicios().append(servicio)

    def entregarBoleta(self, servicio):
        servicio.getCliente().recibirBoleta(servicio.getCine())

    def finalizarServicio(self,servicio):
        self.notificarCliente(servicio)
        self.entregarBoleta(servicio) ##oji
   
    def generarServicio(self, supervisor, cine, cliente):
        servicio = Servicio(supervisor, cine, cliente, self)
        supervisor.asignarServicio(servicio)
        self.asignarServicio(servicio)

    def atenderCliente(self, cliente, cine):
        if len(cliente.getRecibos()) == 0:
            rand = random.randint(0, len(Supervisor.supervisores)-1)
            supervisor = Supervisor.supervisores[rand]
            self.generarServicio(supervisor, cine, cliente)
    
    def registrarPago(self, servicio):
        self._cajaRegistradora.registrarVenta(servicio.getCosto() * Taquillero._MARGEN_GANANCIA, servicio)
        self.quitarServicio(servicio)
    
    def notificarCliente(self, servicio):
        cliente = servicio.getCliente()
        recibo = """Factura # {} \nCliente: {} con cedula {} \nCostoTotal: {} \nRecibir la boleta: {}""".format(str(servicio.getIdentificador()), str(cliente.getNombre()), str(cliente.getCedula()), str(servicio.getCosto() * Taquillero._MARGEN_GANANCIA), servicio.getCine().getNombre())
        cliente.recibirRecibo(recibo)
    
    
    def cobrarServicio(self, servicio):
        cobro = servicio.getCosto() * Taquillero._MARGEN_GANANCIA
        servicio.getCliente().pagarServicio(servicio, cobro)
        if not servicio.isPagado():
            self._cajaRegistradora.registrarVenta(cobro, servicio)
            servicio.setPagado(True)
    
    def cobrarSalario(self, caja):
        porcentaje = 0.05
        self._cartera += caja.descontar(porcentaje)
    
    def liquidar(self):
        caja = self._cajaRegistradora

        liquidaciones = []
        contador = 0

        for empleado in Empleado.getEmpleados():
            carterainicial = empleado.getCartera()
            empleado.cobrarSalario(caja)
            carteraAhora = empleado.getCartera()
            liquidado = carteraAhora - carterainicial

            contador += liquidado
            liquidaciones.append("El {} ha recibido {} por su trabajo.".format(empleado.__str__(), str(round(liquidado))))
        
        caja.setTotalIngresos(caja.getTotalIngresos() - contador)
        return liquidaciones



