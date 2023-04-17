


from pickle import FALSE


if __name__ == '__main__':
    lista = []
    for i in range(4):
        lista.append(i + 0.5)

    print("mostrar lista print ",lista)




    #mostrar
    #for i in lista:
     #   print(i)


    i = 0
    while i < len(lista):
        print(lista[i])
        i = i + 1 

    #Busqueda : 
    print("\n")

    op = float(input("Ingrese un numero para realizar una busqueda : "))


    j = 0
    band = False
    while j < len(lista) and band == False:
        if op == lista[j]:
            band = True
        else: 
            j = j + 1

    print("valor de j : {}".format(j))