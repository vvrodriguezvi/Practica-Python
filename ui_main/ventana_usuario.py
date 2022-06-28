from gestor_aplicacion.personal.empleado import Empleado
from gestor_aplicacion.tienda.cliente import Cliente
from gestor_aplicacion.personal.supervisor import Supervisor
from gestor_aplicacion.personal.taquillero import Taquillero
from gestor_aplicacion.tienda.servicio import Servicio
from gestor_aplicacion.tienda.pelicula import Pelicula
from gestor_aplicacion.tienda.precio_pelicula import PrecioPelicula
from gestor_aplicacion.tienda.archivo import Archivo
from gestor_aplicacion.tienda.cine import Cine
from gestor_aplicacion.tienda.caja_registradora import CajaRegistradora
from ui_main.field_frame import FieldFrame
from ui_main.inicio import Inicio
from base_datos.serializador import Serializador
from ctypes import resize
from tkinter import *
from numpy import diag
from random import choice, random, randint
from .cine_no_veridicado_exception import CineNoVerificadoException
from .servicio_pagado_exception import ServicioPagadoException
from .error_aplicacion import ErrorAplicacion
from .exception_pop_up import ExceptionPopUp
from .cliente_incorrecto_exception import ClientIncorrectoException

# Se enlazan las diferentes funciones de la interfaz

if len(Taquillero.taquilleros) == 0:
    taquillero = Taquillero("Manuel", 1091428126, CajaRegistradora())

if len(Supervisor.supervisores) == 0:
    sup1 = Supervisor("Alejandro", 1264281091)
    sup2 = Supervisor("Camilo", 1091059459)

def outPut(string, text):
    text.delete("1.0", "end")
    text.insert(INSERT, string)
    text.pack(fill=X, expand=True)

def iniciar_ventana_usuario():
    #Ventana principal
    window = Tk()
    window.geometry("680x420")
    window.title("CinemaUnal")
    window.option_add("*tearOff",  FALSE)


    # Métodos sin ningun argumento


    framesAMatar = []

    def matarloTodo(frameUtilizado):

        for frame in framesAMatar:
            frame.pack_forget()
        frameUtilizado.pack(fill=BOTH,expand=True)


    def evtClienteManual():
        matarloTodo(clienteManual)

    # Salida luego de generar un cliente

    outputGenerarCliente = Text(window, height=3)
    framesAMatar.append(outputGenerarCliente)    
    def evtGenerarCliente():
        cliente = generarCliente()
        outPut("Se creo el cliente ID: "+str(Cliente.clientes.index(cliente))+" "+cliente.__str__() ,outputGenerarCliente)
        matarloTodo(outputGenerarCliente)

# ........

    def evtSolicitarServicio():
        matarloTodo(solicitarServicio)
    
    def evtFinalizarServicio():
        matarloTodo(finalizarServicio)
    
    def evtCobrarServicio():
        matarloTodo(cobrarServicio)
    
    def evtDiagnosticarCine():
        matarloTodo(diagnosticarCine)
    
    def evtVerificarCine():
        matarloTodo(verificarCine)

# Salida luego de liquidar
      
    outputLiquidarPeriodo = Text(window, height=6)
    framesAMatar.append(outputLiquidarPeriodo)   
    def evtLiquidarPeriodo():
        taquillero = Taquillero.getTaquilleros()[0]
        stringqueseprintiara = "En la caja registradora hay " + str(round(taquillero.getCajaRegistradora().getTotalIngresos(),2)) + " antes de liquidar.\n"
        for liquidacion in taquillero.liquidar():
            stringqueseprintiara += "\n" + liquidacion

        stringqueseprintiara += "\n\nEn la caja registradora quedan " + str(round(taquillero.getCajaRegistradora().getTotalIngresos(),2))
        
        outPut(stringqueseprintiara, outputLiquidarPeriodo)
        matarloTodo(outputLiquidarPeriodo)
    
# Salida para mostrar la lista de los clientes
    outPutMostrarClientes = Text(window, height=len(Cliente.clientes))
    framesAMatar.append(outPutMostrarClientes)
    #Evento para mostrar clientes
    def evtMostrarClientes():
        stri = ""
        for i in range(len(Cliente.clientes)):
            stri+="ID del cliente: " + str(i) + " " + Cliente.clientes[i].__str__() + "\n"
        if stri == "":
            stri = "Sin clientes. :("
        outPut(stri, outPutMostrarClientes)
        matarloTodo(outPutMostrarClientes)
    
