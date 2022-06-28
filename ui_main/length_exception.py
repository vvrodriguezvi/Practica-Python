from .field_exception import FieldException


class LengthException(FieldException):
    def __init__(self, message="La longitud de la cadena es insuficiente"):
        super().__init__(message)
