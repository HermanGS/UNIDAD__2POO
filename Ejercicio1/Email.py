'''
Defina una clase “Email” con los siguientes atributos: idCuenta, dominio, tipo de dominio y contraseña (todos estos datos se ingresan por teclado). Y los siguientes métodos:

a- El constructor.

b- Método “retornaEmail()” que construye una dirección e-mail con los valores de los atributos de Email. Por ejemplo:

idCuenta.: alumnopoo

dominio: gmail

tipoDominio: com

Resultado devuelto por retornaEmail: alumnopoo@gmail.com

c- Método “getDominio()”, que retorna el dominio.

d- Método “crearCuenta(), crea una cuenta a partir de una dirección de correo que recibe como parámetro.

Implemente un programa que permita:

1- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email) y luego imprima el siguiente mensaje:

Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.

2- Para la instancia creada en el ítem anterior, modificar la contraseña, teniendo en cuenta que se debe ingresar la contraseña actual, y ésta debe ser igual a la registrada en la instancia. Luego se debe ingresar la nueva contraseña y realizar la modificación correspondiente.

3- Crear un objeto de clase Email, a partir de una dirección de correo, como por ejemplo: informatica.fcefn@gmail.com, wicc2019@unsj-cuim.edu, juanLiendro1957@yahoo.com, etc.

4- a) Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes, solo para las direcciones válidas, para las no válidas, mostrar mensaje de error indicando la dirección de email incorrecta.  b) Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual al ingresado. c) Construya el diagrama de secuencia correspondiente.
'''
class Email:
    __idCuenta = ""
    __dominio = ""
    __tipodedominio = ""
    __contraseña = ""


    def inicializar(self,idCuenta,dominio,tipodedominio,contraseña):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipodedominio = tipodedominio
        self.__contraseña = contraseña

    def retornaEmail(self):
        #print(type(self.__idCuenta))
        email = str(self.__idCuenta) + "@" + str(self.__dominio) + "." + str(self.__tipodedominio)
        print("Estimado <{}> te enviaremos tus mensajes a la dirección <{}>.".format(self.__idCuenta,email))
        return email

    def getDominio(self):
        return(self.__dominio)

    def crearCuenta(self,email):
        #informatica.fcefn@gmail.com

        cadena = email.split("@")
#       special_characters = "!@#$%^&*()-+?_=,<>/"
        self.__idCuenta = cadena[0]
        cadena2 = cadena[1].split(".")
        self.__dominio = cadena2[0]
        self.__tipodedominio = cadena2[1]



    def modificarContraseña(self):
        print("---------------------------------------------------------------\n")
        print("Quieres modificar la contraseña :  SI = seguir / NO = cancelar")
        cont = str(input(" ").lower().strip(" "))

        while cont != "si" and cont != "no":
           print("opcion incorrecta -- INGRESE SI O NO")
           cont = str(input(" ").lower().strip(" "))
        if cont == "si":
            print("Ingrese la Contraseña ACTUAL ")
            actual = str(input("  "))
            if actual == str(self.__contraseña):
                print("Ingrese la Contraseña NUEVA ")
                nueva = str(input(" "))
                self.__contraseña = nueva
            else:
                print("La conctraseña no es igual a la anterior")
                print("... Saliendo ...")

        else:
            print("... Saliendo ... \n")

        print("Contraseña final ==> '{}' \n".format(self.__contraseña))
        print("---------------------------------------------------------------\n")


