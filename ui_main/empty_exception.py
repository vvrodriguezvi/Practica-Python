from .field_exception import FieldException


class EmptyException(FieldException):
    def __init__(self, message="No ha ingresado información"):
        super().__init__(message)
