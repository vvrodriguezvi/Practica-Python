from .error_aplicacion import ErrorAplicacion


class FieldException(ErrorAplicacion):
    def __init__(self, message):
        super().__init__(extra_message=message)

