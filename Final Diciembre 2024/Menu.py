from ListaMedios import ListaMedios
class menu_principal():


    def opciones(self):
        control = ListaMedios()
        control.leerLista()
    
        while True:
            print("\n--- Menú Principal ---")
            print("1. Agregar medio de comunicación")
            print("2. Listar medios de comunicación")
            print("3. Calcular Indice")
            
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("1: si es un medio de prensa")
                print("2: si es un medio de radio")
                opcion=input("Seleccione una opción: ")
                if opcion =="1":
                    nombre=str(input("Nombre del medio: "))
                    audiencia=str(input("Audiencia del medio: "))
                    cantSecc=int(input("cantSecc del medio: "))
                    periodicidad=str(input("periodicidad del medio: "))
                    control.agregarP(nombre, audiencia,cantSecc, periodicidad)
                elif opcion == "2":
                    nombre=str(input("Nombre del medio: "))
                    audiencia=str(input("Audiencia del medio: "))
                    frecuencia=str(input("frecuencia del medio: "))
                    control.agregarR(nombre, audiencia,frecuencia)
            elif opcion == "2":
                try:
                    nombre=str(input("Ingreese nombre del medio de radio que desea conocer los datos : "))
                    control.DatosRadio(nombre)
                except Exception:
                    print("Nombre de Radio inexistente")
            elif opcion == "3":
                control.IndicarDatosDelMedioeIndice()
                
            elif opcion == "4":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")



## Leer por teclado el nombre de un programa de radio y muestre el nombre del medio de comunicación,
#  la frecuencia y el horario de inicio de transmisión. El método que resuelve este 
##requerimiento debe lanzar una excepción (Excep on) en caso de no encontrar el nombre ingresado. 