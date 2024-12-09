from gestorEquipos import gestorEquipos

if __name__ == '__main__':
    print("Recuperatorio tema 1")


    gestorE = gestorEquipos()
    gestorE.IngresarEquipos()
    gestorE.Mostrar()
 

    print("\n")
    gestorE.MostrarDatosGestor()    #parece que es necesario usar los metodos get cuando queremos USAR un Atributo que es de una clase PADRE si o si

    print("\n")
    print("Ingrese una posicion para indicar el tipo de Equipo")
    pos = int(input("ingrese la posicion : "))
    try:
        gestorE.LecturaPosicion(pos)
    except IndexError:
        print("Indice Fuera de rango")

    print("\n")
    print("Ingrese un anio para indicar la CANTIDAD de Herramientas Electricas en ese ANIO")
    anio = str(input("ingrese el anio : "))
    print(gestorE.HerramientasElectricasPorAnio(anio))


    print("\n")
    print("Ingrese una capacidad de carga para indicar las Maquinarias con capacidad menor a esa capacidad")
    capacidad = int(input("ingrese la capacidad de carga : "))
    print(gestorE.MaquinariasConCapacidadMenorA(capacidad))

