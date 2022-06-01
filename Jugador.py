from Contrato import Contrato
class Jugador:
    __nombre=''
    __dni=''
    __ciudadNatal=''
    __paisOrigen=''
    __fechaNacimiento=None
    __contrato=None
    def __init__(self,nombre='',dni='',ciudadNatal='',paisOrigen='',fechaNacimiento=None):
        self.__nombre=nombre
        self.__dni=dni
        self.__ciudadNatal=ciudadNatal
        self.__paisOrigen=paisOrigen
        self.__fechaNacimiento=fechaNacimiento
        self.__contrato=[]
    def verificarDNI(self,dni):
        bandera=False
        if self.__dni==dni:
            bandera=True
        return bandera
    def getDNI(self):
        return self.__dni
    def agregarContrato(self,contrato):
        if type(contrato)==Contrato:
            self.__contrato.append(contrato)
        else:
            print('No se pudo agregrar.')
    def buscarContrato(self):
        for i in range(len(self.__contrato)):
            self.__contrato[i].mostrarEquipoFecha()
    def __str__(self):
        return'Nombre:{}'.format(self.__nombre)           


        

