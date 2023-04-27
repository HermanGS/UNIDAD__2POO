import numpy as np
from ManejadorArreglo import arregloNumPy


if __name__ == '__main__':
    print("holasa")
    arregloPuntos = arregloNumPy(3,10)
    arregloPuntos.testArregloPuntos()
    punto0 = arregloPuntos.getUnPunto(0)
    arregloPuntos.calcularDistanciasP0(punto0)
    print("Que tiene el arreglo : ",arregloPuntos.retornaArreglo())
    arregloPuntos.mostrarPuntos()
    print(np.shape(arregloPuntos))