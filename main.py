from base_datos.deserializador import Deserializador
from ui_main.ventana_inicio.inicio import VentanaInicio

if __name__ == "__main__":
    Deserializador.deserializarTodo()
    ventana = VentanaInicio()
    ventana.mainloop()


