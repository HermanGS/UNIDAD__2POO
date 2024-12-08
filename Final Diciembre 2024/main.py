from ListaMedios import ListaMedios
import csv
from Menu import menu_principal

if __name__ == "__main__":
    listaM = ListaMedios()
    menuc = menu_principal()

    #listaM.leerLista()
    #listaM.mostrar()

    menuc.opciones()
