from gestorEventos import gestorEventos

class Menu:


    def opcion(self):
        print("Elije una opcion:")
        print("a) Agregar eventos a la instancia de la clase de control definida anteriormente.\nb) Buscar por teclado el nombre de una banda y mostrar el título del concierto, género musical y hora de inicio de su presentación. En caso de no encontrar la banda, el programa debe lanzar una excepción (Exception).\nc) Mostrar para cada evento el título, número de asistentes previstos y un índice de popularidad\nd)Salir")
        op = str(input("ingrese la letra a - b - c"))
        while op != 'a' and op != 'b' and op != 'c':
            op = str(input("ingrese la letra a - b - c"))
        return op
    
    def opciones(self):
        gestorE = gestorEventos()
        gestorE.ingresar()

        op = self.opcion()

        while op != 'd':
            
            if op == 'a':
                gestorE.AgregarEvento()
            elif op == 'b':
                try:
                    nombreBanda = str(input("Ingrse el nombre de la banda a bucar la info : "))
                    gestorE.InfoPorBanda(nombreBanda)
                except ValueError:
                    print("Banda no encontrada")
            
            elif op == 'c':
                gestorE.MostrarEventos()
            elif op == 'd':
                break

            else: 
                print("Error con la opcion")

            op = self.opcion()
            