# Salida que muestra los servicios

    outPutMostrarServicios = Text(window, height=len(Servicio.servicios))
    framesAMatar.append(outPutMostrarServicios)
    #Evento para mostrar servicios
    def evtMostrarServicios():
        stri = ""
        for i in range(len(Servicio.servicios)):
            stri+= Servicio.servicios[i].__str__() + "\n"
        if stri == "":
            stri = "No se ha generado algun servicio. :("
        outPut(stri, outPutMostrarServicios)
        matarloTodo(outPutMostrarServicios)

# Pestaña con el nombre de los autores de la aplicacion

    def open_popup():
        top= Toplevel(window)
        top.grid_rowconfigure(0, weight=1)
        top.geometry("450x250")
        top.resizable(False,False)
        top.title("Ayuda")
        Label(top, text= "Autores:\nValentina Vanessa Rodriguez\nCamilo Vasco Agudelo\nFabian Alejandro Vasquez\nValeria Vasquez Hernandez", font=('Times 18 bold')).pack(fill=BOTH, expand=True)

# pestaña con la informacion de la aplicacion

    def aplicacion_popup():
        top= Toplevel(window)
        top.geometry("580x320")
        top.resizable(False,False)
        top.title("Aplicación")
        Label(top, text= textonimo , font=('Times 12')).pack(fill=BOTH, expand=True)
    textonimo = "CinemaUnal es una empresa de cines de la ciudad de Medellin.\nSimula la interaccion del cinema IT,\n que facilita la organizacion de la empresa para de esta manera prestar mejor servicio.\nSe tendrá en cuenta toda la cadena de servicio, desde que llega el\ncliente con el respectivo cine a verificar, su paso por los supervisores,\n para revisar las peliculas que estaran disponibles, hasta finalizar con la\entrega de la boleta y el pago del servicio."

#  barra del menu

    def salir():
        Serializador.serializarTodo()
        from ui_main.ventana_inicio.inicio import VentanaInicio
        framesAMatar = []
        window.destroy()
        ventana = VentanaInicio()
        ventana.mainloop()
        
    def evento():
        pass

    frame_a = Frame()#master = window
    
    frame_a.pack()

 # Menu superior superior
    
    menubar = Menu()

    menuarchivo = Menu(window)
    menuprocesos = Menu(window)
    menuayuda = Menu(window)
    

    menubar.add_cascade(menu = menuarchivo,
                        label='Archivo',
                        command = evento)
    menubar.add_cascade(menu = menuprocesos,
                        label = 'Procesos y Consultas',
                        command = evento)
    menubar.add_cascade(menu = menuayuda,
                        label='Help',
                        command = evento)

# submenu: procesos y consultas

    submenu = Menu(window)
    submenu.add_command(label = "Crear cliente manualmente", command = evtClienteManual)
    submenu.add_command(label = "Generar cliente", command = evtGenerarCliente)
    submenu.add_command(label = "Solicitar servicio", command = evtSolicitarServicio)
    submenu.add_command(label = "Diagnosticar peliculas", command = evtDiagnosticarCine)

    menuarchivo.add_command(label = "Aplicacion", command = aplicacion_popup)
    menuarchivo.add_command(label = "Guardar y salir", command = salir)

    menuprocesos.add_cascade(label = "Menu diagnosticar Cine", menu = submenu)

    menuprocesos.add_command(label = "Verificar peliculas del Cinema", command = evtVerificarCine)
    menuprocesos.add_command(label = "Finalizar un servicio", command = evtFinalizarServicio)
    menuprocesos.add_command(label = "Cobrar un servicio", command = evtCobrarServicio)
    menuprocesos.add_command(label = "Liquidar el periodo", command = evtLiquidarPeriodo)
    menuprocesos.add_command(label = "Mostrar clientes", command = evtMostrarClientes)
    menuprocesos.add_command(label = "Mostrar servicios", command = evtMostrarServicios)

    menuayuda.add_command(label = "info", command = open_popup)

    window['menu'] = menubar


# Manual del cliente 
    window.resizable(True,True)

    clienteManual = Frame(window, bd=10)
    nombre = Label(clienteManual, text="Crear cliente manualmente", bd= 10)

# Interfaz de inicio

    interfazInicio = Inicio(window)

    framesAMatar.append(interfazInicio)

# ojo

    descripcion = Label(clienteManual, text="Diligenciar de forma correcta la informacion para realizar el debido proceso ", bd= 10)

