from Email import Email
import csv


def test():

    objeto = Email.inicializar("hh","gmail","com","123")
    print(objeto.retornaEmail())



def test2():
    print("Ingrese el Nombre del Propietario de la Cuenta : ")
    name = input("   ")
    print("---Creación del Email---")

    idcuenta = str(input("Ingrese la ID de la cuenta : "))
    dominio = str(input("Ingrese el DOMINIO de la cuenta : "))
    tipodeDominio = str(input("Ingrese el TIPO DE DOMINIO de la cuenta : "))
    contraseña = str(input("Ingrese la CONTRASEÑA "))

    unobjeto = Email()
    unobjeto.inicializar(idcuenta,dominio,tipodeDominio,contraseña)
    unobjeto.retornaEmail()
    unobjeto.modificarContraseña()

    #Creacion objeto Email mediante una Direccion Email ya existente
    exampleEmail = "informatica.fcefn@gmail.com"
    otroObjeto = Email()
    otroObjeto.crearCuenta(exampleEmail)
    otroObjeto.retornaEmail()

def test3():

    listaEmails = []
    archivo = open("archivoEmails.csv")
    reader = csv.reader(archivo)
    contador = 0
    for fila in reader:
        contador = contador + len(fila)
        for email in fila:
            objetoEmail = Email()
            objetoEmail.crearCuenta(email)
            listaEmails.append(objetoEmail)

    archivo.close()

    print("Cantidad de Emails Procesados  : ",contador)
    print("Cantidad de Emails Almacenados : ",len(listaEmails))

    print("---------------------------------------------------------------\n")
    for i in range(len(listaEmails)):

        listaEmails[i].retornaEmail()
    print("---------------------------------------------------------------\n")
    return(listaEmails)

def test4(lista):
    dominio = str(input(("Ingrese un Dominio para buscar la cantidad de Emails con Ese DOMINIO :  ")))
    cont = 0


    for elemento in lista:
        if dominio == elemento.getDominio():
            cont += 1

    print("El Dominio de <{}> tiene una cantidad de <{}> existencias en la lista de Emails".format(dominio,cont))

if __name__ == '__main__':
    '''

    '''
    lista = test3()
    test4(lista)

    print("Fin")
