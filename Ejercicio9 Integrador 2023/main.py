"""El archivo ‘alumnos.csv’ almacena la información de los alumnos inscriptos en las carreras de la
universidad. La estructura del mismo es la siguiente: dni, apellido, nombre, carrera, año de la
carrera que cursa.

El archivo ‘materiasAprobadas.csv’ almacena información de las materias que los alumnos
inscriptos en una carrera, han aprobado en los últimos tres meses, por examen, equivalencia o
promoción. La estructura de dicho archivo es la siguiente: dni, nombre de materia, fecha, nota,
aprobación (‘E’ – Examen, ‘X’ – Equivalencia, ‘P’ – Promoción).
Los archivos no presentan ningún orden en particular. """

from ManejadorAlumnos import ManejadorAlumnos
from ManejadorMateriasAprobadas import ManejadorMateriasAprobadas
from Menu import Menu

def testManejadorAlumno():
    ManejadorAlumnos1 = ManejadorAlumnos(3,10)
    ManejadorAlumnos1.testIngreso()
    ManejadorAlumnos1.IngresoAlumnosArchivoCSV()
    print("\n")
    ManejadorAlumnos1.MostrarAlumnos()
    print("\n")
    ManejadorAlumnos1.BusquedaAlumnoDni("34699111")
    
def testManejadorMateriasAprobadas():
    ManejadorMateriasAprobadas1 = ManejadorMateriasAprobadas()
    ManejadorMateriasAprobadas1.testIngresoMateria()
    ManejadorMateriasAprobadas1.IngresoMateriasAprobadasArchivoCSV()
    print("\n")
    ManejadorMateriasAprobadas1.mostrarMaterias()
    
def testMenu():
    ManejadorAlumnos1 = ManejadorAlumnos(3,10)
    ManejadorAlumnos1.IngresoAlumnosArchivoCSV()
    ManejadorMateriasAprobadas1 = ManejadorMateriasAprobadas()
    ManejadorMateriasAprobadas1.IngresoMateriasAprobadasArchivoCSV()
    Menuc = Menu()
    Menuc.ElegirOP(ManejadorAlumnos1,ManejadorMateriasAprobadas1)

if __name__ == '__main__':
    print(">------------------------------------ Principal ------------------------------------<")
    #testManejadorAlumno()
    #testManejadorMateriasAprobadas()
    testMenu()
    