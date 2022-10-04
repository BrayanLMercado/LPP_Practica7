'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 7: Arreglos Unidimensionales
Archivo Principal
Fecha: 6 De Octubre De 2022
'''

from pract7Func import*

def main():
    menu()
    opc=int(input("Selecciona Una Opción: "))
    while opc<1 or opc>5:
        print("Selecciona Una Opción Valida")
        menu()
    if opc==1:
        captura()
    elif opc==2:
        print(findNumber())
    elif opc==3:
        randomFill()
    elif opc==4:
        mayores_promedio()
    else:
        mail()

main()