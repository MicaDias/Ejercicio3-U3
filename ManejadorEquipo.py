import csv
import numpy as np
from Equipo import Equipo
class ManejadorEquipo:
    __cantidad=0
    __dimension=0
    __incremento=0
    __arregloEquipos=None
    def __init__(self,dimension=0,incremento=5):
        self.__arregloEquipos=np.empty(dimension,dtype=Equipo)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarEquipo(self,equipo):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.redimensionar()
        self.__arregloEquipos[self.__cantidad]=equipo
        self.__cantidad+=1
    def redimensionar(self):
        self.__arregloEquipos.resize(self.__dimension)
    def cargarArchivo(self):
        archivo=open('Equipos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                try:
                    self.__dimension=int(fila[0])
                except ValueError:
                    print('La primera linea del archivo debe ser un entero.')
                else:
                    self.redimensionar()
                bandera=not bandera
            else:
                self.agregarEquipo(Equipo(fila[0],fila[1],self.__cantidad+1))
    def mostrarDatos(self):
        for i in range(self.__cantidad):
            print(self.__arregloEquipos[i])
    def buscarIdentificador(self,iden):
        i=0
        bandera=True
        resultado=-1

        while i<self.__cantidad and bandera:
            if self.__arregloEquipos[i].verificarIden(iden):
                bandera= not bandera
            else:
                i+=1
        if not bandera:
            resultado=i
        return resultado
    def buscarEquipo(self,identificador):
        resultado=-1
        pos=self.buscarIdentificador(identificador)
        if pos!=-1:
            resultado=self.__arregloEquipos[pos]
        return resultado
    def verificarContrato(self,dni,iden):
        bandera=False
        pos=self.buscarIdentificador(iden)
        if pos!=-1:
           resultado=self.__arregloEquipos[pos].buscarContrato(dni)
           if resultado!=-1:
               bandera=True
        return bandera
    def mostrarJugadores(self,iden):
        pos=self.buscarIdentificador(iden)
        if pos!=-1:
            self.__arregloEquipos[pos].mostrarDatosJugadores()
        else:
            print('No se encontro el equipo.')
    def buscarNombre(self,nombre):
        i=0
        bandera=True
        resultado=-1
        while i<self.__cantidad and bandera:
            if self.__arregloEquipos[i].getNombre()==nombre:
                bandera= not bandera
            else:
                i+=1
        if not bandera:
            resultado=i
        return resultado
    def verificarImporteTotal(self,nombre):
        pos=self.buscarNombre(nombre)
        if pos!=-1:
            self.__arregloEquipos[pos].verificarImporte()
        else:
            print('No se encontro el nombre del equipo.')