from Contrato import Contrato
class Equipo:
    __nombre=''
    __ciudad=''
    __identificador=0
    __contrato=None
    def __init__(self,nombre='',ciudad='',identificador=0):
        self.__nombre=nombre
        self.__ciudad=ciudad
        self.__identificador=identificador
        self.__contrato=[]
    def __str__(self):
        return '{},{}'.format(self.__identificador,self.__nombre)
    def verificarIden(self,iden):
        bandera=False
        if self.__identificador==iden:
            bandera=True
        return bandera
    def buscarContrato(self,dni):
        i=0
        resultado=-1
        bandera=True
        longitud=len(self.__contrato)
        while i<longitud and bandera:
            if self.__contrato[i].verificarDNI(dni):
                bandera=not bandera
            else:
                i+=1
        if not bandera:
            resultado=i
        return resultado
    def agregarContrato(self,contrato):
        if type(contrato)==Contrato:
            self.__contrato.append(contrato)
        else:
            print('No se puede agregar el contrato')
    def mostrarNombre(self):
        print('nombre:',self.__nombre)
    def mostrarDatosJugadores(self):
        for i in range(len(self.__contrato)):
            self.__contrato[i].mostrarContrato()
    def getNombre(self):
        return self.__nombre
    def verificarImporte(self):
        acum=0
        for i in range(len(self.__contrato)):
            acum+=self.__contrato[i].calcularImporte()
        print('El total del equipo {} es {}'.format(self.__nombre,acum))
        
    
        


