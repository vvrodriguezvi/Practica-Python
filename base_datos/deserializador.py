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


class Deserializador():
    
    def deserializar(lista, className):
        def camino(className):
            string = os.path.join(pathlib.Path(__file__).parent.absolute(), "temp\\"+className+".txt")
            return string
        # Leo el archivo
        try:
            picklefile = open(camino(className), 'rb')
        except:
            picklefile = open(camino(className), 'x')
            picklefile = open(camino(className), 'rb')
        # unpickle los datos
        if os.path.getsize(camino(className)) > 0:
            lista = pickle.load(picklefile)
        
        # Cierro el archivo
        picklefile.close()
        return lista
        # Cierro el archivo
    
    def deserializarTodo():
        Taquillero.taquilleros = Deserializador.deserializar(Taquillero.taquilleros, "Taquilleros")
        Supervisor.supervisores =  Deserializador.deserializar(Supervisor.supervisores, "Supervisores")
        CajaRegistradora.cajasRegistradoras = Deserializador.deserializar(CajaRegistradora.cajasRegistradoras, "CajasRegistradoras")
        Cliente.clientes = Deserializador.deserializar(Cliente.clientes, "Clientes")
        Pelicula.peliculas = Deserializador.deserializar(Pelicula.peliculas, "Peliculas")
        Cine.cines = Deserializador.deserializar(Cine.cines, "Cines")
        Servicio.servicios = Deserializador.deserializar(Servicio.servicios, "Servicios")
        Archivo._peliculas = Deserializador.deserializar(Archivo._peliculas, "Archivo_de_almacen_de_peliculas_del_cine")
        Empleado._empleados = Deserializador.deserializar(Empleado._empleados, "Empleados")
        
    