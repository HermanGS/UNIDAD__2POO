"""Voy a estar probando los Arreglos Numpy y sus funcionalidades , a ver que se cuece"""
from Manejador import ManejadorHombres




if __name__ == '__main__':
    print("hello world")
    ManejadorHombres1 = ManejadorHombres(3,10)
    ManejadorHombres1.TestPersonas()

    ManejadorHombres1.mostrarPersonas()
    print("------------------------------------------------------------------------------------------")
    ManejadorHombres1.mostrarPersonas2()