# valor asignado a cada id del cliente

    crearCliente = FieldFrame(clienteManual, "Datos cliente",["ID","Nombre", "Cedula", "Saldo"], "Valor", [len(Cliente.clientes), None, None, None], ["ID"],[1, 0, 1, 1])
    crearCliente.grid_columnconfigure(0, weight=1)
    crearCliente.grid_columnconfigure(1, weight=1)
    crearCliente.grid_rowconfigure(0, weight=1)
    crearCliente.grid_rowconfigure(1, weight=1)
    crearCliente.grid_rowconfigure(2, weight=1)
    crearCliente.grid_rowconfigure(3, weight=1)
    crearCliente.grid_rowconfigure(4, weight=1)
    crearCliente.grid_rowconfigure(5, weight=1)
    
    output = Text(clienteManual, height=3)
    framesAMatar.append(output)

    def creacionCliente():
        try:
            crearCliente.aceptarCheck()
            cine = generarCineAleatorio()
            cines = [cine]
            
            #Creacion del cliente manual, actualizacion de las entries y ID cliente

            if float(crearCliente.getValue("Saldo")) > 500000:
                cliente = Cliente(crearCliente.getValue("Nombre"), crearCliente.getValue("Cedula"), cines, Taquillero.getTaquilleros()[0], float(crearCliente.getValue("Saldo")))
                valores = crearCliente.getValores()
                
                #Actualizar id del cliente en el FieldFrame

                crearCliente.setValores([int(valores[0]) + 1] + [valores[i] for i in range(1, len(valores))])
                
                #Resetear entries del FieldFrame
                
                crearCliente.setEntries(list())
                
                #Refrescar el FieldFrame
                
                crearCliente.actualizacion()
                outPut("Se ha generado manualmente el cliente con ID: " + str(len(Cliente.clientes)-1) + " " + cliente.__str__(), output)

            else: 
                outPut("Se ha ingresado un saldo insuficiente. No se ha generado Cliente", output)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))
        
# Creacion de los botones para aceptar y borrar de creacion manual de cliente

    crearCliente.crearBotones(creacionCliente)   #     Aceptar             Borrar

    nombre.pack()
    #texto.pack()
    interfazInicio.pack()
    descripcion.pack()
    crearCliente.pack(fill=BOTH,expand=True)
    framesAMatar.append(clienteManual)
     
# Frame de Solicitar servicio-----------------------------------------------------
  
    solicitarServicio = Frame(window)
    nombreSolicitarServicio = Label(solicitarServicio, text="Solicitar servicio", bd=10)
    dcrSolicitarServicio = Label(solicitarServicio, text="Ingrese el ID del cliente para solicitar la disponibilidad del cine", bd=10)
    FFsolicitarServicio = FieldFrame(solicitarServicio, None, ["ID cliente"], None, [None], [],[1])
    outputsolicitarServicio = Text(solicitarServicio, height=3)
    framesAMatar.append(outputsolicitarServicio)


    def aceptarSolicitarServicio():
        try:
            FFsolicitarServicio.aceptarCheck()
            outPut(funSolicitarServicio(FFsolicitarServicio.getValue("ID cliente")), outputsolicitarServicio) 
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))

    FFsolicitarServicio.crearBotones(aceptarSolicitarServicio)


    nombreSolicitarServicio.pack()
    dcrSolicitarServicio.pack()
    FFsolicitarServicio.pack()
    framesAMatar.append(solicitarServicio)

# Diagnostica el servicio seleccionado por el administrador.
# Frame de Diagnosticar Cine.

    diagnosticarCine = Frame(window)
    nombreDiagnosticarCine = Label(diagnosticarCine, text="Diagnosticar disponibilidad de un cine", bd=10)
    dcrDiagnosticarCine = Label(diagnosticarCine, text = "Ingrese el ID del servicio a diagnosticar", bd=10)
    FFdiagnosticarCine = FieldFrame(diagnosticarCine, None, ["ID Servicio"], None, [None], [],[1])
    outputDiagnosticarCine = Text(diagnosticarCine, height=7)
    framesAMatar.append(outputDiagnosticarCine)

    def aceptarDiagnosticarCine():
        try:
            FFdiagnosticarCine.aceptarCheck()
        
            outPut(diagnosticarUnCine(), outputDiagnosticarCine)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))

    FFdiagnosticarCine.crearBotones(aceptarDiagnosticarCine)


    nombreDiagnosticarCine.pack()
    dcrDiagnosticarCine.pack()
    FFdiagnosticarCine.pack()
    framesAMatar.append(diagnosticarCine)
  


