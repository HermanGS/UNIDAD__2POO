from Ventana import Ventana


if __name__ == '__main__':

    print("|------------Principal------------|\n\n\n")

    print('==== Ventana Inicio ====')

    ventanaInicio= Ventana('Inicio')

    ventanaInicio.mostrar()

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print("\n\n")
    print('==== Ventana Cargar ====')

    ventanaCargar= Ventana('Cargar',10,20)

    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaCargar.getTitulo(),ventanaCargar.alto(),ventanaCargar.ancho()))
    
    ventanaCargar.mostrar()

    print('*** Mueve a la derecha 10 ***')

    ventanaCargar.moverDerecha(10)

    ventanaCargar.mostrar()

    print('*** Mueve a la izquierda 10 ***')

    ventanaCargar.moverIzquierda(10)

    ventanaCargar.mostrar()

    print('*** Bajar  10 ***')

    ventanaCargar.bajar(10)

    ventanaCargar.mostrar()

    print("\n\n")
    print('==== Ventana Borrar ====')

    ventanaBorrar = Ventana('Borrar', 10,20,100,200)

    ventanaBorrar.mostrar()

    print('*** Subir 5 ***')

    ventanaBorrar.subir(5)   

    ventanaBorrar.mostrar()

    print('*** Subir  sin especificar ***')

    ventanaBorrar.subir()

    ventanaBorrar.mostrar()

    print('*** Bajar sin especificar ***')

    ventanaBorrar.bajar()

    ventanaBorrar.mostrar()

    print("\n\n")
    print('==== Ventana Extra ====')

    ventanaExtra = Ventana('Extra',0,0,1,1)

    ventanaExtra.mostrar()

    print('*** Bajar 25  ( Intento de Verificacion de Condiciones ) ***')

    ventanaExtra.subir()   

    ventanaExtra.mostrar()
