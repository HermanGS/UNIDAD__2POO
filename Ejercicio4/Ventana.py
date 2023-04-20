


class Ventana:
    __titulo : str
    __Xsupiz : int
    __Ysupiz : int
    __Xinfde : int
    __Yinfde : int

    def __init__(self,titulo,Xsupiz = 0,Ysupiz = 0 ,Xinfde = 500,Yinfde = 500):
        if type(titulo) == str and type(Xsupiz) == int and type(Ysupiz) == int and type(Xinfde) == int and type(Yinfde) == int:
            self.__titulo = titulo
            self.__Xsupiz = Xsupiz
            self.__Ysupiz = Ysupiz
            self.__Xinfde = Xinfde
            self.__Yinfde = Yinfde



    def mostrar(self):
        print("( XsupIz = {} , YsupIz = {})  | (XInfDe = {} , YinfDe = {})".format(self.__Xsupiz,self.__Ysupiz,self.__Xinfde,self.__Yinfde))

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return (self.__Yinfde - self.__Ysupiz)
    
    def ancho(self):
        return (self.__Xinfde - self.__Xsupiz)

    def moverDerecha(self,cantidad = 1):
        if (self.__Xinfde + cantidad) <= 500  and (self.__Xsupiz + cantidad) <= 500 and (self.__Xsupiz < self.__Xinfde):
            self.__Xinfde += cantidad
            self.__Xsupiz += cantidad

    def moverIzquierda(self,cantidad = 1):
        if (self.__Xinfde - cantidad) >= 0 and (self.__Xsupiz - cantidad) >= 0 and (self.__Xsupiz < self.__Xinfde):
            self.__Xinfde -= cantidad
            self.__Xsupiz -= cantidad

    def subir(self,cantidad = 1):
        if (self.__Yinfde - cantidad) >= 0 and (self.__Ysupiz - cantidad) >= 0 and (self.__Ysupiz < self.__Yinfde):
            self.__Yinfde -= cantidad
            self.__Ysupiz -= cantidad

    def bajar(self,cantidad = 1):
        if (self.__Yinfde + cantidad) <= 500 and (self.__Ysupiz + cantidad) <= 500 and (self.__Ysupiz < self.__Yinfde):
            self.__Yinfde += cantidad
            self.__Ysupiz += cantidad 
        


    


