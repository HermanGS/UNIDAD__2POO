



class Persona:


    def __init__(self,id,Nombre,Apellido,email,profesion):
        self.__Id = id
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__Email = email
        self.__Profesion = profesion 

    def __str__(self) -> str:
        return "| {} | {} | {} | {} | {} |".format(self.__Id,self.__Nombre,self.__Apellido,self.__Email,self.__Profesion)