# Frame de verificar un cine
    verificarCine = Frame(window)
    nombreVerificarCine = Label(verificarCine, text="Verificar un Cine", bd=10)
    dcrVerificarCine = Label(verificarCine, text="Ingrese el ID del servicio a verificar", bd=10)
    FFverificarCine = FieldFrame(verificarCine, None, ["ID Servicio"], None, [None], [],[1])
    outputVerificarCine = Text(verificarCine, height=3)
    framesAMatar.append(outputVerificarCine)

    def aceptarVerificarCine():
        try:
            FFverificarCine.aceptarCheck()
            outPut(verificar(), outputVerificarCine)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))

    FFverificarCine.crearBotones(aceptarVerificarCine)


    nombreVerificarCine.pack()
    dcrVerificarCine.pack()
    FFverificarCine.pack()
    framesAMatar.append(verificarCine)


# Frame de Finalizar un servicio
  
    finalizarServicio = Frame(window)
    nombreFinalizarServicio = Label(finalizarServicio, text="Finalizar un servicio", bd=10)
    dcrFinalizarServicio = Label(finalizarServicio, text="Ingrese el ID del servicio a finalizar", bd=10)
    FFfinalizarServicio = FieldFrame(finalizarServicio, None, ["ID Servicio"], None, [None], [],[1])
    outputFinalizarServicio = Text(finalizarServicio, height=6)
    framesAMatar.append(outputFinalizarServicio)


    def aceptarFinalizarServicio():
        try:
            FFfinalizarServicio.aceptarCheck()
            outPut(finalizar(), outputFinalizarServicio)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))


    FFfinalizarServicio.crearBotones(aceptarFinalizarServicio)


    nombreFinalizarServicio.pack()
    dcrFinalizarServicio.pack()
    FFfinalizarServicio.pack()
    framesAMatar.append(finalizarServicio)


# Frame de Cobrar un servicio

    cobrarServicio = Frame(window)
    nombreCobrarServicio = Label(cobrarServicio, text="Cobrar un servicio", bd=10)
    dcrCobrarServicio = Label(cobrarServicio, text="Ingrese el ID del servicio a cobrar", bd=10)
    FFcobrarServicio = FieldFrame(cobrarServicio, None, ["ID Servicio"], None, [None], [],[1])
    outputCobrarServicio = Text(cobrarServicio, height=3)
    framesAMatar.append(outputCobrarServicio)


    def aceptarCobrarServicio():
        try:
            FFcobrarServicio.aceptarCheck()
            #FUNCIONALIDAD DE COBRAR SERVICIO
            outPut(cobrar(), outputCobrarServicio)
        except ErrorAplicacion as e:
            ExceptionPopUp(str(e))


    FFcobrarServicio.crearBotones(aceptarCobrarServicio)


    nombreCobrarServicio.pack()
    dcrCobrarServicio.pack()
    FFcobrarServicio.pack()
    framesAMatar.append(cobrarServicio)
 
