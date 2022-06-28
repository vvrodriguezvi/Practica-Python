from .view_exception import ViewException

class ServicioPagadoException(ViewException):
    def __init__(self, message="El cine no ha sido verificado, porfavor revise el servicio prestado"):
        super().__init__(message)
