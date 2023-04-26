

class Menu:




    def PresentarMenu(self):


        """
    def ElegirOpcion(self,lista,indice):
        
        print("\n Ingrese 'a' , 'b' o 'c' para realizar las operaciones correspondientes \n a- Consultar Cantidad de Millas.\n b- Acumular Millas. \n c- Canjear Millas.")
        print("Ingrese '0' (cero) para terminar el Bucle ...")
        opcion = str(input(" \n / Respuesta / :  ")).lower().strip(" ")

        while opcion != 'a' and opcion != 'b' and opcion != 'c' and opcion != '0':
            print("OPCION INCORRECTA - Ingrese [Cero (0) para TERMINAR ]  Ó  Ingrese de nuevo la opcion : ")
            opcion = str(input("Respuesta :  ")).lower().strip(" ")
        print("tipo y valor de la opcion elegida",type(opcion),opcion)
        op = '1'
        while op != '0':

            
            op = 
            print(op != '0')
            print("tipo y valor de la opcion elegida",type(op),op)
            #print(" La op es ",op,"\n")
            if op == 'a':
                print("Cantidad de Millas TOTALES :  ")
                self.opcionA_CantidadMillas(lista,indice)
            elif op == 'b':
                print("Acumular MILLAS : ")
                self.opcionB_AcumularMillas(lista,indice)
            elif op == 'c':
                print("Canjear MILLAS : ")
                self.opcionC_CanjearMillas(lista,indice)
            else:
                print("==> ... Saliendo ... <==")
        """
    def ElegirOpcion(self,lista,indice):
        op = -1
        while op != 0:
            print("\n Ingrese '1' , '2' , '3' o '4' para realizar las operaciones correspondientes \n 1- Consultar Cantidad de Millas.\n 2- Acumular Millas. \n 3- Canjear Millas. \n 4- Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor (> o  __gt__ en python).")
            print("Ingrese '0' (cero) para terminar el Bucle ...")
            op = input("Respuesta : ")
            op = int(op)
            while op < 0 and op > 4:
                print("ERROR - ingreso incorrecto, vuelva a ingresar : ")
                op = input("Respuesta : ")
                op = int(op)
            if op == 1:
                print("Cantidad de Millas TOTALES :  ")
                self.opcionA_CantidadMillas(lista,indice)
            elif op == 2:
                print("Acumular MILLAS : ")
                self.opcionB_AcumularMillas(lista,indice)
            elif op == 3:
                print("Canjear MILLAS : ")
                self.opcionC_CanjearMillas(lista,indice)
            elif op == 4:
                print("Determinar el Viajero con mayor cantidad de millas acumuladas : ")
                self.opcionD_ViajeroConMayorCantidadDeMillas(lista)
            else:
                print("==> ... Saliendo ... <==")


    # MÉTODOS DE LAS OPCIONES

    def opcionA_CantidadMillas(self,lista,indice):
        print(lista[indice].CantidadTotalMillas())

    def opcionB_AcumularMillas(self,lista,indice):
        
        Suma = float(input("Ingrese la cantidad que quiera acumular al total de las millas  : "))
        lista[indice].AcumularMillas(Suma)

    def opcionC_CanjearMillas(self,lista,indice):
        cantCanje = float(input("Ingrese la cantidad que quiera CANJEAR del total de millas :  "))
        lista[indice].CanjearMillas(cantCanje)
    
    def opcionD_ViajeroConMayorCantidadDeMillas(self,lista):
        max = lista[0]
        #print("max inicial",max)
        for i in range(len(lista)):
            #print("lista[i] = ",lista[i])
            #print("max = ",max)
            #print("Evaluacion de la condicion da como resultado ,{} ".format(max >lista[i]))
            if lista[i] > max:
                max = lista[i]
                #print("Actualizacion de max = ",max)
        print("El viajero con mas millas Acumuladas es , ",max)