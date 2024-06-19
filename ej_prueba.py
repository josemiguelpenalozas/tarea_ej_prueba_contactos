#19:43 hora inicio
#21:50 hora limite
#21:07 terminado
import os
from funciones import *



while True:
    os.system("cls")
    print("Gestion de contactos")
    print("1.Agregar contacto")
    print("2.Mostrar contacto")
    print("3.Guardar contatos en CSV")
    print("4.Salir")
    while True:
        try:
                opcion= int(input("ingrese la opcion de la accion a realizar: "))
                if opcion>0 and opcion<5 :
                    break
                else:
                    print("ERROR,valor ingresado erroneo")
        except:
            print("ERROR,Valor ingresado no valido")

    if opcion==1:
        funcion1()

    elif opcion==2:
        funcion2()

    elif opcion==3:
        funcion3()

    else:
        funcion4()
        break