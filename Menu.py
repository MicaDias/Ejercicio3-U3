from datetime import date
from Jugador import Jugador
from Contrato import Contrato
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.salir
        }
    def lanzarMenu(self,manejadorJugador,manejadorEquipo,manejadorContrato):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: Crear un contrato.')
            print('-Ingrese 2: Consultar jugadores contrados.')
            print('-Ingrese 3: Consultar contratos.')
            print('-Ingrese 4:Obtener importe de contratos.')
            print('-Ingrese 5: Guardar Contratos.')
            print('-Ingrese 6:para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion==1:
                ejecutar(manejadorJugador,manejadorContrato,manejadorEquipo)
            elif opcion==2:
                ejecutar(manejadorJugador)
            elif opcion>2 and opcion<5:
                ejecutar(manejadorEquipo)
            elif opcion==5:
                ejecutar(manejadorContrato)
            else:
                ejecutar()
    def opcion1(self,manejadorJugador,manejadorContrato,manejadorEquipo):
        dni=input('Ingrese el dni:')
        jugadorCreado=False
        jugador=manejadorJugador.buscarJugador(dni)
        if jugador==-1:
            print("Ingrese los datos del jugador.")
            nombre=input('Ingrese el nombre:')
            ciudad=input('Ingrese la ciudad:')
            paisOrigen=input('Ingrese el pais:')
            print("Ingresar la fecha de nacimiento:")
            fechaNacimiento=self.cargarFecha()
            jugador=Jugador(nombre,dni,ciudad,paisOrigen,fechaNacimiento)
            jugadorCreado=True
        print('********Equipos*****')
        manejadorEquipo.mostrarDatos()
        iden=self.cargarNumeroEntero()
        equipo=manejadorEquipo.buscarEquipo(iden)
        if equipo!=-1:
            resultado=manejadorEquipo.verificarContrato(dni,iden)
            if resultado:
                print("EXISTE UN CONTRATO ENTRE EL JUGADOR Y EL EQUIPO.")
            else:
                print('***Cargar Contrato***')
                print('Ingrese la fecha de inicio:')
                fechaInicio=self.cargarFecha()
                print('Ingrese la fecha de fin:')
                fechaFin=self.cargarFecha()
                bandera=True
                while bandera:
                    try:
                        pagoMensual=float(input('Ingrese el pago mensual:'))
                    except ValueError:
                        print('ERROR: Se debe ingresar un numero con punto(.)')
                    else:
                        bandera=False
                contrato=Contrato(fechaInicio,fechaFin,pagoMensual,jugador,equipo)
                manejadorContrato.agregarContrato(contrato)
                equipo.agregarContrato(contrato)
                jugador.agregarContrato(contrato)
                if jugadorCreado:
                    manejadorJugador.agregarJugador(jugador)
    def opcion2(self,manejadorJugador):
        dni=input('Ingrese el dni a buscar:')
        manejadorJugador.verificarContrato(dni)
    def opcion3(self,manejadorEquipo):
        identificador=self.cargarNumeroEntero('Ingrese el identificador a buscar:')
        manejadorEquipo.mostrarJugadores(identificador)
    def opcion4(self,manejadorEquipo):
        nombre=input('Ingrese el nombre del equipo:')
        manejadorEquipo.verificarImporteTotal(nombre)
    def opcion5(self,manejadorContrato):
        manejadorContrato.crearArchivo()
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def cargarFecha(self):
        fecha=None
        bandera=True
        while bandera:
            try:
                dia=int(input('Ingrese el dia:'))
                mes=int(input('Ingrese el mes:'))
                año=int(input('Ingrese el año:'))
                fecha=date(año,mes,dia)
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return fecha
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')