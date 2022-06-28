from operator import length_hint
from tkinter import *
from unicodedata import numeric

from numpy import empty
from .empty_exception import EmptyException
from .numeric_exception import NumericException
from .length_exception import LengthException
from .empty_exception import EmptyException


class FieldFrame(Frame):
    def __init__(self, master, tituloCriterios, criterios, tituloValores, valores, habilitado, tipos):
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado
        self._entries = list()
        self._tipos = tipos
        super().__init__(master)
        self.actualizacion()

#crear el fielframe y actualiza los datos

    def actualizacion(self):
        Label(self, text=self._tituloCriterios).grid(padx = 80, column = 0, row = 0)
        Label(self, text=self._tituloValores).grid(padx = 80, column = 1, row = 0)
        for i in range(1, len(self._valores)+1):
            Label(self, text=self._criterios[i-1]).grid(padx = 80, pady=2, column=0, row=i)
            if self._criterios[i-1] in self._habilitado:
                texto = StringVar(value=self._valores[i-1])
                entrada = Entry(self, width = 40, textvariable=texto, state=DISABLED, justify="center")
            else:
                texto = StringVar(value=self._valores[i-1])
                entrada = Entry(self, width = 40, textvariable=texto, justify="center")
        
            entrada.grid(pady =2, column=1, row=i)
            self._entries.append(entrada)

        
# el boton aceptar        

    def aceptarCheck(self):
        criteriosFaltantes = []
        datosErroneos = []
        faltan = False
        erroneos = False
        for i in range(len(self._entries)): 
            self._valores[i] = self._entries[i].get()
            if self._valores[i] == "":
                faltan = True
                criteriosFaltantes.append(self._criterios[i])

        if faltan:
            faltantes = ", ".join(criteriosFaltantes)
            raise EmptyException("Campos faltantes: " + faltantes)
        
        for i in range(len(self._entries)):
            if self._tipos[i] == 0:
                if self._valores[i].isdigit():
                    erroneos = True
                    datosErroneos.append(self._criterios[i])
                elif len(self._valores[i]) < 3: 
                    raise LengthException(self._criterios[i] + " tamaño insuficiente")
            elif self._tipos[i] == 1:
                if not self._valores[i].isdigit():
                    erroneos = True
                    datosErroneos.append(self._criterios[i])
        if erroneos:
            errores = ", ".join(datosErroneos)
            raise NumericException("Ingreso erroneo " + errores)


    
# borrar
    
    def borrarEntry(self):
        for entrada in self._entries:
            entrada.delete(0, "end")
        
    def getValue(self, criterio):
        criterios_dict = dict(zip(self._criterios, self._valores))
        return criterios_dict[criterio]
    
    def getCriterios(self): 
        return self._criterios
        
    def getValores(self):
        return self._valores

    def setValores(self, valores):
        self._valores = valores
    
    def setEntries(self, entries):
        self._entries = entries

# botones
    
    def crearBotones(self, comando1):
        aceptar = Button(self, text="Aceptar",command=comando1).grid(pady = 50, column = 0, row = len(self._criterios)+1)
        borrar = Button(self, text="Borrar",command=self.borrarEntry).grid(pady = 50, column = 1, row = len(self._criterios)+1)
