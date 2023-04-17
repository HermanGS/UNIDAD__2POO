from ast import While
from Menu import Menu
from ViajeroFrecuente import ViajeroFrecuente
import csv

def test():
    viajero1 = ViajeroFrecuente(1,"44808998","herman","soria",20)
    print(viajero1)



if __name__ == '__main__':
    print("Principal")
    print("Testeo Inicio -------------------------------------------")
    test()
    print("Testeo FIN    -------------------------------------------")


    #CargaObjetosDelArchivo ---------------------------------------------------------------------------------

    listaViajeros = []
    archivo = open("ViajerosFrecuentes.csv")
    reader = csv.reader(archivo,delimiter = ",")
    for fila in reader:
        ObjetoViajero = ViajeroFrecuente(int(fila[0]),str(fila[1]),str(fila[2]),str(fila[3]),int(fila[4]))
        listaViajeros.append(ObjetoViajero)

    
    #Mostrar todos los objetos de la lista -----------------------------------------------------------------
    
    print("\n -------------------------------------------")
    for viajero in listaViajeros:
        print(viajero)
    print("-------------------------------------------\n")
    
    #Búsqueda de un Viajero y Menu de opciones -------------------------------------------------------------
    #NumViajero = -1
    NumViajero = int(input("Ingrese un numero de viajero para ACCEDER A LAS OPCIONES   ( Ingrese Cero [0] para terminar)  :   ")) 
    while NumViajero != 0:    
        while NumViajero >= len(listaViajeros) or NumViajero < 0:
            print("Opcion Incorrecta , El numero de Viajero NO existe   , Ingrese de nuevo : ")
            NumViajero = int(input("==> "))

        
        i = 0
        bandera = False

        while i < len(listaViajeros) and bandera == False:

            if NumViajero == listaViajeros[i].getNumeroViajero():
                bandera = True
            else: i = i + 1

        #print("valor del indice : {}".format(i))
        

        #Ingreso Al Menu con el indice del viajero Encontrado ... -----------------------------------------------

        Menuc = Menu()
        Menuc.ElegirOpcion(listaViajeros,i)
    print("...Terminando el Programa ...")



