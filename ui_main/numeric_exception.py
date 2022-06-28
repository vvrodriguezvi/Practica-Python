from .field_exception import  FieldException

class NumericException(FieldException):
    def __init__(self, message="Los datos deben ser de tipo numerico"):
        super().__init__(message)
