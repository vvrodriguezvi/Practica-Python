from .view_exception import ViewException

class CineNoVerificadoException(ViewException):
    def __init__(self, message="El cine no ha verificado si la pelicula esta disponible en el archivo , por favor revise el servicio prestado"):
        super().__init__(message)
