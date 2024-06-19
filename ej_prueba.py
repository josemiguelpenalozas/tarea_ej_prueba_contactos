#19:43 hora inicio
#21:50 hora limite
import os
from funciones import *

contactos=[]

while True:
    print("Gestion de contactos")
    print("1.Agregar contacto")
    print("2.Mostrar contacto")
    print("3.Guardar contatos en CSV")
    print("4.Salir")
    try:
        while True:
            opcion= int(input("ingrese la opcion de la accion a realizar: "))
            if opcion>0 and opcion<5 :
                break
            else:
                print("ERROR,valor ingresado erroneo")
    except:
        print("ERROR,Valor ingresado no valido")
    if opcion==1:
        os.system("cls")
        while True:
            nombre=input("ingrese nombre del contacto: ")
            if len(nombre)>3:
                break
            else:
                os.system("cls")
                print("nombre no valido, ya que debe tener un largo minimo de 3 letras")
                esperar_tecla()

        while True:
            nro_tel=input("ingrese numero de telefono: ")
            if len(nro_tel)==8:
                break
            else:
                os.system("cls")
                print("Numero no valido,debe tener un  tamaño minimo e 8 digitos")
                esperar_tecla()

        while True:
            correo=input("ingrese correo electronico: ")
            if correo.__contains__("@"):
                break
            else:
                os.system("cls")
                print("El correo no es valido ya que no contiene @")
                esperar_tecla()


        contacto={
            "nombre":nombre,
            "numeror_telefonico":nro_tel,
            "correo":correo
        }
        contactos.append(contacto)
        print("Contacto añadido")
        esperar_tecla()

    elif opcion==2:
        os.system("cls")
        i=0
        while i<len(contactos):
            print(contactos[i])
            i=i+1
        esperar_tecla()

    elif opcion==3:
        os.system("cls")
        esperar_tecla()
    else:
        os.system("cls")
        print("gracias por usar nuestra gestion de contactos")
        print("Adios")
        break
