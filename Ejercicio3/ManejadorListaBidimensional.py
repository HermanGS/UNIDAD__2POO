from Registro import Registro



class ManejadorLista:
    __listaRegistros : list


    def __init__(self):
        self.__listaRegistros = []
        ObjetoRegistro = Registro()
        for i in range(30):
            for j in range(24):
                self.__listaRegistros[i][j] = ObjetoRegistro