# FUNCIONALIDADES

    def generarCineAleatorio():
        rand = random()
        nombreCines = [ "C.C Aventura", "C.C Oviedo", "C.C Jardin", "Exito colombia", "C.C Ventura Plaza",
                    "C.C San Diego", "C.C Mayorca", "Exito Bello", "C.C River Plaza", "C.C America" ]
        peliculas = [ Pelicula("Los Vengadores", True),
                        Pelicula("Los Vengadores 2", True),
                        Pelicula("Los Vengadores 3", True),
                        Pelicula("Los Increibles ", True),
                        Pelicula("Los Increibles 2", True),
                        Pelicula("Encanto", True),
                        Pelicula("Moana", True),
                        Pelicula("El conjuto 1", True),
                        Pelicula("El conjuro 2", True),
                        Pelicula("El conjuro 3", True)]
        
        cinePeliculas = list()
        cinePeliculas.append(choice(peliculas))
        cinePeliculas.append(choice(peliculas))

        return Cine(choice(nombreCines), cinePeliculas)
        

    def generarCliente():
        nombres = ["Andres", "Camil", "Fabian", "Alberto", "Manuela", "Alejandra", "Nayibe", "Noralba", "Junmyeon", "Jongin", "Jongdae", "Chanyeol"]
        peliculas = [Pelicula("Los Vengadores", False, PrecioPelicula.D2.value),
        Pelicula("El conjuro 3", False, PrecioPelicula.D5.value),
        Pelicula("El conjuro 2", False, PrecioPelicula.D2.value),
        Pelicula("El conjuro 1", False, PrecioPelicula.D3.value),
        Pelicula("Encanto", False, PrecioPelicula.D2.value),
        Pelicula("Moana", False, PrecioPelicula.D4.value),
        Pelicula("Los Increibles 2", False, PrecioPelicula.D2.value),
        Pelicula("Los Increibles ", False, PrecioPelicula.D2.value),
        Pelicula("Los Vengadores 3", False, PrecioPelicula.D3.value),
        Pelicula("Los Vengadores 2", False, PrecioPelicula.D3.value)]

        supervisor = Taquillero.taquilleros[0]
        cine = generarCineAleatorio()
        cines = [cine]
        saldo = int(450000+1000000*random())
        cliente = Cliente(choice(nombres), randint(100000000, 9999999999), cines, supervisor, saldo)

        valores = crearCliente.getValores()
        #Actualizar id del cliente en el FieldFrame
        crearCliente.setValores([int(valores[0]) + 1] + [valores[i] for i in range(1, len(valores))])
        #Resetear entries del FieldFrame
        crearCliente.setEntries(list())
        #Refrescar el FieldFrame
        crearCliente.actualizacion()

        for pelicula in peliculas:
            Archivo.agregarPelicula(pelicula)
        return cliente

    def funSolicitarServicio(index):
        try:
            cliente = Cliente.getClientes()[int(index)]
        except:
            raise ClientIncorrectoException("El id del cliente no es correcto")
        if len(cliente.getRecibos()) == 0:
            cine = cliente.getCines()[0]
            cliente.solicitarReserva(cine)
            return "El cliente fue atendido exitosamente por " + cliente.getTaquillero().getNombre() + " y se ha generado el servicio en: " + cine.__str__() + ".\nYa puede consultar en los servicios para iniciar su diagnostico."
        else:
            return "El cliente " + cliente.getNombre() + " ya ha sido atendido\n"

    def diagnosticarUnCine():
        try:
            servicio = Servicio.getServicios()[int(FFdiagnosticarCine.getValue("ID Servicio"))] 
        except:
            raise ClientIncorrectoException("El id de servicio incorrecto")
        if not servicio.isReservado():
            servicio.getSupervisor().diagnosticar(servicio)
            
# Devuelve el diagnostico hecho por el Supervisor.

            stringDiagnostico = servicio.getDiagnostico()
            stringDiagnostico += "\nYa puede volver al menu principal para solicitar la verificacion de la reserva\n"
        else:
            stringDiagnostico = "Este cine ya ha sido verificado\n"
        return stringDiagnostico

    def verificar():
        try:
            servicio = Servicio.getServicios()[int(FFverificarCine.getValue("ID Servicio"))]
        except:
            raise ClientIncorrectoException("El id del servicio no es correcto")

        if not servicio.isReservado():
            if servicio.getDiagnostico != None:
                servicio.getSupervisor().verificar(servicio)
                return "El servicio de " + servicio.getCliente().getNombre() + " fue solucionado por "+ servicio.getSupervisor().__str__() + " y tuvo un costo para la empresa de " + str(servicio.getCosto())
            else:
                return "No se ha diagnosticado el cine que escogio el cliente "+ servicio.getCliente().__str__()
        else: 
            return "Ya se ha verificado el cine (cartelera)!"

    def finalizar():
        try: 
            index = FFfinalizarServicio.getValue("ID Servicio")
            servicio = Servicio.getServicios()[int(index)]
        except:
            raise ClientIncorrectoException("El id del servicio no es correcto")

        if servicio.isReservado():
            taquillero = servicio.getTaquillero()
            taquillero.finalizarServicio(servicio)
            return servicio.getCliente().getRecibos()[0] + "\nEl servicio ya esta listo para ser cobrado."
        else:
            raise CineNoVerificadoException("El servicio no ha sido verificado aun y no se puede finalizar.")

    def cobrar():
        try:
            servicio = Servicio.getServicios()[int(FFcobrarServicio.getValue("ID Servicio"))]
            taquillero = Supervisor.getTaquilleros()[0]
        except:
            raise ClientIncorrectoException("El id del servicio no es correcto")

        if not servicio.isPagado():
            if servicio.isReservado():
                taquillero.cobrarServicio(servicio)
                nott = "Se cobra el servicio por un total de "+ str(servicio.getCosto() * Taquillero.getMargenGanancia())
                nott += "\nEn la caja registradora ahora hay "+ str(taquillero.getCajaRegistradora().getTotalIngresos()) + " pesos."
                return nott
            else:
                raise CineNoVerificadoException("Aun no se ha verificado el cine.")
        else:
            raise ServicioPagadoException("Ya se ha cobrado el servicio! Se lamenta la molestia.")
    #------------------------------------------------------------------------------------------------------
    window.mainloop()




