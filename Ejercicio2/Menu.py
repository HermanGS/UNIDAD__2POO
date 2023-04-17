

class Menu:




    def PresentarMenu(self):

        print("\n Ingrese 'a' , 'b' o 'c' para realizar las operaciones correspondientes \n a- Consultar Cantidad de Millas.\n b- Acumular Millas. \n c- Canjear Millas.")
        print("Ingrese '0' (cero) para terminar el Bucle ...")
        opcion = str(input(" \n / Respuesta / :  ")).lower().strip(" ")

        while opcion != 'a' and opcion != 'b' and opcion != 'c' and opcion != '0':
            print("OPCION INCORRECTA - Ingrese [Cero (0) para TERMINAR ]  Ó  Ingrese de nuevo la opcion : ")
            opcion = str(input("Respuesta :  ")).lower().strip(" ")
        return (opcion)

    def ElegirOpcion(self,lista,indice):
        op = '1'
        while op != '0':
            
            
            op = self.PresentarMenu()

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


    # MÉTODOS DE LAS OPCIONES

    def opcionA_CantidadMillas(self,lista,indice):
        print(lista[indice].CantidadTotalMillas())

    def opcionB_AcumularMillas(self,lista,indice):
        
        Suma = float(input("Ingrese la cantidad que quiera acumular al total de las millas  : "))
        lista[indice].AcumularMillas(Suma)

    def opcionC_CanjearMillas(self,lista,indice):
        cantCanje = float(input("Ingrese la cantidad que quiera CANJEAR del total de millas :  "))
        lista[indice].CanjearMillas(cantCanje)