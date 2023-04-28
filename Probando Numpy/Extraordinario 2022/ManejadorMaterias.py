import csv
from MateriasAprobadas import MateriasAprobadas


class ManejadorMaterias:

    def __init__(self):
        self.__ListaMaterias = []


    def IngresoArchivo(self):
        archivo = open('materiasAprobadas.csv')
        reader = csv.reader(archivo,delimiter = ';')

        for fila in reader:
            
            dni = int(fila[0])
            nombreMateria = str(fila[1])
            fecha = str(fila[2])
            nota = int(fila[3])
            aprobacion = str(fila[4])

            ObjetoMateriasA = MateriasAprobadas(dni,nombreMateria,fecha,nota,aprobacion)
            self.__ListaMaterias.append(ObjetoMateriasA)
        archivo.close()

    def MostrarListaMaterias(self):
        for i in self.__ListaMaterias:
            print(i)

    def PorDNIpromedio(self,dni):

        PromedioCaplazos = 0
        cantConAplazos = 0
        PromedioSaplazos = 0
        cantSinAplazos = 0

        for i in range(len(self.__ListaMaterias)):
            if dni == self.__ListaMaterias[i].getDni():
                if self.__ListaMaterias[i].getDni():
                    PromedioCaplazos = PromedioCaplazos + self.__ListaMaterias[i].getNota()
                    cantConAplazos = cantConAplazos + 1 
                    if self.__ListaMaterias[i].getNota() > 3:
                        PromedioSaplazos = PromedioSaplazos + self.__ListaMaterias[i].getNota()
                        cantSinAplazos = cantSinAplazos + 1
        
        PromedioCA = PromedioCaplazos / cantConAplazos
        PromedioSA = PromedioSaplazos / cantSinAplazos

        print ("Promedio Con Aplazos : {}",PromedioCA)
        print ("Promedio Sin Aplazos : {}",PromedioSA)


    def MateriaPromocionalFormato(self,ArregloAlumnos,MateriaP):
        print("DNI      Apellido y nombre     Fecha   Nota      Año que cursa")
        cadena = ""
        i=0
        while i<len(self.__ListaMaterias) and self.__ListaMaterias[i].getNombreMateria() != MateriaP:
            i=i+1
        
        if i<len(self.__ListaMaterias):

            for j in range (len(ArregloAlumnos)):
                if self.__ListaMaterias[i].getDni() == ArregloAlumnos[j].getDni():
                    print("{}       {}      {}      {}      {}".format(self.__ListaMaterias[i].getDni(),ArregloAlumnos[j].getNomyApe(),self.__ListaMaterias[i].getFecha(),self.__ListaMaterias[i].getNota(),ArregloAlumnos[j].getAño()))

        
    def AlumnosSinRendir(self,ArregloAlumnos):
        
        for i in range(len(ArregloAlumnos)):
            j = 0
            bandera = None
            while j < len(self.__ListaMaterias) and ArregloAlumnos[j].getDni() != self.__ListaMaterias[j].getDni():
                j = j +1
            if j<len(self.__ListaMaterias):
                  bandera = ArregloAlumnos[j]
            if bandera == None:
                print(ArregloAlumnos[j])


    def AlumnosSinRendir2(self,ManejadorAlumnos):
        bandera = False
        for i in range(len(ManejadorAlumnos.RetornaArreglo())):
            
            for j in range(len(self.__ListaMaterias)):

                if ManejadorAlumnos.RetornaArreglo()[i].getDni() == self.__ListaMaterias[j].getDni():
                    print("primero",ManejadorAlumnos.RetornaArreglo()[i].getDni())
                    print("segundo",self.__ListaMaterias[j].getDni())
                    bandera = True
            if bandera == False :
                print(ManejadorAlumnos.RetornaArreglo()[i])

    

    
