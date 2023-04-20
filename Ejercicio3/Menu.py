



class Menu:
    __nothing : None

    def op1(self):
        print("ENTRO AL 1")

    def op2(self):
        print("ENTRO AL 2")

    def op3(self):
        print("ENTRO AL 3")

    def ElegirOP(self,Lista,op):
        op = 1
        while op != 0 :
            print("\n\n")
            print("__________________________________________________________________________________________________________________")
            print("<---------------->")
            print("Elige una de estas opciones para Realizar una Operación")
            print("(1) <==> Mostrar para cada variable el día y hora de menor y mayor valor.\n(2) <==> Indicar la temperatura promedio mensual por cada hora.\n(3) <==> Dado un número de día listar los valores de las tres variables para cada hora del día dado. El listado debe tener el siguiente")
            print("<---------------->")
            print("\n")
            op = int(input("(Ingrese 0 para Finalizar el Programa) ==> Respuesta :  "))
            while op < 0 and op > 3:
                print("<---------------->")
                op = int(input("Respuesta INCORRECTA, vuelva a ingregsar su opcion  :  "))
                print("<---------------->")
            if op == 1:
                self.op1()
            elif op == 2:
                self.op2()
            elif op == 3:
                self.op3()
            else: print("______________ Saliendo del Programa ______________")
