'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 7: Arreglos Unidimensionales
Archivo De Funciones
Fecha: 6 De Octubre De 2022
'''

import random
from array import*
'''
Ejercicio 1: Función que capture e imprima un arreglo de N números enteros introducidos por el usuario,
             posteriormente el arreglo se imprimirá.
'''
def captura():
    n=int(input("Cuantos Elementos Quieres Capturar? "))
    numeros=array('f',[])
    for x in range (n):
        num=float(input("Captura Un Número: "))
        numeros.append(num)
    print("Números Capturados: ",end="")
    for t in numeros:
        print(t,end=", ")

'''
Ejercicio 2: Función que regrese un mensaje indicando si se encuentra o no se encuentra un numero en una lista
             llamada Cali de 100 datos, suponer que la lista ya contiene datos y estos fueron definidos por el usuario.
'''
def findNumber():
    cali=[95, 95, 65, 14, 91, 101, 65, 60, 68, 48, 66, 10, 49, 101, 78, 3, 52, 
          96, 10, 84,80, 82, 100, 11, 80, 19, 32, 34, 94, 101, 72, 20, 94, 4, 
          27, 6, 4, 75, 70, 97, 23, 4, 58, 76, 62, 89, 49, 25, 96, 40,16, 54,
          23, 51, 5, 89, 24, 24, 78, 5, 96, 13, 14, 2, 51, 42, 83, 76, 73, 23,
          85, 19, 65, 74, 46, 26, 31, 55, 38, 33, 32, 46, 32, 43, 91, 99, 17,
          91, 94, 39, 55, 20, 91, 68, 101, 63, 82, 35, 21, 84]
    wanted=int(input("Cual Número Quieres Buscar? "))
    flag=False
    i=0
    for x in cali:
        if cali[i]==wanted:
            flag=True
            break
        i+=1
    if flag==True:
        return "Se Encontro El Número"
    else:
        return "No Se Encontró"

'''
Ejercicio 3: Función que inicialice todos los elementos de un arreglo de 50 datos con números aleatorios, al final
             imprimir el arreglo resultante.
'''
def randomFill():
    randoms=[]
    for x in range(50):
        randoms.append(random.randint(1,101)) 
    print("Datos Del Arreglo:",randoms)

'''
Ejercicio 4: Función que almacene en un arreglo de N números flotantes. Calcular el promedio e indicar cuántos
             elementos del vector son mayores que el promedio.
'''
def mayores_promedio():
    n=int(input("Cuantos Números Quieres Capturar: "))
    numeros=array('f',[])
    suma=0
    size=0
    for x in range (n):
        num=float(input("Captura Un Número: "))
        suma+=num
        size+=1
        numeros.append(num)
    promedio=suma/size
    mayores=[]
    for t in numeros:
        if t>promedio:
            mayores.append(t)
    print("El Promedio De Los Datos Es",round(promedio,4))
    print("Números Mayores Al Promedio:",mayores)

'''
Ejercicio 5: Función que permita al usuario crear su correo electrónico de la siguiente manera: le solicitará al usuario
             el apellido paterno y la matricula (no deberá exceder de 10 caracteres en caso de ser así solicitara
             nuevamente los datos).
             Se le presentaran las siguientes opciones con el tipo de correo que desea:
                a.- hotmail
                b.- gmail
             Posteriormente se une el apellido + matricula + @ + hotmail o gmail (según la opción elegida).
'''
def mail():
    apellido=str(input("Cual Es Tu Apellido? "))
    matricula=str(input("Captura Tu Matricula "))
    while len(matricula)>10:
        print("La Matrícula Debe Tener Menos De 10 Caracteres")
        matricula=str(input("Captura Tu Matricula: " ))
    print("Selecciona Una Opción: ")
    print("1) hotmail ")
    print("2) gmail")
    opc=int(input("Opción A Usar: "))
    while(opc<1 or opc>2):
        print("Selecciona Una Opción Valida")
        opc=int(input("Opción A Usar: "))
    if opc==1:
        dominio="hotmail"
    else:
        dominio="gmail"
    print("Correo Creado:",apellido+matricula+"@"+dominio+".com")

#Funciones Auxiliares
def menu():
    print(                  "Menu")
    print("1) Captura e Imprimir Un Arreglo De N Números")
    print("2) Busqueda En Lista Definida ")
    print("3) Arreglo Con Datos Aleatorios")
    print("4) Números Mayores Al Promedio De Un Array")
    print("5) Crear Correo")
