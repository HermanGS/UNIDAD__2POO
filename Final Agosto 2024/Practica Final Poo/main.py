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
    listaP.insertarFinal()
    listaP.mostrar()