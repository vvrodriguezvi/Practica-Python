# La caja registradora es donde se lleva la contabilidad de los difentes cines de la empresa..

class CajaRegistradora:
    cajasRegistradoras = []

    def __init__(self):
        self._servicios = []
        self._totalIngresos = 0
        CajaRegistradora.cajasRegistradoras.append(self)

    def registrarVenta(self, precio, servicio):
        self._servicios.append(servicio)
        self._totalIngresos += precio

    def getTotalIngresos(self):
        return self._totalIngresos

    def setTotalIngresos(self, totalIngresos):
        self._totalIngresos = totalIngresos

    def descontar(self, porcentaje):
        return self._totalIngresos * porcentaje
