import csv
import numpy as np
from Contrato import Contrato
class ManejaContrato:
    __cantidad=0
    __dimension=0
    __incremento=0
    __arregloContrato=None
    def __init__(self,dimension=0,incremento=5):
        self.__arregloContrato=np.empty(dimension,dtype=Contrato)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarContrato(self,contrato):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.redimensionar()
        self.__arregloContrato[self.__cantidad]=contrato
        self.__cantidad+=1
    def redimensionar(self):
        self.__arregloContrato.resize(self.__dimension)
    def crearArchivo(self):
        nombre='contratos.csv'
        archivo=open(nombre,'w',encoding='utf-8',newline='')
        writer=csv.writer(archivo,delimiter=';')
        writer.writerow(['DNI','Nombre del equipo','Fecha de Inicio','Fecha de fin','Pago mensual'])
        for i in range(self.__cantidad):
            self.__arregloContrato[i].guardarDatos(writer)
        archivo.close()

    
    
    