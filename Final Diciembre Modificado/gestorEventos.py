from claseConcierto import Concierto
from claseExposicionArte import ExposicionArtistica
import csv
class gestorEventos:
    __listaEventos: list


    def __init__(self):
        self.__listaEventos = []


    def ingresar(self):
        archivo = open('Eventos.csv')
        reader = csv.reader(archivo,delimiter=",")

        saltarEncabezado = True
        
        for fila in reader:

            if saltarEncabezado == True:
                saltarEncabezado = False
        
            else:
                tipo = str(fila[0])
                titulo = str(fila[1])
                numeroAsistentes = int(fila[2])

                if tipo == 'C':
                    generoMusical = str(fila[3])
                    duracionHs = str(fila[4])
                    obj = Concierto(titulo,numeroAsistentes,generoMusical,duracionHs)
                elif tipo == 'E':
                    frecuencia = str(fila[3])
                    numeroObras = int(fila[4])
                    obj = ExposicionArtistica(titulo,numeroAsistentes,frecuencia,numeroObras)

                self.__listaEventos.append(obj)

    def MostrarEventos(self):
        for i in range(len(self.__listaEventos)):
            print(self.__listaEventos[i])

    
    #a)
    
    def AgregarEventoConcierto(self,titulo,numeroAsistentes,generoMusical,duracionHs):
        obj = Concierto(titulo,numeroAsistentes,generoMusical,duracionHs)
        self.__listaEventos.append(obj)

    def AgregarEventoExposicion(self,titulo,numeroAsistentes,frecuencia,numeroObras,):
        obj = ExposicionArtistica(titulo,numeroAsistentes,frecuencia,numeroObras)
        self.__listaEventos.append(obj)

    def AgregarEvento(self,):
        print("Ingresando Evento:")
        print("Ingrese los datos del Nuevo Evento:")
        print("Ingrese una OPCION :  Concierto = 1  /  Exposicon = 2")
        op = int(input("opcion : "))
        while op != 1 and op != 2:
            op = int(input("opcion : "))

        titulo = str(input("titulo : "))
        numeroAsistentes = str(input("numero de asistentes : "))

        if op == 1:
            detalle1 = str(input("generoMusical : "))
            detalle2 = str(input("duracionHs : "))
            self.AgregarEventoConcierto(titulo,numeroAsistentes,detalle1,detalle2)

        if op == 2:
            detalle1 = str(input("frecuencia : "))
            detalle2 = str(input("numeroObras : "))
            self.AgregarEventoExposicion(titulo,numeroAsistentes,detalle1,detalle2)



    #b)

    """b) Buscar por teclado el nombre de una banda y mostrar el título del concierto, género musical y hora de inicio de su presentación.
     En caso de no encontrar la banda, el programa debe lanzar una excepción (Exception)."""
    
    def InfoPorBanda(self,NombreBanda):
        encontrado = False
        i = 0
        while i<len(self.__listaEventos) and encontrado == False:
            if isinstance(self.__listaEventos[i],Concierto):

               encontrado = self.__listaEventos[i].BuscarNombreBanda(NombreBanda)
               
            if encontrado == True:
                break
            i += 1

        if encontrado == True:
            print("Titulo del Concierto : ",self.__listaEventos[i].getTitulo())
            print("Genero Musical del Concierto : ",self.__listaEventos[i].getGeneroMusical())
        elif encontrado == False:
            raise ValueError

    