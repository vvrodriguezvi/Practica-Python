#Mensajes de errores en la aplicacion, mostrar execpciones

from .error_aplicacion import ErrorAplicacion

class ViewException(ErrorAplicacion):
    def __init__(self, message):
        super().__init__(extra_message=message)
