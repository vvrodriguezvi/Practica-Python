import pickle
from gestor_aplicacion.personal.empleado import Empleado
from gestor_aplicacion.tienda.cliente import Cliente
from gestor_aplicacion.personal.supervisor import Supervisor
from gestor_aplicacion.personal.taquillero import Taquillero
from gestor_aplicacion.tienda.servicio import Servicio
from gestor_aplicacion.tienda.pelicula import Pelicula
from gestor_aplicacion.tienda.archivo import Archivo
from gestor_aplicacion.tienda.cine import Cine
from gestor_aplicacion.tienda.caja_registradora import CajaRegistradora
import pathlib
import os


class Serializador():
    
    def serializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        try:
            # Creo el archivo pickle para guardar los objetos
            picklefile = open(camino(className), 'wb')
            # pickle el objeto en el archivo
            pickle.dump(lista, picklefile)
            # cierro el archivo para guardar
            picklefile.close()
            
        except:
            print("Esta mal. Ojo")

    def serializarTodo():

        Serializador.serializar(Taquillero.getTaquilleros(), "Taquilleros")
        Serializador.serializar(Supervisor.supervisores, "Supervisores")
        Serializador.serializar(CajaRegistradora.cajasRegistradoras, "CajasRegistradoras")
        Serializador.serializar(Cliente.getClientes(), "Clientes")
        Serializador.serializar(Pelicula.peliculas, "Peliculas")
        Serializador.serializar(Cine.cines, "Cines")
        Serializador.serializar(Servicio.getServicios(), "Servicios")
        Serializador.serializar(Archivo.getPeliculas(), "Archivo_de_almacen_de_peliculas_del_cine")
        Serializador.serializar(Empleado.getEmpleados(), "Empleados")

