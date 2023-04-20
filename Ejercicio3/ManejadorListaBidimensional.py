from Registro import Registro



class ManejadorLista:
    __listaRegistros : list


    def __init__(self):
        self.__listaRegistros = []
        ObjetoRegistro = Registro()
        for i in range(5):
            for j in range(5):
                self.__listaRegistros[i][j] = ObjetoRegistro

    def Mostrar(self):
        for i in range(5):
            for j in range(5):
                print(self.__listaRegistros[i][j])

    






