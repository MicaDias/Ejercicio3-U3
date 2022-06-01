class Contrato:
    __fechaInicio=None
    __fechaFin=None
    __pagoMensual=0.0
    __jugador=None
    __equipo=None
    def __init__(self,fechaInicio=None,fechaFin=None,pagoMensual=0.0,jugador=None,equipo=None):
        from Jugador import Jugador
        from Equipo import Equipo
        self.__fechaInicio=fechaInicio
        self.__fechaFin=fechaFin
        self.__pagoMensual=pagoMensual
        if type(jugador)==Jugador:
            self.__jugador=jugador
        else:
            print('No es un jugador.')
        if type(equipo)==Equipo:
            self.__equipo=equipo
        else:
            print('No es un equipo.')
    def verificarDNI(self,dni):
        resultado=False
        if self.__jugador.verificarDNI(dni):
            resultado=True
        return resultado
    def mostrarEquipoFecha(self):
        self.__equipo.mostrarNombre()
        print('Fecha de finalizacion:',self.__fechaFin.strftime('%d/%m/%Y'))
    def calcularMeses(self):
        meses=0
        cantidadDias=self.__fechaFin-self.__fechaInicio
        meses=round(cantidadDias.days/30.417,2)
        return meses 
    def mostrarContrato(self):
        meses=self.calcularMeses()
        if meses<=6:
            print(self.__jugador)
    def calcularImporte(self):
        importe=0
        meses=self.calcularMeses()
        importe=meses*self.__pagoMensual
        return importe
    def guardarDatos(self,writer):
        writer.writerow([self.__jugador.getDNI(),self.__equipo.getNombre(),self.__fechaInicio.strftime('%d/%m/%Y'),self.__fechaFin.strftime('%d/%m/%Y'),self.__pagoMensual])