from .view_exception import ViewException

class ClientIncorrectoException(ViewException):
    def __init__(self, message="el id ingresado no corresponde a un cliente de la aplicacion, intente con otro nuevamente."):
        super().__init__(message)
