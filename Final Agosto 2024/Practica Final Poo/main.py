from clasePaciente import Paciente
from clasePacienteH import pacienteH
from clasePacienteA import pacienteA
from listaPacientes import listaPacientes
if __name__ == '__main__':

    PacienteAmbu = pacienteA('Augustus','Maximus','chau@gmail',2647778889,'pajero','chocolate',"OSDE")
    print("importe final Ambulatorio : ",PacienteAmbu.calcularImporte())
    
    PacienteHospi = pacienteH('Joako','Masman','hola@gmail',2645556669,18,'19/06','cancer',10,1000)
    print("importe final Hospitalizado : ",PacienteHospi.calcularImporte())




    listaP = listaPacientes()
    
    print("Ingrese el nuevo valor de consulta")
    nuevoValorConsulta = float(input("Nuevo valor : "))
    Paciente.setValorConsulta(nuevoValorConsulta)
    #PacienteAmbu.setValorConsulta(nuevoValorConsulta)
    ##listaP.CambiarValorConsulta(nuevoValorConsulta) NO FUNCA  ¿ TIENE QUE SER USANDO LA CLASE!!!
    print("\n\n\n")    
    
    
    listaP.insertarFinal()
    listaP.mostrar()
    listaP.importeTotalPacientes()
    print("\n\n\n")

    try:
        posicion=int(input("Ingrese una posicion:  "))
        paciente = listaP.posicionHDP(posicion)
        if type(paciente) == pacienteA:
            print("El paciente en esa posicion es un Paciente Ambulatorio")
        else:
            print("El paciente en esa posicion es un Paciente Hospitalizado")
    except IndexError:
        print(f"La posicion Ingresada ({posicion}) esta fuera de rango...")

