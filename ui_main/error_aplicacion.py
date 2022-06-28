class ErrorAplicacion(Exception):
    def __init__(self, extra_message="", message="Errores que presenta la aplicación: "):
        c_type = type(self)
        self.message = message + " " + extra_message
        super().__init__(self.message)
