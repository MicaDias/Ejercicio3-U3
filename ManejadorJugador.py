from Jugador import Jugador
class ManejaJugador:
    __listaJugador=[]
    
    def __init__(self):
        self.__listaJugador=[]
    def agregarJugador(self,jugador):
        if type(jugador)==Jugador:
            self.__listaJugador.append(jugador)
        else:
            print("No se pudo agregar.")
    def buscarDni(self,dni):
        i=0
        bandera=True
        resultado=-1
        longitud=len(self.__listaJugador)
        while i<longitud and bandera:
            if self.__listaJugador[i].verificarDNI(dni):
                bandera= not bandera
            else:
                i+=1
        if not bandera:
            resultado=i
        return resultado
    def buscarJugador(self,dni):
        resultado=-1
        pos=self.buscarDni(dni)
        if pos!=-1:
            resultado=self.__listaJugador[pos]
        return resultado
    def verificarContrato(self,dni):
        pos=self.buscarDni(dni)
        if pos!=-1:
           self.__listaJugador[pos].buscarContrato()
        else:
            print('No se encontro el jugador.')
           
        