from gestorRutas import GestorRutas
from gestorVehiculos import GestorVehiculos
from menu import Menu
if __name__ == '__main__':
    print("final 44808998 Herman Gabriel Soria")

    print("\n")
    gestorRutas = GestorRutas()
    gestorRutas.ingresarCSV()
    gestorRutas.MostrarRutas()
    print("\n")
    gestorVehiculos = GestorVehiculos()
    print("\n")

    menu = Menu()
    menu.opciones(gestorVehiculos,gestorRutas)



