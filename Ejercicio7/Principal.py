from ast import While
from Menu import Menu
from ViajeroFrecuente import ViajeroFrecuente
import csv

def test():
    viajero1 = ViajeroFrecuente(1,"44808998","herman","soria",20)
    viajero2 = ViajeroFrecuente(2,"44808338","renzo","miraini",30)
    print(viajero1,"\n",viajero2)
    if viajero1 > viajero2:
        print("El primero es mayor(tiene mas millas) que el segundo")
    else: print("El Segundo tiene mas millas acumuladas que el primero")
    viajero1 = viajero1 + 31
    print("Nuevas millas acumuladas despues de la suma del Viajero 1 +31 millas (ACUMULAR MILLAS) : ",viajero1)
    viajero2 = viajero2 - 20
    print("Nuevo valor de las Millas Acumuladas, Se Canjearon 20 (CANJEAR MILLAS)",viajero2)
    print("Seguiran igual en cuanto a la comparacion ¿?")
    print("viajero1 > viajero2")
    print(viajero1 > viajero2 )
    print("\n\nAl revez -----------------------------------------")
    print(viajero1)
    print("viajero1 == 20, si es verdadero imprime  True , si es Falso imprime False")
    print(viajero1 == 20)
    print("Sobrecarga de Operadores por el reverso __radd__ y __rsub__ 10 + viajero1  , 15 - viajero1")
    viajero1 = 10 + viajero1
    print(viajero1)
    viajero1 = 15 - viajero1
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
        
        NumViajero = int(input("Ingrese un numero de viajero para ACCEDER A LAS OPCIONES   ( Ingrese Cero [0] para terminar)  :   ")) 

    print("\n...Terminando el Programa ...")



