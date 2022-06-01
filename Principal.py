from ManejadorContrato import ManejaContrato
from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejaJugador
from Menu import Menu
if __name__=='__main__':
    manejadorJugador=ManejaJugador()
    manejadorContrato=ManejaContrato()
    menu=Menu()
    manejadorEquipo=ManejadorEquipo()
    manejadorEquipo.cargarArchivo()
    menu.lanzarMenu(manejadorJugador,manejadorEquipo,manejadorContrato)
