import msvcrt
import os
import csv
contactos=[]

def esperar_tecla():
    print("presione cualquier tecla para avanzar")
    msvcrt.getch()

def funcion1():
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
            "numero telefonico":nro_tel,
            "correo":correo
        }
    contactos.append(contacto)
    print("Contacto añadido")
    esperar_tecla()

def funcion2():
    os.system("cls")
    i=0
    while i<len(contactos):
        print(contactos[i])
        i=i+1
    esperar_tecla()

def funcion3():
    os.system("cls")
    archivo_nombre=input("ingrese nombre del archivo: ")+".csv"
    nom_bus=input("ingrese el nombre del contacto del que quiere agregar: ")
    x=0
    encontrado=0
    while x <len(contactos):
        if contactos[x]["nombre"]==nom_bus:
            nomcont=contactos[x]["nombre"]
            nro_cont=contactos[x]["numero telefonico"]
            correo_cont=contactos[x]["correo"]
            texto=[nomcont,nro_cont,correo_cont]
            encontrado=1
        x=x+1
    if encontrado==1:
        with open(archivo_nombre,"a",newline="") as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow(texto)
    esperar_tecla()

def funcion4():
    os.system("cls")
    print("gracias por usar nuestra gestion de contactos")
    print("Adios")
