'''Se necesita desarrollar una aplicación que procese la información de las variables meteorológicas temperatura, humedad y presión atmosférica. El registro de estas variables se hace cada una hora durante todos los días del mes. Esto se guarda en un archivo de texto separado con coma que contiene los siguientes datos: número de día, hora, valor de la variable temperatura, valor de la variable humedad y valor de la variable presión atmosférica. Se genera un archivo por cada mes.

Defina la clase “Registro” que posea como atributos los valores de las tres variables meteorológicas que se registran.

Implemente un programa que:

1.    Defina una lista bidimensional en la que se almacene el registro de las variables meteorológicas (instancia de la clase Registro) para cada día del mes, por cada hora.

2.    Almacene en la lista bidimensional los datos registrados en el archivo.

3.    Presente un menú de opciones permita realizar las siguientes tareas:

3.1.        Mostrar para cada variable el día y hora de menor y mayor valor.

3.2.        Indicar la temperatura promedio mensual por cada hora.

3.3.        Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente formato.'''

'''3.4 Diagrama de secuencia'''


from ManejadorListaBidimensional import ManejadorLista
from Menu import Menu
from Registro import Registro
import csv

def testMenu():
    Menuc = Menu()
    lista = []
    Menuc.ElegirOP(lista,1)

def testIngresoArchivo():
    listaBidimensional = [[]]
    archivo = open("Temperaturas.csv")
    reader = csv.reader(archivo,delimiter = ';')
    for fila in reader:
     pass


def testIngresoRegistro():
    objetoRegistro = Registro()
    print("Printear el objeto registro : ")
    print(objetoRegistro)


def testPruebaManejadorLista():
    ManejadorL = ManejadorLista()
    ManejadorL.Mostrar()

if __name__ == '__main__':
    print("-------principal-------")

    testPruebaManejadorLista()










