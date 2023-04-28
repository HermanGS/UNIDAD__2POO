from Menu import Menu
from ManejadorAlumnos import ManejadorAlumnos
from ManejadorMaterias import ManejadorMaterias


if __name__ == '__main__':
    
    MAlumnos = ManejadorAlumnos()
    MMaterias = ManejadorMaterias()

    MAlumnos.IngresoArchivo()
    MAlumnos.MostrarArregloAlumnos()

    ArregloAlu = MAlumnos.RetornaArreglo()

    print("-------------------------------------")
    MMaterias.IngresoArchivo()
    MMaterias.MostrarListaMaterias()

    print("\n")
    dni = int(input("Ingrese el dni del alumno para calcular los 2 Promedios"))
    MMaterias.PorDNIpromedio(44666213)

    MateriaP = str(input("Ingrese el nombre de la Materia para Saber los Alumnos que la promocionaron"))
    MMaterias.MateriaPromocionalFormato(ArregloAlu,"Sistemas Digitales")


    
    MAlumnos.Ordema()
    MAlumnos.MostrarArregloAlumnos()
    
    print("Alumnos Sin Rendir:")
    MMaterias.AlumnosSinRendir(ArregloAlu)
    print("\n")
    MAlumnos.MostrarArregloAlumnos()
    Menuc = Menu()

    op = -1
    
    while op !=5:
        Menuc.Menuopciones()
        op = int(input("Ingrese una opcion "))
        while op<1 or op>5:
            print("Error - Ingrese la opcion de  nuevo ")
            op = int(input("Ingrese una opcion "))
        Menuc.ChoseOP(op,MAlumnos,MMaterias)
